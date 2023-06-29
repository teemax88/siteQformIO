from pom.QuizPage.builder import QuizPage
from variables import *
import pytest
import time


class TestCaseQuizPage:
    @pytest.mark.skip
    def test_of_page_navigation_menu(self, quiz_page):
        app = QuizPage(driver=quiz_page)
        """ Проверяем меню навигации """
        app.other_page_navigation_menu(page_url=QUIZPAGE, text_logo=quiz)

    @pytest.mark.skip
    def test_demo_button(self, quiz_page):
        app = QuizPage(driver=quiz_page)
        """ Проверяем кнопку Демо """
        # app.demo_button(QUIZPAGE)
        app.find_by("xpath", app.element.demo_button).click()

        # Проверяем URL
        assert app.driver.current_url == f'{QUIZPAGE}/demo', f"Адрес страницы не соответствует {QUIZPAGE}/demo"

    @pytest.mark.skip
    def test_of_start_button(self, quiz_page):
        app = QuizPage(driver=quiz_page)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, quiz_page):
        app = QuizPage(driver=quiz_page)
        """ Проверяем кнопку по услуге создания форм"""
        # app.offer_creation()
        button_for_offer = app.find_by("xpath", app.element.button_for_offer)
        app.action.move_to_element(button_for_offer).click(button_for_offer).perform()
        time.sleep(2)

        assert app.driver.current_url == SERVICE, f"Адрес страницы не соответствует {app.driver.current_url}"

    @pytest.mark.skip
    def test_check_footer(self, quiz_page):
        app = QuizPage(driver=quiz_page)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, quiz_page):
        app = QuizPage(driver=quiz_page)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider(QUIZPAGE)
        """ Проверяем слайдер с примерами """
        app.check_slider()


# **********************************************************************************

"""Страница Возможности"""


class TestCaseQuizFeaturesPage:
    @pytest.mark.skip
    def test_of_top_and_navigation_menu(self, quiz_feature_page):
        app = QuizPage(driver=quiz_feature_page)
        """ Проверяем меню навигации Конструктор форм """
        app.other_page_navigation_menu(page_url=f'{QUIZPAGE}/features', text_logo=quiz)

    @pytest.mark.skip
    def test_demo_button(self, quiz_feature_page):
        app = QuizPage(driver=quiz_feature_page)
        """ Проверяем кнопку Демо """
        # app.demo_button(QUIZPAGE)
        app.find_by("xpath", app.element.demo_button).click()

        # Проверяем URL
        assert app.driver.current_url == f'{QUIZPAGE}/demo', f"Адрес страницы не соответствует {QUIZPAGE}/demo"

    @pytest.mark.skip
    def test_of_start_button(self, quiz_feature_page):
        app = QuizPage(driver=quiz_feature_page)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, quiz_feature_page):
        app = QuizPage(driver=quiz_feature_page)
        """ Проверяем кнопку по услуге создания форм"""
        # app.offer_creation()
        button_for_offer = app.find_by("xpath", app.element.button_for_offer)
        app.action.move_to_element(button_for_offer).click(button_for_offer).perform()
        time.sleep(2)

        assert app.driver.current_url == SERVICE, f"Адрес страницы не соответствует {app.driver.current_url}"

    @pytest.mark.skip
    def test_check_footer(self, quiz_feature_page):
        app = QuizPage(driver=quiz_feature_page)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, quiz_feature_page):
        app = QuizPage(driver=quiz_feature_page)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()
