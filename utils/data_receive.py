"""

Nota: Este es un draft de cómo podríamos recibir la data por BLE desde el ESP32 hacia la app del celular.

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass, cast
from time import sleep

# UUIDs personalizados (deben coincidir con los definidos en el código del ESP32)
SERVICE_UUID = '12345678-1234-1234-1234-1234567890ab'
CHARACTERISTIC_UUID = 'abcdefab-1234-5678-1234-abcdefabcdef'

# Clases de Java necesarias
BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothManager = autoclass('android.bluetooth.BluetoothManager')
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
BluetoothGattCallback = autoclass('android.bluetooth.BluetoothGattCallback')
UUID = autoclass('java.util.UUID')

class BLETemperatureApp(App):
    def build(self):
        self.label = Label(text="Buscando ESP32...", font_size='20sp')
        Clock.schedule_once(self.iniciar_ble, 2)
        return self.label

    def iniciar_ble(self, dt):
        context = cast(Context, PythonActivity.mActivity.getApplicationContext())
        self.bt_manager = context.getSystemService(Context.BLUETOOTH_SERVICE)
        self.bt_adapter = self.bt_manager.getAdapter()

        if not self.bt_adapter or not self.bt_adapter.isEnabled():
            self.label.text = "Bluetooth desactivado"
            return

        self.label.text = "Escaneando..."
        self.bt_adapter.startLeScan(self.le_scan_callback)

    def le_scan_callback(self, device, rssi, scanRecord):
        nombre = device.getName()
        if nombre and "ESP32-TEMP" in nombre:
            self.bt_adapter.stopLeScan(self.le_scan_callback)
            self.label.text = f"Dispositivo encontrado: {nombre}"

            # Conectar al dispositivo BLE
            self.gatt = device.connectGatt(PythonActivity.mActivity, False, self.gatt_callback)
            self.gatt.connect()

    def gatt_callback(self):
        # Obtener el servicio y la característica BLE
        service = self.gatt.getService(UUID.fromString(SERVICE_UUID))
        characteristic = service.getCharacteristic(UUID.fromString(CHARACTERISTIC_UUID))

        # Leer el valor de la característica
        self.gatt.readCharacteristic(characteristic)

        # Esperar la respuesta
        sleep(1)

        # Obtener el valor de la característica
        value = characteristic.getValue()
        if value:
            temp_bytes = value
            temp_str = ''.join([chr(b) for b in temp_bytes])
            self.label.text = f"Temperatura: {temp_str}°C"
        else:
            self.label.text = "Error al leer la temperatura"

        # Cerrar la conexión GATT
        self.gatt.disconnect()

BLETemperatureApp().run()

"""