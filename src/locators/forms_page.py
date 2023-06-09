class FormsPage:
    def __init__(self, driver):
        self.driver = driver

    """Панель навигации"""

    @property
    # Выпадающая панель Виды со списков видов и шаблонов форм в навигации
    def nav_views_dropdown_panel(self) -> str:
        return "//div[@class='nav-item-dropdown']/div[contains(@class, 'content')]"

    @property
    # Раздел Виды в навигации
    def views_item(self) -> str:
        return "//ul[contains(@class, 'nav')]//li[contains(@class, 'dropdown')]"

    @property
    # Список видов в навигации
    def nav_views_list_items(self) -> str:
        return "//div[contains(@class, 'content')]//ul[@class='list']//li[@class='list-item']"

    """ Интерактивный слайдер """

    @property
    # Большой слайд
    def big_slider(self) -> str:
        return "//div[@class='big-slider']"

    @property
    # Панель смены слайдов
    def slider_panel(self) -> str:
        return "//div[contains(@class, 'thumb-slider')]"

    @property
    # Список слайдов (для цикла)
    def slider_list(self) -> str:
        return "//div[@class='swiper-wrapper']//div[contains(@class, 'swiper-slide')]//img"

    @property
    # Список больших слайдов (для отображения)
    def big_slider_list(self) -> str:
        return "//div[@class='big-slider']//div[@class='big-slider__container']"

    @property
    # Стрелка Next у слайдера
    def next_btn_slider(self) -> str:
        return "//div[contains(@class, 'thumb-slider')]//div[@class='swiper-button-next']"

