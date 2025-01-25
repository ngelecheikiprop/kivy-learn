'learning how to use boxes and buttons'
import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        #class grid layout contructor
        super(MyGridLayout, self).__init__(**kwargs)

        #set columns 
        self.cols = 2

        #addd widgets
        self.add_widget(Label(text='Name: '))

        #add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__=='__main__':
    MyApp().run()
