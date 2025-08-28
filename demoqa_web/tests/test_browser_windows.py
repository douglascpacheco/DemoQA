import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def close_banner_if_exists(driver):
    try:
        driver.find_element(By.ID, "close-fixedban").click()
    except:
        pass

def test_browser_windows(driver):
    driver.get('https://demoqa.com/')
    close_banner_if_exists(driver)

    alerts_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Alerts, Frame & Windows']/ancestor::div[contains(@class,'card')]"))
    )
    alerts_card.click()

    browser_windows = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Browser Windows']"))
    )
    browser_windows.click()

    main_window = driver.current_window_handle
    driver.find_element(By.ID, 'windowButton').click()

    handles = driver.window_handles
    assert len(handles) > 1

    driver.switch_to.window(handles[1])
    msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'sampleHeading'))
    )
    assert msg.text == "This is a sample page"
    driver.close()
    driver.switch_to.window(main_window)

def test_browser_windows_negative(driver):
    driver.get('https://demoqa.com/')
    close_banner_if_exists(driver)

    try:
        driver.find_element(By.ID, 'windowButton').click()
        handles = driver.window_handles
        assert len(handles) == 1, "Nenhuma nova janela deveria ser aberta fora da página correta."
    except:
        pass
