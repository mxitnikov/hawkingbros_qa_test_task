from selenium import webdriver
import unittest
from page_objects.google_search import GoogleSearch
from page_objects.hawkins_bros_main import HawkingBrosMainPage
from page_objects.hawking_brow_about import HawkingBrosAboutPage


class TestHawkingBros(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        # Настройка FirefoxDriver
        cls.driver = webdriver.Firefox()
        cls.driver.set_window_size(1920, 1080)
        cls.driver.implicitly_wait(10)

    def test_navigate_to_about_us(self):
        # Шаг 1: Открыть Google
        self.driver.get("https://www.google.com")

        # Создаем объект страницы Google
        google_page = GoogleSearch(self.driver)
        google_page.search("hawkingbros.com")  # Ищем Hawking Bros
        google_page.click_first_result()  # Переходим по первой ссылке

        # Создаем объект главной страницы Hawking Bros
        hawking_bros_main_page = HawkingBrosMainPage(self.driver)

        # Проверяем, что мы на главной странице
        self.assertIn("https://hawkingbros.com", hawking_bros_main_page.get_current_url())

        # Шаг 2: Нажимаем на кнопку меню и далее на "О компании"
        hawking_bros_main_page.click_on_menu_burger()
        hawking_bros_main_page.click_on_about_company_btn()

        # Создаем объект страницы Hawking Bros "О компании"
        hawking_bros_about_page = HawkingBrosAboutPage(self.driver)

        # Шаг 3: Проверяем наличие текста
        target_text = "Компания Hawking Bros была основана в 2014 году в городе Владимире."
        text_on_page_result = hawking_bros_about_page.text_located_on_page(target_text)

        self.assertTrue(text_on_page_result is True)

    @classmethod
    def tearDownClass(cls):
        # Закрытие драйвера
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()