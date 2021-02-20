from .Predict import Predictor
from selenium.webdriver import (Chrome, Firefox, ChromeOptions, FirefoxProfile)
import datetime
import yaml
import time
import random

class FBScraper():
    def __init__(self, email, password, profile, status = 4, scroll_time = 7, browser= 'Firefox'):
        self.first_email = email
        self.first_password = password
        self.first_profile_url = profile
        self.number_status = status
        self.scroll_time = scroll_time
        self.name = profile.split("/")[3]
 
        y = self.set_browser(browser)
        self.dic_status = {}

    def set_browser(self, browser):
        #Firefox
        if browser == 'Firefox':
            profile = FirefoxProfile()
            profile.set_preference("dom.webnotifications.enabled", False)
            self.browser = Firefox(firefox_profile=profile)
            
        #Chrome
        if browser == 'Chrome':
            options = ChromeOptions()
            options.add_argument("--disable-notifications")
            self.browser = Chrome(options=options)
    def open_fb(self):
        #Login to FB in Selenium Browser
        url = 'http://www.facebook.com/'
        self.browser.get(url)

        email =self.browser.find_element_by_id('email')
        password = self.browser.find_element_by_id('pass')

        email.send_keys(self.first_email)
        password.send_keys(self.first_password)

        self.browser.find_element_by_id("loginbutton").click()

   
