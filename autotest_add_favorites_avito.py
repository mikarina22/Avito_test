import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвер браузера. После этой команды открывается новое открытое окно браузера
driver = webdriver.Chrome()

# Открыть страницу с карточкой объявления
driver.get("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")

# Найти кнопку, которая добавляет в "Избранное"
submit_button = driver.find_element(By.CSS_SELECTOR, ".desktop-usq1f1")

# Нажать на кнопку.
submit_button.click()

# Выполняется проверка на добавление объявления в избранное. Результат теста выводится в консоль.
item_name = driver.find_element(By.CSS_SELECTOR, ".desktop-p6xjn6")
if item_name.text == "В избранном":
   print("Тест пройден успешно")
else:
   print("Тест не пройден")

# После выполнения всех действий закрыть окно браузера
driver.quit()