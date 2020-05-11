# coding:utf-8
from common.login import *
from common.location import *
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

saleno = 'Z0002'
buyerno = 'K0001'
brandno = 'BS'
categoryno = '01'
startdate = '2019-12-01'
enddate = '2019-12-31'


class Test_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.denglu = Login.login_xie(cls, )
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_001(self):
        u'''总部地区结算'''
        title = self.driver.title
        self.assertEqual(title, "百丽零售FAS管理系统")
        self.driver.implicitly_wait(10)

        # 输入菜单名称查询
        self.driver.find_element_by_xpath("//input[@type='text' and @autocomplete='off']").send_keys("HU-结算单")
        sleep(2)
        # 进入菜单
        self.driver.find_element_by_xpath("//input[@type='text' and @autocomplete='off']").send_keys(Keys.ENTER)

        # 跳回顶端
        self.driver.switch_to.default_content()

        # 定位frame位置
        f1 = self.driver.find_element_by_xpath("//iframe[@class='panel-iframe']")
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='panel-iframe']"))
        # 跳转frame
        self.driver.switch_to.frame(f1)
        sleep(1)

        # 点击批量生成
        self.driver.find_element_by_xpath('//*[text()="批量生成"]').click()
        sleep(2)

        # 选择品牌部
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[1]/td/span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[1]/td/span/input').send_keys(brandno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r5-2-0"]/td[1]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[1]/td/span/span/span').click()

        # 选择公司
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[2]/td/span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[2]/td/span/input').send_keys(saleno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r6-2-0"]/td[1]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[2]/td/span/span/span').click()

        # 选择品牌
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[3]/td/span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[3]/td/span/input').send_keys(brandno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r7-2-0"]/td[1]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[3]/td/span/span/span').click()

        # 选择客户
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[4]/td/span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[4]/td/span/input').send_keys(buyerno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r8-2-0"]/td[1]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[4]/td/span/span/span').click()

        # 选择大类
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[5]/td/span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[5]/td/span/input').send_keys(categoryno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r9-2-0"]/td[1]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[5]/td/span/span/span').click()

        # 输入结算单日期
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[10]/td/input').click()
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[10]/td/input').clear()
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[10]/td/input').send_keys(enddate)
        self.driver.find_element_by_xpath('//*[@id="dataForm"]/div/table/tbody/tr[10]/td/input').send_keys(Keys.ENTER)

        # 输入起始日期
        self.driver.find_element_by_xpath('//*[@id="batchBalanceStartDate"]').clear()
        self.driver.find_element_by_xpath('//*[@id="batchBalanceStartDate"]').click()
        self.driver.find_element_by_xpath('//*[@id="batchBalanceStartDate"]').send_keys(startdate)
        self.driver.find_element_by_xpath('//*[@id="batchBalanceStartDate"]').send_keys(Keys.ENTER)

        # 输入结束日期
        self.driver.find_element_by_xpath('//*[@id="batchBalanceEndDate"]').clear()
        self.driver.find_element_by_xpath('//*[@id="batchBalanceEndDate"]').click()
        self.driver.find_element_by_xpath('//*[@id="batchBalanceEndDate"]').send_keys(enddate)
        self.driver.find_element_by_xpath('//*[@id="batchBalanceEndDate"]').send_keys(Keys.ENTER)

        # 点击确认生成结算单
        self.driver.find_element_by_xpath('//*[@id="myFormPanel"]/div[2]/a[1]/span/span').click()
        sleep(1)


if __name__ == "__main__":
    unittest.main()

