import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class HawkingBrosAboutPage:
    def __init__(self, driver: selenium.webdriver.Firefox):
        self.driver = driver

    def text_located_on_page(self, text: str) -> bool:
        """
        Возвращается True/False в зависимости от того, есть ли текст на странице
        :param text: Нужный текст
        :return:
        """

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{text}")]')))

            if element.is_displayed():
                return True

        except TimeoutException:
            return False

        except NoSuchElementException:
            return False

