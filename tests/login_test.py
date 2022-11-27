from selenium import webdriver
from time import sleep
from pages.login_page import LoginPage
import pytest

def test_landing_page(setup):
    driver = setup
    assert driver.title == 'EBANQ'
    driver.quit()

def test_user_login(setup):
    driver = setup
    loginP = LoginPage(driver)
    loginP.user_login()
    sleep(5)
    assert 'John Doe' in driver.page_source
   
def test_login_with_blankusername(setup):
    driver = setup 
    loginPage = LoginPage(driver)
    loginPage.login_with_blank_user_name()
    assert "Field is required" in driver.page_source

def test_login_with_incorrect_cridentials(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_with_incorrect_cridentials()
    sleep(5)
    assert 'Wrong username or password' in driver.page_source

invalid_login_data = [
    ("", "", "Field is required."),
    ("test", "test", "Wrong username or password."),
    ("abc", "test", "Should be minimum 4 chars")
]

@pytest.mark.parametrize("username, password, checkpoint", invalid_login_data)
def test_invalidLogin(setup, username, password, checkpoint):
    driver = setup 
    loginP = LoginPage(driver)
    loginP.Login(username, password)
    sleep(5)
    assert checkpoint in driver.page_source
