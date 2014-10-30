import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class GetUserInput(GridLayout):
    def __init__(self, **kwargs):
        super(GetUserInput, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class RestaurantExplorer(App):
    def build(self):
        return GetUserInput()


if __name__ == '__main__':
    RestaurantExplorer().run()
