import selenium
from selenium.webdriver.common.by import By


class GoogleSearch:
    def __init__(self, driver: selenium.webdriver.firefox):
        self.driver = driver

    def search(self, query: str):
        """
        Реализует поиск в Google
        :param query: Строка для поиска
        :return:
        """
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()

    def click_first_result(self):
        """
        Нажимает на первый результат поиска
        :return:
        """
        first_result = self.driver.find_element(By.CSS_SELECTOR, "h3")
        first_result.click()