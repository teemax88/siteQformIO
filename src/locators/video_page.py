class VideoPage:
    def __init__(self, driver):
        self.driver = driver

    """Блок Виды отображения"""

    @property
    # Видео в миниатюре
    def miniature_widget(self) -> str:
        return "//div[@class='qform__freewidgets-wrapper']"

    @property
    # Блок с кнопками переключения
    def switch_block(self) -> str:
        return "//section[@class='videowidget-switch']//div[@class='buttons']"

    @property
    # Список кнопок переключения
    def switch_buttons_list(self) -> str:
        return "//section[@class='videowidget-switch']//div[@class='buttons']/button"

    @property
    # Включеный вид отображения
    def actual_button_on(self) -> str:
        return "//section[@class='videowidget-switch']//div[@class='buttons']/button[contains(@class, 'button-on')]"

    # Картинки к виду отображения виджета
    def images_in_block(self, index) -> str:
        return f"//section[@class='videowidget-switch']//div[@class='slider']/div[{index}]//img"


    """Блок Видеослайдера"""

    @property
    # Список слайдов
    def video_list(self) -> str:
        return "//div[@class='swiper-wrapper']/div[contains(@class, 'swiper-slide')]"

    # Контент слайда
    def video_content(self, index) -> str:
        return f"//div[@class='swiper-wrapper']/div[contains(@class, 'swiper-slide')][{index}]//div[@class='views-box_content']"

    # Динамический блок для изменения стрелки слайдера
    def display_property_of_arrow(self, index) -> str:
        return f"//div[contains(@class, 'video-main-block')]/div[{index}]"

    @property
    # Кнопка для следующего слайда
    def video_prev_slide(self) -> str:
        return "//div[contains(@class, 'video-main-block')]//div[contains(@class, 'swiper-button-prev')]"

    @property
    # Кнопка для предыдущего слайда
    def video_next_slide(self) -> str:
        return "//div[contains(@class, 'video-main-block')]//div[contains(@class, 'swiper-button-next')]"
