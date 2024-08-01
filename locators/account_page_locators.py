from selenium.webdriver.common.by import By


class AccountPageLocators:
    ORDERS_HISTORY_LINK = By.LINK_TEXT, "История заказов"
    EXIT_FROM_ACCOUNT_BUTTON = By.XPATH, "//*[text()='Выход']"
