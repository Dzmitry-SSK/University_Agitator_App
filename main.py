from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen



class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class AddUserScreen(MDScreen):
    pass

class UsersScreen(MDScreen):
    pass

class TestsScreen(MDScreen):
    pass

class AddTestScreen(MDScreen):
    pass

class AddCampaignScreen(MDScreen):
    pass

class CampaignsScreen(MDScreen):
    pass

class AboutUniversityScreen(MDScreen):
    pass

class AboutFacultyScreen(MDScreen):
    pass

class AdminScreen(MDScreen):
    pass

class ContentNavigationDrawer(MDScreen):
    pass

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        return Builder.load_file('app_style.kv')

if __name__ == '__main__':
    Example().run()


