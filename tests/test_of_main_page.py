from pom.MainPage.builder import MainPage
from variables import *
import pytest


class TestCaseMainPage:
    @pytest.mark.skip
    def test_of_top_and_navigation_menu(self, browser):
        app = MainPage(browser)
        """ Проверяем верхнее меню главной страницы """
        assert browser.current_url == URL, f"Страница не соответствует адресу {URL}"
        app.top_menu()
        """ Проверяем меню навигации главной страницы """
        app.main_page_navigation_menu()

    def test_demo_button(self, browser):
        app = MainPage(browser)
        """ Проверяем кнопку Демо """
        app.demo_button(FORMPAGE)
        app.main_page_navigation_menu()

    def test_of_start_button(self, browser):
        app = MainPage(browser)
        """ Проверяем кнопку Начать """
        app.start_button()

    def test_service_cards(self, browser):
        app = MainPage(browser)
        """ Проверяем карточки с сервисами"""
        app.service_cards()

    def test_offer_creation(self, browser):
        app = MainPage(browser)
        """ Проверяем кнопку по услуге создания форм"""
        app.offer_creation()

    def test_check_footer(self, browser):
        app = MainPage(browser)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    def test_checking_main_page_elements(self, browser):
        app = MainPage(browser)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()
        """ Проверяем блок с гиф инструкцией по созданию формы """
        app.gif_for_insert_form()

    # *********************************************

    @pytest.mark.skip
    def test_quiz_constructor_button(self, browser):
        app = MainPage(browser)
        """ Проверяем кнопку Конструктор квизов """
        app.quiz_constructor_button(QUIZPAGE)

    @pytest.mark.skip
    def test_videowidget_button(self, browser):
        app = MainPage(browser)
        """ Проверяем кнопку Видеовиджет """
        app.videowidget_button(VIDEOPAGE)

    @pytest.mark.skip
    def test_qlink_button(self, browser):
        app = MainPage(browser)
        """ Проверяем кнопку Qlink """
        app.qlink_button()
