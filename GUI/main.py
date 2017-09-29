from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.config import Config
Config.set('graphics','resizable',0)

from kivy.uix.behaviors import ButtonBehavior

from kivy.core.window import Window
Window.size = (300, 500)

from registro import Registro

class Login(Screen):

    def do_login(self):

        app = App.get_running_app()

        self.manager.transition = SlideTransition(direction="up")
        self.manager.current = 'registro'

        app.config.read(app.get_application_config())

        app.config.write()




    def resetForm(self):

        self.ids['login'].text = ""

        self.ids['password'].text = ""



class LoginApp(App):

    username = StringProperty(None)

    password = StringProperty(None)



    def build(self):

        manager = ScreenManager()



        manager.add_widget(Login(name='login'))

        manager.add_widget(Registro(name='registro'))



        return manager



    def get_application_config(self):

        if(not self.username):

            return super(LoginApp, self).get_application_config()



        conf_directory = self.user_data_dir + '/' + self.username



        if(not os.path.exists(conf_directory)):

            os.makedirs(conf_directory)



        return super(LoginApp, self).get_application_config(

            '%s/config.cfg' % (conf_directory)

        )



if __name__ == '__main__':

    LoginApp().run()