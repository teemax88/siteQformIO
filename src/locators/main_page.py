class MainPage:
    def __init__(self, driver):
        self.driver = driver

    """Header и навигация главной страницы"""

    @property
    # Заголовок страниц
    def title(self) -> str:
        return "//h1"

    @property
    # Главный логотип страницы
    def official_logo(self) -> str:
        return "//a[@class='link-active']"

    @property
    # Кнопка Вход
    def signin_button(self) -> str:
        return "//div[contains(@class, 'text-right')]/a[contains(text(), 'Вход')]"

    @property
    # Кнопка Регистрация
    def register_button(self) -> str:
        return "//div[contains(@class, 'text-right')]/a[contains(text(), 'Регистрация')]"

    @property
    # Список сервисов
    def services_list(self) -> str:
        return "//div[@class='services-list']"

    @property
    # Кнопка Все сервисы
    def services_button(self) -> str:
        return "//div[@class='services']/button"

    @property
    # Логотип QForm в меню Все сервисы
    def services_qform_logo(self) -> str:
        return "//div[@class='services-list']//a[@class='link-active']/img"

    @property
    # Блок с другими сервисами в меню Все сервисы
    def block_with_other_services(self) -> str:
        return "//ul[@class='list-desctop']"

    @property
    # Лого в меню
    def logo_in_menu(self) -> str:
        return "//div[contains(@class, 'page-navigation')]//button[contains(@class, 'page-logo')]//span"

    @property
    # Текст лого в меню
    def logo_name_in_menu(self) -> str:
        return "//button[contains(@class, 'page-logo')]//span"

    @property
    # Разделы функции в меню
    def navigation_item_titles(self) -> str:
        return "//ul[contains(@class, 'nav')]//li[@class='nav-item']/a"

    @property
    # Блок функции в меню
    def menu_list(self) -> str:
        return "//div[contains(@class, 'open-menu')]"

    @property
    # Блок функции в меню
    def menu_list_items(self) -> str:
        return "//div[contains(@class, 'nav-dropdown')]/ul//li[@class='nav-item__link']/a"

    @property
    # Элемент, чтобы закрыть-открыть меню
    def icon_to_close_or_open_menu(self) -> str:
        return "//button[contains(@class, 'nav-item__link')]/span"

    def page_link_on_navigation_menu(self, name_page: str) -> str:
        """Ссылка на раздел в меню навигации (нужно передать название страницы из variables)"""
        return f"//li[@class='nav-item']/a[contains(text(), '{name_page}')]"

    @property
    # Кнопка Демо
    def demo_button(self) -> str:
        return "//ul[contains(@class, 'nav')]//following::div/a[contains(text(), 'Демо')]"

    @property
    # Кнопка Примеры
    def examples_button(self) -> str:
        return "//div[contains(@class, 'hero-actions')]//a[contains(text(), 'Примеры')]"

    @property
    # Кнопка Начать
    def start_button(self) -> str:
        return "//div[contains(@class, 'hero-actions')]//a[contains(text(), 'Начать')]"

    """Секция с гиф инструкцией по созданию формы"""

    @property
    # Блок с гиф инструкцией по созданию формы
    def gif_block_for_insert_form(self) -> str:
        return "//div[contains(@class, 'insert-form')]//div[contains(@class, 'complete-solutions__body')]"

    @property
    # Видеоплеер
    def video_player(self) -> str:
        return "//div[@class='video']/video[@class='video__player']"

    @property
    # Активный элемент меню плеера
    def active_player_menu_item(self) -> str:
        return "//div[@class='insert-form__menu']//div[contains(@class, 'menu-item-active')]/p"

    @property
    # Неактивные элементы меню плеера
    def inactive_player_menu_items(self) -> str:
        return "//div[@class='insert-form__menu']//div[@class='insert-form__menu-item']/p"

    """Блок с карточками сервисов"""

    @property
    # Блок с карточками сервисов
    def block_with_service_cards(self) -> str:
        return "//div[contains(@class, 'parts__list')]"

    @property
    # Список кнопок Подробнее у карточек сервисов
    def button_for_service_cards(self) -> str:
        return "//div[contains(@class, 'system-part__bottom')]//a"

    @property
    # Список кнопок Подробнее у карточек сервисов
    def service_cards(self) -> str:
        return "//div[@class='system-part__top']"

    @property
    # Заголовки у карточек сервисов
    def service_cards_title(self) -> str:
        return "//div[@class='system-part__top']/h3"

    """Блок с предложением услуги по созданию форм"""

    @property
    # Кнопка Подробнее на баннере с предложением услуги по созданию форм
    def button_for_offer(self) -> str:
        return "//div[@class='cat-banner__body']//a"

    """Секция Слайдер с примерами"""

    @property
    # Секция с примерами
    def examples_section(self) -> str:
        return "//div[@id='examples']"

    @property
    # Видимые изображения в слайдере
    def visible_images(self) -> str:
        return "//ul[@class='splide__list']//li[contains(@class, 'is-visible')]/img"

    @property
    # Кнопка для следующего слайда
    def button_next_slide(self) -> str:
        return "//button[contains(@class, 'splide-next')]"

    @property
    # Слайд
    def slide_list(self) -> str:
        return "//ul[@class='splide__list']//li[contains(@class, 'is-visible')]"

    """Footer страницы"""

    @property
    # Блок Footer
    def footer(self) -> str:
        return "//footer[contains(@class, 'footer')]"

    @property
    # Логотип в блоке Footer
    def footer_logo(self) -> str:
        return "//footer//div[@class='logo-img']/img"

    @property
    # Список сервисов в блоке Footer
    def footer_service_list(self) -> str:
        return "//footer//div[@class='footer-services__list-wrapper']//a"

    @property
    # Соцсети в блоке Footer
    def footer_social_list(self) -> str:
        return "//footer//div[@class='socials']//a"

    @property
    # Список ссылок авторских прав в блоке Footer
    def footer_license_agreements(self) -> str:
        return "//div[@class='copyright']//span[@class='copyright__item']/a"
        # return "//div[@class='copyright']//span[@class='copyright__item']/a[contains(text(), 'договор')]"

    # *********************************************************************************************

    """Элементы сервиса app.qform"""

    @property
    # Loader
    def videowidget_loader(self) -> str:
        return "//div[@class='qform_backdrop']"

    @property
    # Форма авторизации QForm
    def qfrom_auth_body(self) -> str:
        return "//div[@class='auth-body']"

    @property
    # Заголовок формы авторизации QForm
    def qfrom_auth_title(self) -> str:
        return "//div[@class='title']"

    @property
    # Страница справочной системы
    def qfrom_reference_system(self) -> str:
        return "//div[@class='logo-main']//span[@class='reference']"

    # *********************************************************************************************

    """Общие элементы страниц Конструктор форм, Конструктор квизов и Видеовиджет"""

    @property
    # Ссылка Функции в верхней панели
    def link_functions_in_top_panel(self) -> str:
        return "//nav/a[@class='link-active']"

    @property
    # Активная кнопка в панели навигации
    def active_link_on_navigation(self) -> str:
        return "//li[contains(@class, 'nav-item')]/a[contains(@class, 'link-active')]"

    # *********************************************************************************************

    """Страница QForm.Link"""

    @property
    # Заголовок страницы
    def qlink_page_title(self) -> str:
        return "//div[@class='page-title']"

    @property
    # Логотип страницы
    def qlink_footer_logo(self) -> str:
        return "//a[@class='logo']"

    # *********************************************************************************************

    """Страница Demo"""

    @property
    # Активная кнопка по умолчанию при переходе на страницу
    def active_link(self) -> str:
        return "//div[contains(@class, 'hero-actions')]//a[contains(@class, 'link-active')]"
