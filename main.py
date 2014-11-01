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
from kivy.uix.popup import Popup

class RestaurantMate(App):
    def build(self):
        global starting_tip
        starting_tip = 10

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
        input_btn = Button(
            text='Calculate Tip',
            font_size=20,
            size_hint_x=None,
            width=200,
            background_color=[0,1.7,0,1]
        )

        def adjust_tip(rating):
            global starting_tip
            if rating == 1:
                starting_tip = starting_tip - 5
            elif rating == 2:
                starting_tip = starting_tip - 2.5
            elif rating == 3:
                starting_tip = starting_tip + 2.5
            elif rating == 4:
                starting_tip = starting_tip + 3.5
            else:
                starting_tip = starting_tip + 5
            return starting_tip

        def calculate_tip(instance):
            service_rating_value = float(service_rating.text)
            food_rating_value = float(food_rating.text)
            adjust_tip(service_rating_value)
            adjust_tip(food_rating_value)

            # starting_tip = float(starting_tip)
            meal_cost = float(food_cost.text)
            tip = meal_cost * (starting_tip/100)
            popup = Popup(
                title='Suggested Tip',
                content=Label(
                    text='Your suggested tip is\n ' + str(starting_tip) + '%\n' + 'Which is $' + str(tip),
                    multiline=True,
                ),
                # content="Your suggested tip percentage is:",
                auto_dismiss=False,
            )
            popup.open()
            print('The button <%s> is being pressed' % instance.text)

        input_btn.bind(on_press=calculate_tip)

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
