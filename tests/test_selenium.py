import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TestYandexAuth:
    @pytest.fixture(autouse=True)
    def setup_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_yandex_login(self):
        try:
            self.driver.get("https://passport.yandex.ru/auth/")

            phone_input_field = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="tel"]'))
            )
            phone_input_field.clear()

            # Ждем ввода номера телефона и нажатия кнопки войти / Окно ввода телефона
            is_visible_input_code = None
            while is_visible_input_code is None:
                try:
                    is_visible_input_code = self.driver.find_element(By.CSS_SELECTOR,
                                            'input[data-testid="code-field-segment"]')
                except NoSuchElementException:
                    pass

            # Ждем ввода одиночного кода / Окно ввода кода
            is_visible_choose_user = None
            while is_visible_choose_user is None:
                try:
                    is_visible_choose_user = self.driver.find_element(By.CSS_SELECTOR,
                                            'div[data-testid="page-suggest"]')
                except NoSuchElementException:
                    pass

            # Проверка на вход в свой аккаунт / Окно выбора аккаунта
            while True:
                try:
                    enter = self.wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'section[data-testid="user-info-section"]'))
                    )
                    assert enter.is_displayed(), "Авторизация не прошла успешно"
                    break
                except TimeoutException:
                    pass

                is_id = None
                while is_id is None:
                    try:
                        is_id = self.driver.find_element(By.CSS_SELECTOR,
                                'section[data-testid="user-info-section"]')
                    except NoSuchElementException:
                        pass

        except TimeoutException:
            pytest.fail("Таймаут ожидания элемента: элемент не появился в течение заданного времени")
        except Exception as e:
            pytest.fail(f"Произошла ошибка: {str(e)}")