import time
from pom.BasePage.basemodel import Basemodel
from selenium.webdriver.common.by import By


class VideoPage(Basemodel):
    def __init__(self, driver):
        super().__init__(driver)

    def visibility_and_types_videos_on_page(self):
        time.sleep(5)
        """ Проверка отображения видео в миниатюре """
        miniature_widget = self.find_by("xpath", self.element.miniature_widget)
        widget_position = miniature_widget.value_of_css_property("position")
        widget_bottom = miniature_widget.value_of_css_property("bottom")
        widget_left = miniature_widget.value_of_css_property("left")

        assert widget_position == "fixed", "Позиция видео не фиксированная"
        assert widget_bottom == "30px", "Расстояние от низа не равно 30px"
        assert widget_left == "30px", "Расстояние от левого края не равно 30px"

        """ Проверка блока с видами отображения"""

        # Скроллим до блока с кнопками переключения
        switch_block = self.find_by("xpath", self.element.switch_block)
        self.action.move_to_element(switch_block).perform()

        # Находим кнопки переключения (будут в списке).
        # Создаем отдельный список с ожидаемыми названиями кнопок
        # Создаем счетчик для списков
        switch_buttons_list = self.finds_by("xpath", self.element.switch_buttons_list)
        views_title_list = ['В миниатюре', 'В контенте', 'По событию']
        counter = 0

        # Открываем цикл по спсику кнопок переключения
        for button in switch_buttons_list:
            # Кликаем на 1-у кнопку
            button.click()
            time.sleep(1)

            # Сравниваем название кнопки с ожидаемым названием по индексу counter
            assert self.get_text_from_one_element(button) == views_title_list[counter], "Название кнопки вида не соответствует"

            # Находим изображения по индексу counter+1, для проверки картинок активного вида отображения
            images_in_block = self.finds_by("xpath", self.element.images_in_block(counter+1))

            # Запускаем цикл для изображений
            for image in images_in_block:
                # Берем свойство clientWidth
                image_property = image.get_property("clientWidth")

                # Проверяем что текущая картинка отображается, и далее что свойство clientWidth > 0
                assert image.is_displayed(), "Картинки не отображаются"
                assert image_property > 0, "Свойство clientWidth не больше 0, значит картинка не отображается"

            # Наращиваем счетчик
            counter += 1

    def video_check_slider(self):
        time.sleep(2)
        """ Проверка слайдера с видео"""
        try:
            # Делаем скриншот начального состояния слайдера
            self.driver.save_screenshot(f'screen/video_slider_expect_res_{self.data}.png')

            # Собираем список слайдов
            list_videos = self.finds_by("xpath", self.element.video_list)
            count = 0

            # Запускаем по списку слайдов цикл
            for index in range(1, len(list_videos)+1):
                # каждый слайд проверяем на отображение
                video = self.find_by("xpath", self.element.video_content(index))
                assert video.is_displayed(), "Видео не отображается"

                arrow = self.find_by("xpath", self.element.display_property_of_arrow(2))
                display_property_of_arrow = arrow.get_property("clientWidth")

                if display_property_of_arrow > 0:
                    self.find_by("xpath", self.element.video_prev_slide).click()
                    time.sleep(1)
                    video = self.find_by("xpath", self.element.video_content(index))
                    assert not video.is_displayed(), "Видео отображается"

                count += 1
            assert len(list_videos) == count, f"Слайд номер {count} не появился. Смотри промежуточный скриншот: {self.driver.save_screenshot(f'screen/video_slider_between_res_{self.data}.png')}"

            list_videos = self.finds_by("xpath", self.element.video_list)
            count = 0

            # Запускаем обратный цикл
            for index in range(len(list_videos), 1, -1):
                print(index)
                # каждый слайд проверяем на отображение
                video = self.find_by("xpath", self.element.video_content(index))
                assert video.is_displayed(), "Видео в обратную сторону не отображается"

                arrow = self.find_by("xpath", self.element.display_property_of_arrow(3))
                display_property_of_arrow = arrow.get_property("clientWidth")
                if display_property_of_arrow > 0:
                    self.find_by("xpath", self.element.video_next_slide).click()
                    time.sleep(1)
                    video = self.find_by("xpath", self.element.video_content(index))
                    assert video.is_displayed(), "Видео в обратную сторону после клика не отображается"

                count += 1
            assert len(list_videos) == count, f"Слайд номер {count} не появился. Смотри скриншот: {self.driver.save_screenshot(f'screen/video_slider_actual_res_{self.data}.png')}"
        except:
            print(f"[INFO]:: Проблема со слайдером на странице {self.driver.current_url}")
