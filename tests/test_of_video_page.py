from pom.VideoPage.builder import VideoPage
from variables import *
import pytest


class TestCaseVideoPage:
    @pytest.mark.skip
    def test_of_top_and_navigation_menu(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор квизов """
        app.go_to_page(video)
        """ Проверяем верхнее меню Конструктор форм """
        assert browser.current_url == VIDEOPAGE, f"Страница не соответствует адресу {VIDEOPAGE}"
        app.top_menu()
        """ Проверяем меню навигации Конструктор форм """
        app.other_navigation_menu(VIDEOPAGE, video)

    @pytest.mark.skip
    def test_demo_button(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video)
        """ Проверяем кнопку Демо """
        app.demo_button(VIDEOPAGE)

    @pytest.mark.skip
    def test_of_start_button(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video)
        """ Проверяем кнопку по услуге создания форм"""
        app.offer_creation()

    @pytest.mark.skip
    def test_check_footer(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()


    @pytest.mark.skip
    def test_checking_form_page_elements(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video)
        # """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        # app.examples_button_for_scroll_to_slider()
        # """ Проверяем слайдер с примерами """
        # app.video_check_slider()
        # """ Проверяем миниатюру и блок с видами отображения """
        app.visibility_and_types_videos_on_page()


# **********************************************************************************

"""Страница Возможности"""


class TestCaseVideoFeaturesPage:
    @pytest.mark.skip
    def test_of_top_and_navigation_menu(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video, features)
        """ Проверяем верхнее меню Конструктор форм """
        assert browser.current_url == VIDEOPAGE, f"Страница не соответствует адресу {VIDEOPAGE}"
        app.top_menu()
        """ Проверяем меню навигации Конструктор форм """
        app.other_navigation_menu(VIDEOPAGE, video)

    @pytest.mark.skip
    def test_demo_button(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video, features)
        """ Проверяем кнопку Демо """
        app.demo_button(VIDEOPAGE)

    @pytest.mark.skip
    def test_of_start_button(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video, features)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video, features)
        """ Проверяем кнопку по услуге создания форм"""
        app.offer_creation()

    @pytest.mark.skip
    def test_check_footer(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video, features)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, browser):
        app = VideoPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(video, features)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()