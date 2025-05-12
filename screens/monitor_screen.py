from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random
from utils.thresholds import evaluar_parametros

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
        # Simular sensores
        temp = round(random.uniform(36.5, 41.0), 1)
        fc = random.randint(70, 140)

        self.label_temp.text = f"Temperatura: {temp} °C"
        self.label_fc.text = f"Frecuencia cardíaca: {fc} bpm"

        estado = evaluar_parametros(temp, fc)

        if estado == "critico":
            self.label_estado.text = "Estado: CRÍTICO ⚠️"
            self.label_estado.color = (1, 0, 0, 1)  # Rojo
            self.boton_test.disabled = True
        elif estado == "preocupante":
            self.label_estado.text = "Estado: PREOCUPANTE"
            self.label_estado.color = (1, 0.5, 0, 1)  # Naranja
            self.boton_test.disabled = False
        else:
            self.label_estado.text = "Estado: Estable"
            self.label_estado.color = (0, 1, 0, 1)  # Verde
            self.boton_test.disabled = True

        # Guardar datos simulados por si luego se usan
        self.temp_actual = temp
        self.fc_actual = fc

    def ir_a_test(self, instance):
        # Guardar valores para pasarlos al test cognitivo
        self.manager.get_screen("test").set_datos_previos(self.temp_actual, self.fc_actual)
        self.manager.current = "test"
