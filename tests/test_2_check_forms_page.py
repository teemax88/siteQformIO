from pom.FormsPage.builder import FormsPage
from variables import *
import pytest
import time


@pytest.mark.usefixtures("forms_page")
class TestCaseFormsPage:
    @pytest.mark.skip
    def test_of_page_navigation_menu(self):
        app = FormsPage(self.driver)
        """ Проверяем меню навигации """
        app.other_page_navigation_menu(page_url=FORMPAGE)

    @pytest.mark.skip
    def test_demo_button(self):
        app = FormsPage(self.driver)
        """ Проверяем кнопку Демо """
        # app.demo_button(page_url=FORMPAGE)
        app.find_by("xpath", app.element.demo_button).click()
        time.sleep(3)

        # Проверяем URL
        assert app.driver.current_url == f'{FORMPAGE}/demo', f"Адрес страницы не соответствует {FORMPAGE}/demo"

        app.fin(FORMPAGE)

    @pytest.mark.skip
    def test_of_start_button(self):
        app = FormsPage(self.driver)
        """ Проверяем кнопку Начать """
        app.start_button()

        app.fin(FORMPAGE)

    @pytest.mark.skip
    def test_offer_creation(self):
        app = FormsPage(self.driver)
        """ Проверяем кнопку по услуге создания форм"""
        # app.offer_creation()
        button_for_offer = app.find_by("xpath", app.element.button_for_offer)
        app.action.move_to_element(button_for_offer).click(button_for_offer).perform()
        time.sleep(2)

        assert app.driver.current_url == SERVICE, f"Адрес страницы не соответствует {app.driver.current_url}"

        app.fin(FORMPAGE)

    @pytest.mark.skip
    def test_check_footer(self):
        app = FormsPage(self.driver)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

        app.fin(FORMPAGE)

    @pytest.mark.skip
    def test_checking_form_page_elements(self):
        app = FormsPage(self.driver)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()
        """ Проверяем кнопку по услуге создания форм"""
        app.interactive_slider()


# **********************************************************************************

"""Страница Возможности"""


@pytest.mark.usefixtures("forms_feature_page")
class TestCaseFormsFeaturesPage:
    @pytest.mark.skip
    def test_of_page_navigation_menu(self):
        app = FormsPage(self.driver)
        """ Проверяем меню навигации Конструктор форм """
        app.other_page_navigation_menu(page_url=f'{FORMPAGE}/features')

        app.fin(f'{FORMPAGE}/features')

    @pytest.mark.skip
    def test_demo_button(self):
        app = FormsPage(self.driver)
        """ Проверяем кнопку Демо """
        # app.demo_button(page_url=FORMPAGE)
        app.find_by("xpath", app.element.demo_button).click()
        time.sleep(2)

        # Проверяем URL
        assert app.driver.current_url == f'{FORMPAGE}/demo', f"Адрес страницы не соответствует {FORMPAGE}/demo"

        app.fin(f'{FORMPAGE}/features')

    @pytest.mark.skip
    def test_of_start_button(self):
        app = FormsPage(self.driver)
        """ Проверяем кнопку Начать """
        app.start_button()

        app.fin(f'{FORMPAGE}/features')

    @pytest.mark.skip
    def test_offer_creation(self):
        app = FormsPage(self.driver)
        """ Проверяем кнопку по услуге создания форм"""
        # app.offer_creation()
        button_for_offer = app.find_by("xpath", app.element.button_for_offer)
        app.action.move_to_element(button_for_offer).click(button_for_offer).perform()
        time.sleep(2)

        assert app.driver.current_url == SERVICE, f"Адрес страницы не соответствует {app.driver.current_url}"

        app.fin(f'{FORMPAGE}/features')

    @pytest.mark.skip
    def test_check_footer(self):
        app = FormsPage(self.driver)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

        app.fin(f'{FORMPAGE}/features')

    @pytest.mark.skip
    def test_checking_form_page_elements(self):
        app = FormsPage(self.driver)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()

        app.fin(f'{FORMPAGE}/features')


# **********************************************************************************

"""Страница Виды"""


@pytest.mark.usefixtures("forms_page")
class TestCaseViews:
    @pytest.mark.skip
    def test_of_views_dropdown(self):
        app = FormsPage(self.driver)
        """ Проверяем Виды в выпадающем списке """
        app.check_views_dropdown(1, 1)
        """ Проверяем Шаблоны в выпадающем списке """
        app.check_views_dropdown(1, 2)

    @pytest.mark.skip
    def test_of_views_page(self, forms_page):
        app = FormsPage(driver=forms_page)
        """ Проверяем страницу Виды """
        app.check_views_page()

