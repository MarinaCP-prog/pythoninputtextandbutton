import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialise infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        # Set columns
        self.cols = 1
        
        # Create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        
        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        
        # Add widgets
        self.top_grid.add_widget(Label(text="Favourite Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)
        
        # Add widgets
        self.top_grid.add_widget(Label(text="Favourite Colour: "))
        # Add Input Box
        self.colour = TextInput(multiline=False)
        self.top_grid.add_widget(self.colour)
        
        # Add the new top_grid to our app
        self.add_widget(self.top_grid)
        
        # Create a third gridlayout
        self.thirdlayout = GridLayout()
        self.thirdlayout.cols = 2
        
        self.thirdlayout.add_widget(Label(text="Favorite Pet: "))
        self.pet = TextInput(multiline=False)
        self.thirdlayout.add_widget(self.pet)
        
        # Add the new thirdlayout to our app
        self.add_widget(self.thirdlayout)
        
        # Create a submit button
        self.submit = Button(text=" Submit", font_size=32)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        colour = self.colour.text
        pet = self.pet.text
        
        #print(f'Hello {name}, you like {pizza} pizza and your favorite colour is {colour}.') 
        # Print it to the screen
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza and your favorite colour is {colour}. Your favourite pet is a {pet}'))
        
        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.colour.text = ""
        self.pet.text = ""
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()   