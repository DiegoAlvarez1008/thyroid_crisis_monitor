from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random
from utils.puntajes import calcular_puntaje_total, evaluar_estado
#from utils.puntajes import calcular_puntaje_temp
#from utils.puntajes import calcular_puntaje_fc
#from utils.puntajes import calcular_puntaje_test
# IMPORTANTE SABER: 
#Estos 3 métodos no son necesarios porque se llaman desde el método calcular_puntaje_total en el archivo de 'utils/puntajes.py'

class MonitorScreen(Screen):
    def __init__(self, **kwargs):
        super(MonitorScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.label_temp = Label(text="Temperatura: -- °C", font_size=20)
        self.label_fc = Label(text="Frecuencia cardíaca: -- bpm", font_size=20)
        self.label_estado = Label(text="Estado: No evaluado", font_size=18, color=(1, 1, 1, 1))

        self.boton_medir = Button(text="Iniciar medición", on_press=self.realizar_medicion)
        self.boton_test = Button(text="Realizar test cognitivo", on_press=self.ir_a_test, disabled=True)

        self.layout.add_widget(self.label_temp)
        self.layout.add_widget(self.label_fc)
        self.layout.add_widget(self.label_estado)
        self.layout.add_widget(self.boton_medir)
        self.layout.add_widget(self.boton_test)

        self.add_widget(self.layout)

    def realizar_medicion(self, instance):
        # Vamos a simular la obtención de los valores de temperatura y frecuencia cardíaca porque por ahora no cuenton sensores ni con ESP32
        i = 0
        counter = 0
        while (i < 3): # Se comienza iterando porque se simula que se toman 3 mediciones para evaluar el estado del paciente
            i += 1
            temp = round(random.uniform(36.5, 41.0), 1)
            fc = random.randint(70, 140)

            #La verdadera obtención de los valores de puntuaciones de temperatura son:
            #temp = llamamos al método que recibirá dichos valores a través de la comunicación BLE con el ESP32
            # fc = llamamos al método que recibirá dichos valores a través de la comunicación BLE con el ESP32 
            self.label_temp.text = f"Temperatura: {temp} °C"
            self.label_fc.text = f"Frecuencia cardíaca: {fc} bpm"
            puntuacion = calcular_puntaje_total(temp, fc, 0, True)  # Simulamos un test con respuesta correcta: True y tiempo de respuesta: 0 segundos
            estado = evaluar_estado(puntuacion)

            if estado == "critico":
                counter += 1
                
            elif estado == "preocupante":
                self.label_estado.text = "Estado: PREOCUPANTE"
                self.label_estado.color = (1, 0.5, 0, 1)  # Naranja
                self.temp_actual = temp
                self.fc_actual = fc
                self.ir_a_test(None)
                return
                
                # Comenzamos con el test cognitivo porque sabemos que el estado es preocupante y no crítico
                # Acá iría código que deriva al test cognitivo, por ejemplo, habilitando un botón o cambiando de pantalla
                # Y luego también pondríamos una línea de código que suma el puntaje del test cognitivo al total de puntuaciones
                # Finalmente si está en CRÍTICO no tenemos que hacer validez alguna porque el test cognitivo es lo más preciso
                # Pasa al protocolo CRÍTICO

            else:
                self.label_estado.text = "Estado: Estable"
                self.label_estado.color = (0, 1, 0, 1)  # Verde
                self.boton_test.disabled = True
                break
            
            if counter >= 3:
                self.label_estado.text = "Estado: CRÍTICO ⚠️"
                self.label_estado.color = (1, 0, 0, 1)  # Rojo
                self.boton_test.disabled = True
                # PASA AL PROTOCOLO CRÍTICO
                
        self.temp_actual = temp
        self.fc_actual = fc        

    def ir_a_test(self, instance):
        self.manager.get_screen("test").set_datos_previos(self.temp_actual, self.fc_actual)
        self.manager.current = "test"