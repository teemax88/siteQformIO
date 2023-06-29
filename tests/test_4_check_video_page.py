from pom.VideoPage.builder import VideoPage
from variables import *
import pytest
import time


class TestCaseVideoPage:
    @pytest.mark.skip
    def test_of_page_navigation_menu(self, video_page):
        app = VideoPage(driver=video_page)
        """ Проверяем меню навигации """
        app.other_page_navigation_menu(page_url=VIDEOPAGE, text_logo=video)

    @pytest.mark.skip
    def test_demo_button(self, video_page):
        app = VideoPage(driver=video_page)
        """ Проверяем кнопку Демо """
        # app.demo_button(VIDEOPAGE)
        app.find_by("xpath", app.element.demo_button).click()

        # Проверяем URL
        assert app.driver.current_url == f'{VIDEOPAGE}/demo', f"Адрес страницы не соответствует {VIDEOPAGE}/demo"

    @pytest.mark.skip
    def test_of_start_button(self, video_page):
        app = VideoPage(driver=video_page)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, video_page):
        app = VideoPage(driver=video_page)
        """ Проверяем кнопку по услуге создания форм"""
        # app.offer_creation()
        button_for_offer = app.find_by("xpath", app.element.button_for_offer)
        app.action.move_to_element(button_for_offer).click(button_for_offer).perform()
        time.sleep(2)

        assert app.driver.current_url == SERVICE, f"Адрес страницы не соответствует {app.driver.current_url}"

    @pytest.mark.skip
    def test_check_footer(self, video_page):
        app = VideoPage(driver=video_page)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, video_page):
        app = VideoPage(driver=video_page)
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
    def test_of_top_and_navigation_menu(self, video_feature_page):
        app = VideoPage(driver=video_feature_page)
        """ Проверяем меню навигации Конструктор форм """
        app.other_page_navigation_menu(page_url=f'{VIDEOPAGE}/features', text_logo=video)

    @pytest.mark.skip
    def test_demo_button(self, video_feature_page):
        app = VideoPage(driver=video_feature_page)
        """ Проверяем кнопку Демо """
        # app.demo_button(VIDEOPAGE)
        app.find_by("xpath", app.element.demo_button).click()

        # Проверяем URL
        assert app.driver.current_url == f'{VIDEOPAGE}/demo', f"Адрес страницы не соответствует {VIDEOPAGE}/demo"

    @pytest.mark.skip
    def test_of_start_button(self, video_feature_page):
        app = VideoPage(driver=video_feature_page)
        """ Проверяем кнопку Начать """
        app.start_button()

    @pytest.mark.skip
    def test_offer_creation(self, video_feature_page):
        app = VideoPage(driver=video_feature_page)
        """ Проверяем кнопку по услуге создания форм"""
        # app.offer_creation()
        button_for_offer = app.find_by("xpath", app.element.button_for_offer)
        app.action.move_to_element(button_for_offer).click(button_for_offer).perform()
        time.sleep(2)

        assert app.driver.current_url == SERVICE, f"Адрес страницы не соответствует {app.driver.current_url}"

    @pytest.mark.skip
    def test_check_footer(self, video_feature_page):
        app = VideoPage(driver=video_feature_page)
        """ Проверяем соцсети в футере"""
        app.footer()
        """ Проверяем соцсети в футере"""
        app.footer_social_icons()
        """ Проверяем авторские права в футере"""
        app.footer_copyright()

    @pytest.mark.skip
    def test_checking_form_page_elements(self, video_feature_page):
        app = VideoPage(driver=video_feature_page)
        """ Проверяем кнопку Примеры и скролл до слайдера с примерами """
        app.examples_button_for_scroll_to_slider(VIDEOPAGE)
        """ Проверяем слайдер с примерами """
        app.check_slider()
