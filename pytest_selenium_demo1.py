import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # setting up the driver instance
    driver.implicitly_wait(10) #the time the driver should wait before it finds an element or how much time it must wait before failing

    yield driver
    driver.close() #closing the driver instance
    driver.quit()



def test_google_search(driver): #pass the driver parameter
    driver.get("https://www.google.com")
    googleSearch = driver.find_element(By.ID, "APjFqb")
    googleSearch.send_keys("Automation")
    googleSearch.send_keys(Keys.RETURN)
    time.sleep(2)
    print("Google Search Test Complete")