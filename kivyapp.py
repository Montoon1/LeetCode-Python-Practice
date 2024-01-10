from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')
import api_test

class LeetApp(App):

    def build(self):
        random_button = Button(text= 'Get Random Question', font_size= 14)
        random_button.bind(on_press = self.firstrun)
        title_button = Button(text= "Current Title", font_size= 14)
        title_button.bind(on_press = self.title_name)
        difficulty_button = Button(text= "Current Difficulty", font_size= 14)
        difficulty_button.bind(on_press = self.difficulty)
        content_button = Button(text= "Current Content", font_size= 14)
        content_button.bind(on_press = self.content)
        app_main = BoxLayout(spacing=10, padding=5, orientation='horizontal')
        app_main.add_widget(Label(text="Random Question", font_size = 24))
        app_main.add_widget(random_button)
        app_main.add_widget(title_button)
        app_main.add_widget(difficulty_button)
        app_main.add_widget(content_button)
        return app_main

    def firstrun(self, event):
        total = api_test.get_total()
        random_int = api_test.set_random_int(total)
        self.current_title, self.current_difficulty, self.current_content = api_test.get_random_question(random_int)

    def title_name(self, event):
        print(self.current_title)

    def difficulty(self, event):
        print(self.current_difficulty)

    def content(self, event):
        print(self.current_content)

if __name__ == '__main__':
    LeetApp().run()