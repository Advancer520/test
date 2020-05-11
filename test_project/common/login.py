# coding:utf-8
import unittest
from selenium import webdriver
import time


class Login():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def login_xie(self, username="autotest-xie", password="123456"):
        self.driver.get("https://sso-test.belle.net.cn")
        self.driver.maximize_window()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("submit_name_password").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='零售系统']").click()
        time.sleep(1)

    def login_ty(self, username="autotest-ty", password="123456"):
        self.driver.get("https://sso-test.belle.net.cn")
        self.driver.maximize_window()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("submit_name_password").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='零售系统']").click()
        time.sleep(1)







