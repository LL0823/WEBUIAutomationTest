#-*- coding:utf8 -*-
from base.readConfig import ReadConfig
from selenium import webdriver
from selenium.webdriver.ie import webdriver as ie_webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.chrome.options import Options

class DriverTool:

    @classmethod
    def get_driver(cls,selenium_hub,browser_type):
        driver=None
        browser_type=browser_type.lower()
        download_file_content_types = "application/octet-stream,application/vnd.ms-excel,text/csv,application/zip,application/binary"

        if browser_type=='ie':
            opt = ie_webdriver.Options()
            opt.force_create_process_api = True
            opt.ensure_clean_session = True
            opt.add_argument('-private')
            ie_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
            ie_capabilities.update(opt.to_capabilities())
            driver = webdriver.Remote(selenium_hub, desired_capabilities=ie_capabilities)
        elif browser_type=='firefox':
            firefox_profile=FirefoxProfile()
            # firefox_profile参数可以在火狐浏览器中访问about:config进行查看
            firefox_profile.set_preference('browser.download.folderList',2) # 0是桌面;1是“我的下载”;2是自定义
            firefox_profile.set_preference('browser.download.dir',ReadConfig().config.download_dir)
            firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk',download_file_content_types)
            driver = webdriver.Remote(selenium_hub, webdriver.DesiredCapabilities.FIREFOX.copy(),browser_profile=firefox_profile)
        elif browser_type=='chrome':
            chrome_options=Options()
            prefs={'download.default_directory':ReadConfig().config.download_dir,'profile.default_content_settings.popups':0}
            chrome_options.add_experimental_option('prefs',prefs)
            driver = webdriver.Remote(selenium_hub, webdriver.DesiredCapabilities.CHROME.copy(),options=chrome_options)
        else:
            return driver
        driver.maximize_window()
        driver.delete_all_cookies()
        return driver