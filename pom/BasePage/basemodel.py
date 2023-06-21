import time
from src.locators.builder import Elements
from src.utils.methods import BaseMethods
from selenium.webdriver.common.action_chains import ActionChains
from variables import *
from datetime import datetime


class Basemodel(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.element = Elements(self.driver)
        self.action = ActionChains(self.driver)
        self.data = datetime.strftime(datetime.now(), '%d-%m-%H-%M')

    def top_menu(self):
        """ Проверяем верхнее меню """
        all_services_btn = self.find_by("xpath", self.element.services_button)
        all_services_btn_text = self.get_text_from_one_element(all_services_btn)
        services_list = self.find_by("xpath", self.element.services_list)

        assert all_services_btn_text == "Все сервисы", "Надпись кнопки Все сервисы не соответствует"
        assert not services_list.is_displayed(), "Список сервисов отображается"

        # Клик по кнопке Все сервисы, открываеся меню сервисов
        all_services_btn.click()

        services_list = self.is_visible("xpath", self.element.services_list)
        other_services = self.find_by("xpath", self.element.block_with_other_services)
        services_qform_logo = self.find_and_get_attribute("xpath", self.element.services_qform_logo, "clientWidth")
        # services_qform_logo = self.find_by("xpath", self.element.services_qform_logo)
        # services_qform_logo_client_width = self.get_attribute_from_one_element("clientWidth", services_qform_logo)

        assert services_list.is_displayed(), "Список сервисов не отображается"
        assert other_services.is_displayed(), "Не отображается блок с другими сервисами в меню Все сервисы"
        assert services_qform_logo > "0", "Свойство clientWidth == 0, элемент не отображается"

        # Клик по кнопке Все сервисы, скрывается меню сервисов
        all_services_btn.click()

        """ Проверяем кнопку Вход """
        self.check_login_button()

        # Возвращаемся на сайт
        self.driver.back()

        """ Находим кнопку Регистрация, берем содержимое атрибута href, далее кликаем по кнопке """
        self.check_register_button()

        # Возвращаемся на сайт
        self.driver.back()

    def check_login_button(self):
        """ Находим кнопку Вход, берем содержимое атрибута href, далее кликаем по кнопке """
        self.find_by("xpath", self.element.signin_button).click()

        self.is_not_present("xpath", self.element.videowidget_loader)
        qfrom_auth_body = self.is_visible("xpath", self.element.qfrom_auth_body)
        qfrom_auth_title = self.is_visible("xpath", self.element.qfrom_auth_title)
        qfrom_auth_title_text = self.get_text_from_one_element(qfrom_auth_title).split("\n")[0]

        assert qfrom_auth_body.is_displayed(), "Не отображается форма авторизации Qform"
        assert qfrom_auth_title_text == "Войти в QForm", "Заголовок формы авторизации Qform не соответствует"
        assert self.driver.current_url == AUTHPAGE, f"Не перешли по адресу {AUTHPAGE}"

    def check_register_button(self):
        """ Находим кнопку Регистрация, берем содержимое атрибута href, далее кликаем по кнопке """
        self.find_by("xpath", self.element.register_button).click()

        # Вызываем функцию проверки страницы Регистрации QForm
        self.qform_register_page()

    def qform_register_page(self):
        self.is_not_present("xpath", self.element.videowidget_loader)
        qfrom_register_body = self.is_visible("xpath", self.element.qfrom_auth_body)
        qfrom_register_title = self.is_visible("xpath", self.element.qfrom_auth_title)
        qfrom_register_title_text = self.get_text_from_one_element(qfrom_register_title).split("\n")[0]

        assert qfrom_register_body.is_displayed(), "Не отображается форма авторизации Qform"
        assert qfrom_register_title_text == "Регистрация в QForm", "Заголовок формы авторизации Qform не соответствует"
        assert self.driver.current_url == REGPAGE, f"Не перешли по адресу {REGPAGE}"

    def main_page_navigation_menu(self, nav_logo="Функции"):
        """ Проверяем меню навигации"""
        logo_in_menu = self.find_by("xpath", self.element.logo_in_menu)
        logo_in_menu_text = self.get_text_from_one_element(logo_in_menu)
        navigation_item_titles = self.finds_by("xpath", self.element.navigation_item_titles)
        menu_list = self.find_by("xpath", self.element.menu_list)
        demo_button = self.find_by("xpath", self.element.demo_button)

        assert logo_in_menu_text == nav_logo, "Текст лого в меню навигации не соответствует"
        for title in navigation_item_titles:
            assert title.is_displayed(), f"Раздел {title.text.strip()} не отображается"
        assert not menu_list.is_displayed(), "Меню функции не отображается"
        assert demo_button.is_displayed(), "Кнопка Демо не отображается"

        # Клик по логотипу Функции для скрытия/открытия меню функции
        logo_in_menu.click()

        menu_list = self.is_visible("xpath", self.element.menu_list)
        icon_to_close_or_open_menu = self.get_text_from_one_element(
            self.find_by("xpath", self.element.icon_to_close_or_open_menu))
        menu_list_items = self.finds_by("xpath", self.element.menu_list_items)

        assert menu_list.is_displayed(), "Меню функции не отображается"
        for item in menu_list_items:
            assert item.is_displayed(), f"Пример {item.text.strip()} не отображается"
        assert icon_to_close_or_open_menu == "×", "Значок не поменялся на --> ×"

        # Клик по значку для скрытия/открытия меню функции
        icon_to_close_or_open_menu = self.find_by("xpath", self.element.icon_to_close_or_open_menu)
        icon_to_close_or_open_menu.click()
        time.sleep(2)

        icon_to_close_or_open_menu = self.get_text_from_one_element(
            self.find_by("xpath", self.element.icon_to_close_or_open_menu))
        menu_list = self.find_by("xpath", self.element.menu_list)

        assert icon_to_close_or_open_menu == "....", "Значок не поменялся на --> ...."
        assert not menu_list.is_displayed(), "Меню функции не исчезло"

    def demo_button(self, page_url):
        """ Проверка кнопки Демо в панели навигации Главной страницы"""
        self.find_by("xpath", self.element.demo_button).click()
        time.sleep(2)

        # Проверяем URL
        assert self.driver.current_url == f'{page_url}/demo', f"Адрес страницы не соответствует {page_url}/demo"

        self.top_menu()

        self.main_page_navigation_menu()

    def examples_button_for_scroll_to_slider(self, page_url: str):
        """ Кнопка Примеры и скролл до слайдера с примерами"""
        window_start_offset = self.driver.execute_script(
            'return window.pageYOffset')  # проверяем что текущее положение == 0
        assert window_start_offset == 0, "Текущее положение не равно 0"

        examples_button = self.find_by("xpath", self.element.examples_button)
        examples_button.click()
        time.sleep(2)
        assert self.driver.current_url == f'{page_url}#examples', f"Адрес страницы не соответствует {self.driver.current_url}"

        examples_section_offset = self.find_by("xpath", self.element.examples_section).get_property("offsetTop")
        window_y = self.driver.execute_script('return window.pageYOffset')
        assert -10 < window_y - examples_section_offset < 10, "Большая разница скролла до слайдера"

    def check_slider(self):
        # Собираем список слайдов
        list_images = self.finds_by("xpath", self.element.visible_images)

        # Далее в цикле у каждого берем свойство naturalWidth. Если значение == 0 то изображение не отображается

        for image in list_images:
            try:
                image_width = image.get_property('clientWidth')
                assert image_width > 0, self.driver.save_screenshot(f'screen/{self.data}.png')
            except:
                print(f"[INFO]:: Изображение в слайдере не отображается на странице {self.driver.current_url}")

        try:
            button_next_slide = self.find_by("xpath", self.element.button_next_slide)
            slide_list = self.finds_by("xpath", self.element.slide_list)
            for slide in slide_list:
                button_next_slide.click()
                time.sleep(1)
                assert slide.get_property("ariaHidden"), "Слайд не скрыт"
        except:
            print(f"[INFO]:: Слайд не скрывается на странице {self.driver.current_url}")

    def start_button(self):
        """ Проверка кнопки Начать"""
        start_button = self.find_by("xpath", self.element.start_button)
        self.action.move_to_element(start_button).perform()
        time.sleep(2)
        start_button.click()

        # Вызываем функцию проверки страницы Регистрации QForm
        self.qform_register_page()

    def offer_creation(self):
        """ Проверка кнопки по услуге создания форм"""
        button_for_offer = self.find_by("xpath", self.element.button_for_offer)
        self.action.move_to_element(button_for_offer).click(button_for_offer).perform()
        time.sleep(2)

        assert self.driver.current_url == SERVICE, f"Адрес страницы не соответствует {self.driver.current_url}"
        self.top_menu()
        self.main_page_navigation_menu()

    def footer(self):
        """ Проверка блока Футер"""
        self.scroll_to_footer()

        # Проверяем, что у футера отображается логотип куформ, взяв свойство clientWidth
        footer_logo_client_width = self.find_by("xpath", self.element.footer_logo).get_property("clientWidth")
        assert footer_logo_client_width > 0, "Логотип не отображается"

        # Проверяем список сервисов в цикле, что каждый из них отображается
        footer_service_list = self.finds_by("xpath", self.element.footer_service_list)
        for service in footer_service_list:
            assert service.is_displayed(), f"Сервис {service.text.strip()} не отображается"

        # Проверяем список соцсетей в цикле, что каждый из них отображается
        footer_social_list = self.finds_by("xpath", self.element.footer_social_list)
        for social in footer_social_list:
            assert social.is_displayed(), f"Значок соцсети не отображается"

    def scroll_to_footer(self):
        # Скроллим до футера
        footer = self.find_by("xpath", self.element.footer)
        self.action.move_to_element(footer).perform()
        time.sleep(2)

    def footer_social_icons(self):
        """ Проверка кнопок Соцсети в Футере страницы"""

        # Находим список соцсетей и проходимся циклом. В нем:
        # берем атрибут href, потом кликаем, переключаемся на открывшееся окно, сравниваем взятый адрес из href с фактическим
        footer_social_list = self.finds_by("xpath", self.element.footer_social_list)
        for social in footer_social_list:
            qform_window = self.driver.current_window_handle
            social_link = social.get_attribute("href").strip()
            social.click()

            window_list = self.driver.window_handles
            self.driver.switch_to.window(window_list[-1])
            time.sleep(4)

            assert self.driver.current_url == social_link, f"Адрес страницы не соответствует {social_link}"

            self.driver.close()
            self.driver.switch_to.window(qform_window)

    def footer_copyright(self):
        """ Проверка Авторских прав в Футере страницы"""

        footer_license_agreements = self.are_visible("xpath", self.element.footer_license_agreements)
        for agreement in footer_license_agreements:
            qform_window = self.driver.current_window_handle
            agreement_link = agreement.get_attribute("href").strip()
            agreement_text = self.get_text_from_one_element(agreement)
            agreement.click()

            window_list = self.driver.window_handles
            self.driver.switch_to.window(window_list[-1])

            assert self.driver.current_url == agreement_link, f"Адрес страницы не соответствует {agreement_link}"

            if self.driver.current_url == "https://help.qform.io/ru/":
                qfrom_reference_system = self.find_by("xpath", self.element.qfrom_reference_system)
                qfrom_reference_system_text = self.get_text_from_one_element(qfrom_reference_system)

                assert qfrom_reference_system_text == "Справочная система", "Заголовок на странице Справочная система не соответствует"
            else:
                title = self.find_by("xpath", self.element.title)
                title_text = self.get_text_from_one_element(title)

                assert title_text == agreement_text or title_text.startswith(
                    agreement_text), f"Текст ссылки {agreement_text} не соответствует заголовку страницы {title_text}"

                self.top_menu()
                self.main_page_navigation_menu()
            self.driver.close()
            self.driver.switch_to.window(qform_window)

    def interactive_slider(self):
        """ Проверка слайдера"""

        # Сохранить offset обертки (5375) - с ним будем сравнивать фактическую позицию окна после клика
        # big_slider_offset = self.find_by("xpath", self.element.big_slider).get_property("offsetTop")

        # Получить список слайдов для цикла
        slider_list = self.finds_by("xpath", self.element.slider_list)

        # Получить список больших слайдов для проверки отображения в цикле
        big_slider_list = self.finds_by("xpath", self.element.big_slider_list)

        # Скроллим до панели слайдов
        slider_panel = self.find_by("xpath", self.element.slider_panel)
        self.action.move_to_element(slider_panel).perform()
        time.sleep(2)

        # Устанавливаем счетчик для больших слайдов
        counter = 1

        # Делаем цикл из списка слайдов
        for slide in slider_list[1:]:
            # Клик по слайду
            slide.click()

            # Получить текущее положение: оно должно быть в промежутке +10 и -10 от обертки
            # current_window_offset = self.driver.execute_script('return window.pageYOffset')
            # assert -10 < current_window_offset - big_slider_offset < 10, "Большая разница скролла"

            # Скроллим до панели слайдов
            slider_panel_scroll = self.find_by("xpath", self.element.slider_panel)
            self.action.move_to_element(slider_panel_scroll).perform()
            time.sleep(2)

            # Проверка слайда в панели на отображение
            slide_client_width = slide.get_property("clientWidth")
            assert slide_client_width > 0, "Слайд не отображается"

            # Проверка большого слайда на отображение (будем брать по номеру из counter)
            big_slide_client_width = big_slider_list[counter].get_property("clientWidth")
            assert big_slide_client_width > 0, "Большой слайд не отображается"

            try:
                # находим стрелочку Next и берем property: ariaDisabled
                next_arrow = self.find_by("xpath", self.element.next_btn_slider)
                next_arrow_aria_disabled = next_arrow.get_attribute("ariaDisabled")
                if next_arrow_aria_disabled == "false":
                    next_arrow.click()
            except:
                pass
            counter += 1

    def other_page_navigation_menu(self, page_url, text_logo):
        """ Проверяем меню навигации других страниц"""

        # Берем Заголовок страницы
        title = self.find_and_get_text("xpath", self.element.title)

        # Берем текст лого в навигации
        official_logo = self.find_by("xpath", self.element.official_logo)

        # Блок со списком видов в навигации
        views_dropdown_panel = self.find_by("xpath", self.element.nav_views_dropdown_panel)

        # Кнопка Демо
        demo_button = self.find_by("xpath", self.element.demo_button)

        assert self.driver.current_url == page_url, f"URl не соответствует {self.driver.current_url}"
        assert title == text_logo, f"Заголовок не соответствует тексту у кнопки лого в меню"
        assert not views_dropdown_panel.is_displayed(), "Список видов отображается"
        assert demo_button.is_displayed(), "Кнопка Демо не отображается"

        # Наводим на раздел Виды
        views_item = self.find_by("xpath", self.element.views_item)
        self.action.move_to_element(views_item).perform()
        time.sleep(1)

        # Список видов в навигации
        nav_views_list_items = self.finds_by("xpath", self.element.nav_views_list_items)
        for item in nav_views_list_items:
            assert item.is_displayed(), f"Пример {item.text.strip()} не отображается"

        # logo_in_navigation.click()
        self.action.move_to_element(official_logo).perform()

        # Блок со списком видов в навигации
        views_dropdown_panel = self.find_by("xpath", self.element.nav_views_dropdown_panel)
        assert not views_dropdown_panel.is_displayed(), "Список видов отображается"

    def check_urls_views_dropdown(self):
        # Наводим на раздел Виды
        views_item = self.find_by("xpath", self.element.views_item)
        self.action.move_to_element(views_item).perform()
        time.sleep(1)

        # Получаем список видов в навигации
        nav_views_list_items = self.finds_by("xpath", self.element.nav_views_list_items)

        # Убираем курсор от выпадающего списка
        logo_in_navigation = self.find_by("xpath", self.element.logo_name_in_menu)
        # logo_in_navigation.click()
        self.action.move_to_element(logo_in_navigation).perform()
        time.sleep(1)

        # Цикл - наведение на Виды и переход
        for item in range(len(nav_views_list_items)):
            self.action.move_to_element(views_item).perform()
            time.sleep(1)

            link_url = self.get_attribute_from_one_element("href", nav_views_list_items[item])
            link_text = self.get_text_from_one_element(nav_views_list_items[item])

            nav_views_list_items[item].click()
            time.sleep(2)
            title = self.find_and_get_text("xpath", self.element.title)

            assert self.driver.current_url == link_url, f'Адрес страницы не соответствует {self.driver.current_url}'
            assert title == link_text, f'Заголовок не соответствует {title}'

    def check_views_page(self):
        pass

