from selenium import webdriver
import time
import pytest


@pytest.fixture(scope="class")
def OneTimeSetUp(request):
    driver = webdriver.Chrome(
        "C:\\Users\\Sanket\\Desktop\\boot_framework\\resources\\drivers\\chromedriver.exe")
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    time.sleep(4)
    # request.addfinalizer(OneTimeSetUp)
    # return driver
    request.cls.driver = driver

    yield driver
    time.sleep(3)
    driver.close()
    driver.quit()