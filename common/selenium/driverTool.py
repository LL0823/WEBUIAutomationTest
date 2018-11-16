#-*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.ie import webdriver as ie_webdriver

class DriverTool:

    @classmethod
    def get_driver(cls,selenium_hub,browser_type):
        driver=None
        browser_type=browser_type.lower()
        if browser_type=='ie':
            opt = ie_webdriver.Options()
            opt.force_create_process_api = True
            opt.ensure_clean_session = True
            opt.add_argument('-private')
            ie_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
            ie_capabilities.update(opt.to_capabilities())
            driver = webdriver.Remote(selenium_hub, desired_capabilities=ie_capabilities)
        elif browser_type=='firefox':
            driver = webdriver.Remote(selenium_hub, webdriver.DesiredCapabilities.FIREFOX.copy())
        elif browser_type=='chrome':
            driver = webdriver.Remote(selenium_hub, webdriver.DesiredCapabilities.CHROME.copy())
        else:
            return driver
        driver.maximize_window()
        driver.delete_all_cookies()
        return driver