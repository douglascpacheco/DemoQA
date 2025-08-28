from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Caminho do arquivo para upload
file_path = os.path.abspath("arquivo_teste.txt")

# Cria o arquivo de upload se não existir
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("Arquivo de teste para upload.")

def test_practice_form():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")

    driver.find_element(By.ID, "firstName").send_keys("Nome")
    driver.find_element(By.ID, "lastName").send_keys("Sobrenome")
    driver.find_element(By.ID, "userEmail").send_keys("email@teste.com")
    driver.find_element(By.XPATH, "//label[text()='Male']").click()
    driver.find_element(By.ID, "userNumber").send_keys("11999999999")
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)
    driver.find_element(By.ID, "currentAddress").send_keys("Endereço teste")
    driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
    driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)
    driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
    driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert driver.find_element(By.ID, "example-modal-sizes-title-lg").is_displayed()
    driver.find_element(By.ID, "closeLargeModal").click()
    driver.quit()
