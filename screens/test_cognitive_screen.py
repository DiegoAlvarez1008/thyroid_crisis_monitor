from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import time

class TestCognitiveScreen(Screen):
    def __init__(self, **kwargs):
        super(TestCognitiveScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.label_instruccion = Label(text="Responde lo más rápido posible:\n¿5 + 3 = ?", font_size=20)
        self.boton_correcto = Button(text="8", on_press=self.evaluar_respuesta)
        self.boton_incorrecto = Button(text="9", on_press=self.evaluar_respuesta)

        self.label_resultado = Label(text="", font_size=18)

        self.layout.add_widget(self.label_instruccion)
        self.layout.add_widget(self.boton_correcto)
        self.layout.add_widget(self.boton_incorrecto)
        self.layout.add_widget(self.label_resultado)

        self.add_widget(self.layout)

    def set_datos_previos(self, temp, fc):
        self.temp = temp
        self.fc = fc
        self.inicio = time.time()
        self.label_resultado.text = ""

    def evaluar_respuesta(self, instance):
        tiempo = time.time() - self.inicio
        correcta = instance.text == "8"
        puntaje_test = 10 if tiempo < 3 and correcta else 5 if correcta else 0

        total = puntaje_test
        if self.temp >= 38.5:
            total += 10
        if self.fc >= 100:
            total += 10

        self.label_resultado.text = f"Test: {'Correcto' if correcta else 'Incorrecto'} en {tiempo:.1f}s\nPuntaje total: {total}"
