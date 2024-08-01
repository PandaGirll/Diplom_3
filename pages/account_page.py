import allure

from data import URLs
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.URL = URLs.ACCOUNT_PAGE

    @allure.step('Открываем страницу Личный Кабинет {self.URL}')
    def open_account_page(self):
        self.open_page(self.URL)

    @allure.step('Дожидаемся полной загрузки страницы')
    def wait_loading_page(self):
        self.wait_visibility(AccountPageLocators.ORDERS_HISTORY_LINK)

    @allure.step('Нажимаем на ссылку "История заказов"')
    def click_link_order_history(self):
        self.click_element(AccountPageLocators.ORDERS_HISTORY_LINK)

    @allure.step("Нажимаем на кнопку 'Выход'")
    def click_button_exit(self):
        self.click_element(AccountPageLocators.EXIT_FROM_ACCOUNT_BUTTON)
