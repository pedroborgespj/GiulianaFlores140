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

    def test_cadastrar_usuario(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
        assert self.driver.find_element(By.CLASS_NAME, "titulo-dept").text == "IDENTIFICAÇÃO"
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
        assert self.driver.find_element(By.CLASS_NAME, "titulo-dept").text == "MINHA CONTA"
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Carlos Eduardo Francisco Francisco de Paula")
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("283.277.770-84")
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("carlos_eduardo_depaula@siemens.com")
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("yuhi3Lczgs")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("57041-417")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("679")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("47984751009")
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#lblWelcome > b").text == "Carlos"