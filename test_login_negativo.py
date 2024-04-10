import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Usuarios():

    url = "https://www.giulianaflores.com.br"

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_login_negative(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
        assert self.driver.find_element(By.CLASS_NAME, "titulo-dept").text == "IDENTIFICAÇÃO"
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("carlos_eduardo_depaula@siemens.com")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("abcde123")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        self.driver.find_element(By.CLASS_NAME, "font_erro").text == 'e-mail ou senha inválidos!'