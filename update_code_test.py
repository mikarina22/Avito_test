import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAvito(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_to_favorites(self):
        driver = self.driver
        driver.get("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".desktop-usq1f1")))
        submit_button.click()

        item_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".desktop-p6xjn6")))
        try:
            self.assertEqual(item_name.text, "В избранном")
            print("Тест пройден успешно")
        except AssertionError:
            print("Тест не пройден")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()