import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle, Line
from kivy.graphics.instructions import InstructionGroup

class RestaurantMate(App):
    def build(self):
        controls = AnchorLayout(
            anchor_x='right',
            anchor_y='top',
        )
        box = BoxLayout(
            orientation='vertical'
        )

        service_rating_label = Label(
            text='On a scale of 1 to 5 how would you rate the service?',
            font_size=18,
        )
        service_rating = TextInput(
            font_size=18,
            size_hint_x=None,
            width=200
        )
        food_rating_label = Label(
            text='On a scale of 1 to 5 how would you rate the food?',
            font_size=18,
        )
        food_rating = TextInput(
            font_size=18,
            size_hint_x=None,
            width=200
        )
        food_cost_label = Label(
            text='On a scale of 1 to 5 how would you rate the food?',
            font_size=18,
        )
        food_cost = TextInput(
            font_size=18,
            size_hint_x=None,
            width=200
        )
        input_btn = Button(text='Calculate Tip', font_size=40, size_hint_x=None,
                          width=200, background_color=[0,1.7,0,1])

        controls.add_widget(box)
        box.add_widget(service_rating_label)
        box.add_widget(service_rating)
        box.add_widget(food_rating_label)
        box.add_widget(food_rating)
        box.add_widget(food_cost_label)
        box.add_widget(food_cost)
        box.add_widget(input_btn)

        return controls

if __name__ == '__main__':
    RestaurantMate().run()
