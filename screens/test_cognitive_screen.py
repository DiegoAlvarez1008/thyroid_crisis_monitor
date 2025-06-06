from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import time
from utils.puntajes import calcular_puntaje_total

class TestCognitiveScreen(Screen):
    def __init__(self, **kwargs):
        super(TestCognitiveScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.add_widget(self.layout)
        self.preguntas = [
            {"pregunta": "¿5 + 3 = ?", "opciones": ["8", "9"], "correcta": "8"},
            # Aquí puedes agregar más preguntas luego
        ]
        self.index = 0
        self.inicio = 0
        self.temp = 0
        self.fc = 0

    def set_datos_previos(self, temp, fc):
        self.temp = temp
        self.fc = fc
        self.index = 0
        self.layout.clear_widgets()
        self.mostrar_mensaje_intro()

    def mostrar_mensaje_intro(self):
        self.layout.clear_widgets()
        intro_label = Label(
            text="Usted va a realizar una pequeña prueba,\nresponda rápidamente y lo que crea correcto",
            font_size=22,
            color=(1, 1, 1, 1),
            halign="center"
        )
        self.layout.add_widget(intro_label)
        Clock.schedule_once(lambda dt: self.mostrar_pregunta(), 3)

    def mostrar_pregunta(self):
        self.layout.clear_widgets()
        pregunta = self.preguntas[self.index]

        self.label_pregunta = Label(text=pregunta["pregunta"], font_size=20)
        self.layout.add_widget(self.label_pregunta)

        for opcion in pregunta["opciones"]:
            btn = Button(text=opcion)
            btn.bind(on_press=self.evaluar_respuesta)
            self.layout.add_widget(btn)

        self.inicio = time.time()

    def evaluar_respuesta(self, instance):
        tiempo = time.time() - self.inicio
        correcta = instance.text == self.preguntas[self.index]["correcta"]
        total = calcular_puntaje_total(self.temp, self.fc, tiempo, correcta)

        self.layout.clear_widgets()
        resultado = Label(
            text=f"Test: {'Correcto' if correcta else 'Incorrecto'} en {tiempo:.1f}s\nPuntaje total: {total}",
            font_size=18
        )
        self.layout.add_widget(resultado)

        # Aquí puedes continuar con más preguntas si agregas más en el arreglo
