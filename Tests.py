# python -m pytest -v --driver Chrome --driver-path C:\chromedriver C:\Users\User\PycharmProjects\final_project_SF_28/Tests.py
from Base_page import *
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from Page_Object import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def test_vision(selenium):
    ''' ТК-001 общий вид страницы (сохранение скриншота)'''
    form = AuthForm(selenium)
    form.driver.save_screenshot('screenshot_001.jpg')

def test_by_phone(selenium):
    '''ТК - 005 по умолчанию выбрана форма авторизации по телефону'''
    form = AuthForm(selenium)
    assert form.placeholder.text == 'Мобильный телефон'

def test_positive_by_phone(selenium):
    ''' ТК - 006 авторизация по телефону'''
    form = AuthForm(selenium)
    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()
    assert form.get_current_url() != '/account_b2c/page'

def test_positive_by_email(selenium):
    '''ТК - 007 авторизация по почте'''
    form = AuthForm(selenium)
    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()
    assert form.get_current_url() != '/account_b2c/page'

def test_positive_by_log(selenium):
    '''ТК - 008 авторизация по логину'''
    form = AuthForm(selenium)
    # ввод логина
    form.username.send_keys('valid_email')
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()
    assert form.get_current_url() != '/account_b2c/page'


def test_get_code(selenium):
    '''Тк- 011 получения временного кода на телефон, открытие формы для ввода кода'''
    form = CodeForm(selenium)
    # ввод телефона
    form.address.send_keys(valid_phone)
    # пауза для ввода капчи
    sleep(15)
    form.get_click()
    rt_code = form.driver.find_element(By.ID, 'rt-code-0')
    assert rt_code

def test_change_placeholder(selenium):
    '''TK- 012 проверка автоматического изменения типа аутентификации'''
    form = AuthForm(selenium)
    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys('_')
    sleep(5)
    assert form.placeholder.text == 'Мобильный телефон'
    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)
    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys('_')
    sleep(5)
    assert form.placeholder.text == 'Электронная почта'
    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)
    # ввод логина
    form.username.send_keys('Login')
    form.password.send_keys('_')
    sleep(5)
    assert form.placeholder.text == 'Логин'

def test_forgot_pass(selenium):
    '''ТК - 013 открытие формы восстановления пароля'''
    form = AuthForm(selenium)
    # нажатие надписи "Забыл пароль"
    form.forgot.click()
    sleep(5)
    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    assert reset_pass.text == 'Восстановление пароля'


def test_register(selenium):
    '''TK- 014 переход и открытие формы регистрации'''
    form = AuthForm(selenium)
    # нажатие на надпись "Зарегистрироваться"
    form.register.click()
    sleep(5)
    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    assert reset_pass.text == 'Регистрация'


def test_agreement(selenium):
    '''TK- 015 открытие пользовательского соглашения'''
    form = AuthForm(selenium)
    original_window = form.driver.current_window_handle
    # нажатие на надпись "Пользовательское соглашение" в подвале
    form.agree.click()
    sleep(5)
    WebDriverWait(form.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in form.driver.window_handles:
        if window_handle != original_window:
            form.driver.switch_to.window(window_handle)
            break
    win_title = form.driver.execute_script("return window.document.title")
    assert win_title == 'User agreement'


def test_auth_vk(selenium):
    '''TK-017 переход по ссылке авторизации через соцсеть ВК '''
    form = AuthForm(selenium)
    form.vk_btn.click()
    sleep(5)
    assert form.get_base_url() == 'oauth.vk.com'

def test_auth_ok(selenium):
    '''TK-018 переход по ссылке авторизации через соцсеть ОК'''
    form = AuthForm(selenium)
    form.ok_btn.click()
    sleep(5)
    assert form.get_base_url() == 'connect.ok.ru'


def test_auth_mailru(selenium):
    '''TK-019 переход по ссылке авторизации через майл.ру'''
    form = AuthForm(selenium)
    form.mailru_btn.click()
    sleep(5)
    assert form.get_base_url() == 'connect.mail.ru'


def test_auth_google(selenium):
    '''TK-020 перехода по ссылке авторизации через google'''
    form = AuthForm(selenium)
    form.google_btn.click()
    sleep(5)
    assert form.get_base_url() == 'accounts.google.com'


def test_auth_ya(selenium):
    '''TK-021 переход по ссылке авторизации через яндекс'''
    form = AuthForm(selenium)
    form.ya_btn.click()
    sleep(5)
    assert form.get_base_url() == 'b2c.passport.rt.ru'

def test_negative_by_zero(selenium):
    '''TK-022 негативный сценарй авторизации с пустыми полями'''
    form = AuthForm(selenium)
    # ввода нет
    form.username.send_keys(' ')
    form.password.send_keys(' ')
    sleep(5)
    form.btn_click()
    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'

def test_negative_by_phone(selenium):
    '''TK-024 негативный сценарй авторизации по телефону'''
    form = AuthForm(selenium)
    # ввод телефона
    form.username.send_keys('+89206957')
    form.password.send_keys('any_password')
    sleep(5)
    form.btn_click()
    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'

def test_negative_by_email(selenium):
    '''TK-027 негативный сценарий авторизации по почте'''
    form = AuthForm(selenium)
    # ввод почты
    form.username.send_keys('dfdfdf@dfgfd')
    form.password.send_keys('any_password')
    sleep(5)
    form.btn_click()
    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'

def test_negative_by_log(selenium):
    '''TK-026 негативный сценарий авторизации по логину'''
    form = AuthForm(selenium)
    # ввод логина
    form.username.send_keys('rtdfdfdf')
    form.password.send_keys('any_password')
    sleep(5)
    form.btn_click()
    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'

def test_negative_by_pers_acc(selenium):
    '''TK-027 негативный сценарий авторизации по лицевому счету'''
    form = AuthForm(selenium)
    # ввод логина
    form.username.send_keys('rsdffsdfsdf')
    form.password.send_keys('any_password')
    sleep(5)
    form.btn_click()
    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'