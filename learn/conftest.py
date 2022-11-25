from selenium import webdriver
import pytest
import time


@pytest.fixture(scope="function")
def browser_chrome():

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "106.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        }
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:8080/wd/hub",
        desired_capabilities=capabilities)

    yield driver
    time.sleep(20)
    driver.quit()


@pytest.fixture(scope="function")
def browser_firefox():

    capabilities = {
        "browserName": "firefox",
        "browserVersion": "",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    driver = webdriver.Remote(
        command_executor='http://localhost:8080/wd/hub',
        desired_capabilities=capabilities
    )
    yield driver
    time.sleep(20)
    driver.quit()











