# coding:utf-8
from common.login import *
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
        cls.denglu = Login.login_xie(cls,)
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
        self.driver.find_element_by_xpath("//input[@type='text' and @autocomplete='off']").send_keys("HU-出库明细表")
        sleep(1)
        # 进入菜单
        self.driver.find_element_by_xpath("//input[@type='text' and @autocomplete='off']").send_keys(Keys.ENTER)
        
        # 跳回顶端
        self.driver.switch_to.default_content()

        # 定位frame位置
        f1 = self.driver.find_element_by_xpath("//iframe[@class='panel-iframe']")
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='panel-iframe']"))
        # 跳转frame
        self.driver.switch_to.frame(f1)
        
        # 输入公司条件
        self.driver.find_element_by_xpath('//*[@id="searchForm"]/table/tbody/tr[1]/td[1]/span/input').click()
        # self.driver.find_element_by_xpath('//*[@id="multiSalerNo"]/../span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="searchForm"]/table/tbody/tr[1]/td[1]/span/input').send_keys(saleno)
        sleep(1)
        # 选定公司
        self.driver.find_element_by_xpath('//input[@type="checkbox" and @name="ck"]').click()
        
        # 输入客户
        self.driver.find_element_by_xpath('//*[@name="multiBuyerNo"]/../span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@name="multiBuyerNo"]/../span/input').send_keys(buyerno)
        sleep(1)
        # 选定客户
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[1]/div').click()
        
        # 输入品牌
        self.driver.find_element_by_xpath('//*[@name="multiBrandUnitNo"]/../span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@name="multiBrandUnitNo"]/../span/input').send_keys(brandno)
        sleep(1)
        # 选定品牌
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[1]/div').click()
        
        # 输入大类
        self.driver.find_element_by_xpath('//*[@name="multiCategoryNo"]/../span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@name="multiCategoryNo"]/../span/input').send_keys(categoryno)
        sleep(1)
        # 选定大类
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r4-2-0"]/td[1]/div').click()
        
        # 输入起始日期
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').clear()
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').click()
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').send_keys(startdate)

        # 输入结束日期
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').clear()
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').click()
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').send_keys(enddate)
        # 点击查询
        self.driver.find_element_by_xpath('//span[@class="l-btn-text icon-search l-btn-icon-left"]').click()
        sleep(2)

        salename = self.driver.find_element_by_xpath('//*[@id="datagrid-row-r12-2-0"]/td[1]/div').text
        print(salename)
        self.assertEqual(salename, "百丽鞋业（宿州）有限公司")

        balanceno = self.driver.find_element_by_xpath('//*[@id="datagrid-row-r12-2-0"]/td[29]/div/a').text
        print(balanceno)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r12-2-0"]/td[29]/div/a').click()
        sleep(2)

        self.driver.switch_to.default_content()
        # 跳转到第二个frame
        f2 = self.driver.find_element_by_xpath('//*[@id="mainTabs"]/div[2]/div[3]/div/iframe')
        self.driver.switch_to.frame(f2)

        # 点击结算单浏览
        self.driver.find_element_by_xpath('//*[@id="top_btn_add"]/span').click()
        sleep(2)

        # 输入结算单号
        self.driver.find_element_by_xpath('//input[@name="billNo" and @class="ipt"]').send_keys(balanceno)

        # 输入起始日期
        self.driver.find_element_by_xpath('//input[@id="startDate"]').clear()

        # 输入结束日期
        self.driver.find_element_by_xpath('//input[@id="endDate"]').clear()

        # 结算单查询
        self.driver.find_element_by_xpath('//*[text()="查询"]/../span').click()
        sleep(2)
        # 选中数据
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r16-1-0"]').click()
        sleep(1)

        # # 反确认
        # self.driver.find_element_by_link_text("反确认").click()
        # sleep(1)
        # self.driver.find_element_by_xpath('//*[text()="你确定要反确认选中的单据?"]/../div/a/span/span').click()
        # sleep(1)

        # 删除结算单
        # self.driver.find_element_by_xpath('//*[@id="datagrid-row-r16-1-0"]').click()
        self.driver.find_element_by_link_text("删除").click()
        self.driver.find_element_by_xpath('//*[text()="你选中了1条单据，确定要删除?"]/../div/a/span/span').click()
        sleep(1)

        # 新增结算单
        self.driver.find_element_by_link_text("新增").click()
        sleep(1)
        self.driver.find_element_by_link_text("新增").click()
        sleep(1)
        # 结算单新增选公司
        self.driver.find_element_by_xpath('//*[@name="salerName"]/../input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@name="salerName"]/../input').send_keys(saleno)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div').click()

        # 结算单新增选客户
        self.driver.find_element_by_xpath('//*[@name="buyerName"]/../input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@name="buyerName"]/../input').send_keys(buyerno)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[1]/div').click()

        # 结算单新增选品牌
        self.driver.find_element_by_xpath('//*[@name="brandUnitName"]/../input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@name="brandUnitName"]/../input').send_keys(brandno)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[1]/div').click()

        # 结算单新增选大类
        self.driver.find_element_by_xpath('//*[@name="categoryName"]/../input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@name="categoryName"]/../input').send_keys(categoryno)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r4-2-0"]/td[1]/div').click()

        # 输入起始日期
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').clear()
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').click()
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').send_keys(startdate)

        # 输入结束日期
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').clear()
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').click()
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').send_keys(enddate)

        # 输入结算单日期
        self.driver.find_element_by_xpath('//input[@id="balanceDate"]').clear()
        self.driver.find_element_by_xpath('//input[@id="balanceDate"]').click()
        self.driver.find_element_by_xpath('//input[@id="balanceDate"]').send_keys(enddate)

        # 保存结算单
        self.driver.find_element_by_link_text("保存").click()
        self.driver.implicitly_wait(3)
        # 删除结算单
        self.driver.find_element_by_xpath('//*[text()="删除"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[text()="确定"]').click()

        # 点击选单
        self.driver.find_element_by_xpath('//*[text()="选单"]').click()
        sleep(1)

        # 跳转到第三个frame
        f3 = self.driver.find_element_by_xpath('//div[@class="panel"]/div/iframe')
        self.driver.switch_to.frame(f3)

        # 选单选择公司
        self.driver.find_element_by_xpath('//input[@name="salerNo"]/../span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//input[@name="salerNo"]/../span/input').send_keys(saleno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div').click()

        # 选单选择客户
        self.driver.find_element_by_xpath('//input[@name="buyerNo"]/../span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//input[@name="buyerNo"]/../span/input').send_keys(buyerno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[1]/div').click()

        # 选单选择品牌
        self.driver.find_element_by_xpath('//input[@name="multiBrandUnitNo"]/../span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//input[@name="multiBrandUnitNo"]/../span/input').send_keys(brandno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r4-2-0"]/td[1]/div').click()

        # 选单选择大类
        self.driver.find_element_by_xpath('//input[@name="categoryNo"]/../span/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//input[@name="categoryNo"]/../span/input').send_keys(categoryno)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[1]/div').click()

        # 输入起始日期
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').clear()
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').click()
        self.driver.find_element_by_xpath('//input[@id="balanceStartDate"]').send_keys(startdate)

        # 输入结束日期
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').clear()
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').click()
        self.driver.find_element_by_xpath('//input[@id="balanceEndDate"]').send_keys(enddate)

        # 输入结算单日期
        self.driver.find_element_by_xpath('//input[@id="balanceDate"]').clear()
        self.driver.find_element_by_xpath('//input[@id="balanceDate"]').click()
        self.driver.find_element_by_xpath('//input[@id="balanceDate"]').send_keys(enddate)

        # 加载明细
        self.driver.find_element_by_xpath('//*[text()="加载明细"]').click()
        self.driver.implicitly_wait(5)

        # 选定明细
        btn_div = self.driver.find_element_by_xpath('//*[@type="checkbox"]')
        sleep(2)
        btn_div.click()
        sleep(1)

        # 跳回第二个frame
        self.driver.switch_to.default_content()
        # f2 = self.driver.find_element_by_xpath('//*[@id="mainTabs"]/div[2]/div[3]/div/iframe')
        self.driver.switch_to.frame(f2)

        # 生成选单结算单
        self.driver.find_element_by_xpath('//*[text()="生成结算单"]').click()
        self.driver.implicitly_wait(5)

        # 删除结算单
        self.driver.find_element_by_xpath('//*[text()="删除"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[text()="确定"]').click()

        # 点击结算单浏览
        self.driver.find_element_by_xpath('//*[@id="top_btn_add"]/span').click()
        sleep(1)

        # 总部财务确认结算单
        #self.driver.find_element_by_xpath('//*[text()="确认"]').click()
        #sleep(1)
        #self.driver.find_element_by_xpath('//*[text()="确定"]').click()


if __name__ == "__main__":
    unittest.main()

