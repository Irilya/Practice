import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():


      pytest.driver = webdriver.Edge('C:\SkillBox\edgedriver_win64\msedgedriver.exe')
      pytest.driver.implicitly_wait(10)
      # Переходим на страницу авторизации
      pytest.driver.get('http://petfriends1.herokuapp.com/login')

      yield

      pytest.driver.quit()


def test_show_all_pets():
      element = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'pass'))
      )


      # Вводим email
      pytest.driver.find_element_by_id('email').send_keys('irilya@mail.ru')
      # Вводим пароль
      pytest.driver.find_element_by_id('pass').send_keys('cambala')
      # Нажимаем на кнопку входа в аккаунт
      pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

      # Проверяем, что мы оказались на главной странице пользователя
      assert pytest.driver.find_element_by_xpath("(//div[contains(text(), 'Все питомцы наших пользователей')])")

      images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
      names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
      descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

      for i in range(len(names)):
            assert images[i].get_attribute('src') != ''
            assert names[i].text != ''
            assert descriptions[i].text != ''
            assert ',' in descriptions[i].text
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0


def test_show_my_pets():
      myDynamicElement = pytest.driver.find_element_by_id("email")

      # Вводим email
      pytest.driver.find_element_by_id('email').send_keys('irilya@mail.ru')
      # Вводим пароль
      pytest.driver.find_element_by_id('pass').send_keys('cambala')
      # Нажимаем на кнопку входа в аккаунт
      pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
      assert pytest.driver.find_element_by_xpath("(//div[contains(text(), 'Все питомцы наших пользователей')])")
      pytest.driver.find_element_by_css_selector('button.navbar-toggler').click()
      # Нажимаем на ссылку перехода на страницу "Мои питомцы"
      pytest.driver.find_element_by_link_text("Мои питомцы").click()
      # Проверяем, что мы оказались на странице с питомцами пользователя
      assert pytest.driver.find_element_by_id("all_my_pets")

      number_of_pets = pytest.driver.find_element_by_xpath('/html/body/div/div[1]').text.split()
      number_of_pets = int(number_of_pets[2])
      count_pets = pytest.driver.find_elements_by_xpath('//*[@id ="all_my_pets"]//tbody/tr')

      assert number_of_pets == len(count_pets)
