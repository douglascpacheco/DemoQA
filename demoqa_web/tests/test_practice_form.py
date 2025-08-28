import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import os

fake = Faker()
UPLOAD_FILE_PATH = os.path.join(os.path.dirname(__file__), '../uploads/upload.txt')

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def close_banner_if_exists(driver):
    try:
        banner = driver.find_element(By.ID, "close-fixedban")
        banner.click()
    except:
        pass

def test_practice_form(driver):
    driver.get('https://demoqa.com/')
    close_banner_if_exists(driver)

    forms_card = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']/ancestor::div[contains(@class,'card')]"))
    )
    forms_card.click()

    practice_form = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']"))
    )
    practice_form.click()

    driver.find_element(By.ID, 'firstName').send_keys(fake.first_name())
    driver.find_element(By.ID, 'lastName').send_keys(fake.last_name())
    driver.find_element(By.ID, 'userEmail').send_keys(fake.email())
    driver.find_element(By.XPATH, "//label[text()='Male']").click()
    driver.find_element(By.ID, 'userNumber').send_keys(fake.msisdn()[0:10])
    driver.find_element(By.ID, 'dateOfBirthInput').send_keys('01 Jan 2000\n')
    driver.find_element(By.ID, 'subjectsInput').send_keys('Maths\n')
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()
    driver.find_element(By.ID, 'uploadPicture').send_keys(os.path.abspath(UPLOAD_FILE_PATH))
    driver.find_element(By.ID, 'currentAddress').send_keys(fake.address())
    driver.find_element(By.ID, 'react-select-3-input').send_keys('NCR\n')
    driver.find_element(By.ID, 'react-select-4-input').send_keys('Delhi\n')

    driver.find_element(By.ID, 'submit').click()

    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content'))
    )
    assert modal.is_displayed()
    driver.find_element(By.ID, 'closeLargeModal').click()

def test_practice_form_negative(driver):
    driver.get('https://demoqa.com/')
    close_banner_if_exists(driver)

    forms_card = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']/ancestor::div[contains(@class,'card')]"))
    )
    forms_card.click()

    practice_form = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']"))
    )
    practice_form.click()

    driver.find_element(By.ID, 'submit').click()

    try:
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content'))
        )
        assert False, "Popup não deveria aparecer sem preencher campos obrigatórios."
    except:
        pass
