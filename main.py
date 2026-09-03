from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
class Myapp(App):
    def build(self):
        layout=BoxLayout(orientation="vertical")
        self.label=Label(text="Hello")
        button=Button(text="press")
        button.bind(on_press=self.text)
    
        layout.add_widget(button)
        layout.add_widget(self.label)
        
        return layout
    def text(self,increment):
        self.label.text="world"
        
Myapp().run()