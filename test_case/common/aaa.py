from config import config_browser,config_data,config_mysql
import unittest

class My_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oncepath = config_data.once_repath()
        cls.browser = config_browser.browser_choose()

    @classmethod
    def tearDownClass(cls):
        browser = cls.browser
        browser.close()

    def test3_open(self):
        browser = self.browser
        browser.get(R'http://merchants.guxiansheng.cn/')
        browser.maximize_window()

    def test2_login(self):
        browser = self.browser
        browser.implicitly_wait(30)
        browser.find_element_by_name('username').clear()
        browser.find_element_by_name('username').send_keys('admin-wlzx')
        browser.find_element_by_name('password').clear()
        browser.find_element_by_name('password').send_keys("123456aa")
        browser.find_element_by_class_name('m-b').click()
        browser.implicitly_wait(30)

    def test1_screen(self):
        browser = self.browser
        oncepath = self.oncepath
        browser.implicitly_wait(30)
        browser.find_element_by_xpath('//*[@id="side-menu"]/li[4]/a/span[1]').click()
        browser.find_element_by_xpath('//*[@id="side-menu"]/li[4]/ul/li[1]/a').click()
        browser.implicitly_wait(30)
        browser.save_screenshot(config_data.screen_path(oncepath))

if __name__ == '__main__':
    unittest.main()