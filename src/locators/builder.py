from src.locators.main_page import MainPage
from src.locators.forms_page import FormsPage
from src.locators.video_page import VideoPage


class Elements(MainPage, FormsPage, VideoPage):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

        def __init__(self):
            super().__init__()
