import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HawkingBrosMainPage:
    def __init__(self, driver: selenium.webdriver.Firefox):
        self.driver = driver

    def get_current_url(self) -> str:
        """
        Возвращает URL страницы, где сейчас находится драйвер
        :return:
        """
        return self.driver.current_url

    def click_on_menu_burger(self):
        """
        Производится нажатие на кнопку, открывающую меню при помощи JS (так как она всегда перекрыта прехеадером)
        :return:
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "burger"))
        )
        self.driver.execute_script("document.querySelector('div.burger').click();")
        self.driver.implicitly_wait(10)

    def click_on_about_company_btn(self):
        """
        Производится нажатие на кнопку "О компании" при помощи JS
        :return:
        """
        about_us_link = self.driver.find_element(By.XPATH, "//a[@href='/about']")
        self.driver.execute_script("arguments[0].click();", about_us_link)
        self.driver.implicitly_wait(10)