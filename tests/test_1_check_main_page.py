from pom.MainPage.builder import MainPage
from variables import *
import pytest


@pytest.mark.usefixtures("browser")
class TestCaseMainPage:
    @pytest.mark.skip
    def test_of_top_and_navigation_menu(self):
        app = MainPage(self.driver)
        """ Проверяем верхнее меню главной страницы """
        assert app.driver.current_url == URL, f"Страница не соответствует адресу {URL}"
        app.top_menu()
        """ Проверяем меню навигации главной страницы """
        app.main_page_navigation_menu()

    @pytest.mark.skip
    def test_demo_button(self):
        app = MainPage(self.driver)
        """ Проверяем кнопку Демо """
        app.demo_button(FORMPAGE)
        app.main_page_navigation_menu()

        app.fin(URL)

    @pytest.mark.skip
    def test_of_start_button(self):
        app = MainPage(self.driver)
        """ Проверяем кнопку Начать """
        app.start_button()

        app.fin(URL)

    @pytest.mark.skip
    def test_service_cards(self):
        app = MainPage(self.driver)
        """ Проверяем карточки с сервисами"""
        app.service_cards()

    @pytest.mark.skip
    def test_offer_creation(self):
        app = MainPage(self.driver)
        """ Проверяем кнопку по услуге создания форм"""
        app.offer_creation()

        app.fin(URL)

    @pytest.mark.skip
    def test_check_footer(self):
        app = MainPage(self.driver)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

        app.fin(URL)

    @pytest.mark.skip
    def test_checking_main_page_elements(self):
        app = MainPage(self.driver)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider(URL)
        """ Проверяем слайдер с примерами """
        app.check_slider()
        """ Проверяем блок с гиф инструкцией по созданию формы """
        app.gif_for_insert_form()

