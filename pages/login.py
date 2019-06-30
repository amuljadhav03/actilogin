from selenium import webdriver
class loginpage:
    def login(self):
        driver = webdriver.Chrome(executable_path="C:/Users/AMUL JADHAV/PycharmProjects/actilogin/drivers/chromedriver.exe")
        driver.get("https://demo.actitime.com/")
        driver.implicitly_wait(30)
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_xpath('//input[@name="pwd"]').send_keys("manager")
        driver.find_element_by_id("loginButton").click()
        driver.find_element_by_xpath('//a[@id="logoutLink"]').click()