class FormsPage:

    """Панель навигации"""

    @property
    # Выпадающая панель Виды со списков видов и шаблонов форм в навигации
    def nav_views_dropdown_panel(self) -> str:
        return "//div[@class='nav-item-dropdown']/div[contains(@class, 'content')]"

    @property
    # Выпадающий список Виды в навигации
    def views_dropdown(self) -> str:
        return "//ul[contains(@class, 'nav')]//li[contains(@class, 'dropdown')]"

    # Список видов
    def nav_views_item(self, section: int, item: int) -> str:
        return f"//div[@class='nav-item-dropdown']/div[contains(@class, 'content')]/div[{section}]//li[{item}]/a"

    @property
    # Ссылка Смотреть все
    def see_all_link_on_form_views(self) -> str:
        return "//div[@id='nav_Виды']//a[@class='link-more']"

    @property
    # Ссылка Смотреть все
    def see_all_link_on_form_templates(self) -> str:
        return "//div[@id='nav_Шаблоны']//a[@class='link-more']"



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
