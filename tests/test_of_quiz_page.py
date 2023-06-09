from pom.QuizPage.builder import QuizPage
from variables import *
import pytest


class TestCaseQuizPage:
    @pytest.mark.skip
    def test_of_top_and_navigation_menu(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор квизов """
        app.go_to_page(quiz)
        """ Проверяем верхнее меню Конструктор форм """
        assert browser.current_url == QUIZPAGE, f"Страница не соответствует адресу {QUIZPAGE}"
        app.top_menu()
        """ Проверяем меню навигации Конструктор форм """
        app.other_navigation_menu(QUIZPAGE, quiz)

    @pytest.mark.skip
    def test_demo_button(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz)
        """ Проверяем кнопку Демо """
        app.demo_button(QUIZPAGE)

    @pytest.mark.skip
    def test_of_start_button(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz)
        """ Проверяем кнопку по услуге создания форм"""
        app.offer_creation()

    @pytest.mark.skip
    def test_check_footer(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()


# **********************************************************************************

"""Страница Возможности"""


class TestCaseQuizFeaturesPage:
    @pytest.mark.skip
    def test_of_top_and_navigation_menu(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz, features)
        """ Проверяем верхнее меню Конструктор форм """
        assert browser.current_url == QUIZPAGE, f"Страница не соответствует адресу {QUIZPAGE}"
        app.top_menu()
        """ Проверяем меню навигации Конструктор форм """
        app.other_navigation_menu(QUIZPAGE, quiz)

    @pytest.mark.skip
    def test_demo_button(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz, features)
        """ Проверяем кнопку Демо """
        app.demo_button(QUIZPAGE)

    @pytest.mark.skip
    def test_of_start_button(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz, features)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz, features)
        """ Проверяем кнопку по услуге создания форм"""
        app.offer_creation()

    @pytest.mark.skip
    def test_check_footer(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz, features)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, browser):
        app = QuizPage(browser)
        """ Идем на страницу Конструктор форм """
        app.go_to_page(quiz, features)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider()
        """ Проверяем слайдер с примерами """
        app.check_slider()