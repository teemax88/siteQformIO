import time
from pom.BasePage.basemodel import Basemodel
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(Basemodel):
    def __init__(self, driver):
        super().__init__(driver)

        self.action = ActionChains(driver)

    def gif_for_insert_form(self):
        """ Проверка плеера с анимацией Как вставить форму на сайт"""
        gif_block = self.find_by("xpath", self.element.gif_block_for_insert_form)
        self.action.move_to_element(gif_block).perform()

        video_player = self.find_by("xpath", self.element.video_player)
        assert video_player.is_displayed()

        active_player_menu_item = self.find_by("xpath", self.element.active_player_menu_item)
        active_player_menu_item_text = self.get_text_from_one_element(active_player_menu_item)
        video_src_list = list(video_player.get_attribute('src').strip())

        assert active_player_menu_item_text == "Добавить сайт", f"{active_player_menu_item_text} не является активным элементом меню"

        inactive_menu_names = ['Создать форму', 'Настроить поля', 'Вставить код на свой сайт']
        index = 0
        inactive_player_menu_items = self.finds_by("xpath", self.element.inactive_player_menu_items)
        for menu in inactive_player_menu_items:
            menu.click()
            time.sleep(1)
            menu_text = self.get_text_from_one_element(menu)
            src = video_player.get_attribute('src').strip()
            assert src not in video_src_list, "Ссылка на видео не изменилась"
            assert menu_text == inactive_menu_names[index], f"Название активного меню не соответствует {menu_text}"

            video_src_list.append(src)
            index += 1

    def service_cards(self):
        """ Проверка кнопок на карточках с сервисами"""
        official_logo = self.find_by("xpath", self.element.official_logo)
        service_cards = self.are_visible("xpath", self.element.service_cards)
        service_cards_title = self.are_visible("xpath", self.element.service_cards_title)
        service_cards_title_list = self.get_text_all_webelements(service_cards_title)
        count_cards = len(service_cards)
        for card in range(count_cards - 1):
            # При каждой итерации заново ищем карточки, так как при возвращении на страницу состояние элемента меняется
            button_for_service_cards = self.are_visible("xpath", self.element.button_for_service_cards)

            # Берем из кнопки ссылку на страницу, куда должен произойти переход
            card_link = button_for_service_cards[card].get_attribute("href")

            # Переменная card будет иметь последовательный номер, по которому мы будем переходить к следующей карточке
            self.action.move_to_element(button_for_service_cards[card]).click(button_for_service_cards[card]).perform()
            time.sleep(2)

            # Передаем сохраненную ссылку очередной карточки и передаем ее в функцию для проверки соответствия страницы
            self.other_page_navigation_menu(card_link, service_cards_title_list[card])

            official_logo.click()
            time.sleep(2)

    def quiz_constructor_button(self, page_url):
        """ Проверка кнопки Конструктор квизов в панели навигации Главной страницы"""
        self.find_by("xpath", self.element.quiz_constructor_button).click()
        time.sleep(2)

        self.other_navigation_menu(page_url)
        self.top_menu()

    def videowidget_button(self, page_url):
        """ Проверка кнопки Видеовиджет в панели навигации Главной страницы"""
        self.find_by("xpath", self.element.videowidget_button).click()
        time.sleep(2)

        self.other_navigation_menu(page_url)
        self.top_menu()

    def qlink_button(self):
        """ Проверка кнопки Qlink в панели навигации Главной страницы"""
        qlink_button = self.find_by("xpath", self.element.qlink_button)
        qlink_button_link = qlink_button.get_attribute("href").strip()
        qlink_button.click()
        time.sleep(2)

        window_list = self.driver.window_handles
        self.driver.switch_to.window(window_list[-1])

        qlink_page_title = self.find_by("xpath", self.element.qlink_page_title)
        qlink_page_title_text = self.get_text_from_one_element(qlink_page_title)

        assert self.driver.current_url == qlink_button_link, f"Текущий адрес {self.driver.current_url} не соответствует {qlink_button_link}"
        assert qlink_page_title_text == "QForm.link", f"Заголовок не соответствует {qlink_page_title_text}"

        """ Клик по логотипу QForm в футере страницы"""
        qlink_footer_logo = self.find_by("xpath", self.element.qlink_footer_logo)
        assert qlink_footer_logo.is_displayed(), "Логотип не отображается"

        qlink_footer_logo.click()
        time.sleep(2)

        assert self.driver.current_url == "https://qform.io/", f"Текущий адрес {self.driver.current_url} не соответствует"









