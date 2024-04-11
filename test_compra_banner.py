import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Usuarios():

    url = "https://www.giulianaflores.com.br"

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_buy_from_banner(self):
        self.driver.get(self.url)
        assert self.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(1) .title-item").text == "Dupla de Orquídeas Amarelas para Presente"
        assert self.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(1) .actual-price").text == "R$ 149,90"
        self.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(1) .title-item").click()
        assert self.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == "DUPLA DE ORQUÍDEAS AMARELAS PARA PRESENTE"
        assert self.driver.find_element(By.CLASS_NAME, "precoPor_prod").text == "R$ 149,90"
        self.driver.find_element(By.ID, "ContentSite_txtZip").send_keys("02177-060")
        self.driver.find_element(By.CSS_SELECTOR, ".jOpenShippingPopup").click()
        time.sleep(2) # foi necessário colocar para o teste rodar
        self.driver.find_element(By.CSS_SELECTOR, ".jConfirmShippingData").click()
        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".title-defaut-interna").text == "MEU CARRINHO"
        assert self.driver.find_element(By.CSS_SELECTOR, ".prodBasket_nome > a").text == "Dupla de Orquídeas Amarelas para Presente"
        assert self.driver.find_element(By.CLASS_NAME, "precoPor_basket").text == "R$ 149,90"
        self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click()
        ## finalizando o teste na etapa de login