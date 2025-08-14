from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("tomsmith")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    mydiv = driver.find_element(By.XPATH, "//div[@id='flash-messages']")
    assert "You logged into a secure area!" in mydiv.text
    driver.quit()
