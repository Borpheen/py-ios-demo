from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Root(BoxLayout):
    def __init__(self, **kw):
        super().__init__(orientation="vertical", padding=24, spacing=16, **kw)
        self.lbl = Label(text="Hello from Python on iOS!")
        self.add_widget(self.lbl)
        self.add_widget(Button(text="Tap me", on_press=lambda *_: self.tap()))
    def tap(self):
        self.lbl.text = "It’s a real app."

class DemoApp(App):
    def build(self):
        return Root()

if __name__ == "__main__":
    DemoApp().run()
