from pom.FormsPage.builder import FormsPage
from variables import *
import pytest


class TestCaseFormsPage:
    @pytest.mark.skip
    def test_of_page_navigation_menu(self, forms_page):
        app = FormsPage(driver=forms_page)
        """ Проверяем меню навигации Конструктор форм """
        app.other_page_navigation_menu(page_url=FORMPAGE, text_logo=forms)

    @pytest.mark.skip
    def test_demo_button(self, forms_page):
        app = FormsPage(driver=forms_page)
        """ Проверяем кнопку Демо """
        app.demo_button(page_url=FORMPAGE)

    @pytest.mark.skip
    def test_of_start_button(self, forms_page):
        app = FormsPage(driver=forms_page)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, forms_page):
        app = FormsPage(driver=forms_page)
        """ Проверяем кнопку по услуге создания форм"""
        app.offer_creation()

    @pytest.mark.skip
    def test_check_footer(self, forms_page):
        app = FormsPage(driver=forms_page)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, forms_page):
        app = FormsPage(driver=forms_page)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()
        """ Проверяем кнопку по услуге создания форм"""
        app.interactive_slider()


# **********************************************************************************

"""Страница Возможности"""


class TestCaseFormsFeaturesPage:
    @pytest.mark.skip
    def test_of_page_navigation_menu(self, forms_feature_page):
        app = FormsPage(driver=forms_feature_page)
        """ Проверяем меню навигации Конструктор форм """
        app.other_page_navigation_menu(page_url=f'{FORMPAGE}/features', text_logo=forms)

    @pytest.mark.skip
    def test_demo_button(self, forms_feature_page):
        app = FormsPage(driver=forms_feature_page)
        """ Проверяем кнопку Демо """
        app.demo_button(page_url=FORMPAGE)

    @pytest.mark.skip
    def test_of_start_button(self, forms_feature_page):
        app = FormsPage(driver=forms_feature_page)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, forms_feature_page):
        app = FormsPage(driver=forms_feature_page)
        """ Проверяем кнопку по услуге создания форм"""
        app.offer_creation()

    @pytest.mark.skip
    def test_check_footer(self, forms_feature_page):
        app = FormsPage(driver=forms_feature_page)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, forms_feature_page):
        app = FormsPage(driver=forms_feature_page)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()
