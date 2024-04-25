import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    # Passo em si
    context.driver.get("https://www.giulianaflores.com.br/")

@when(u'acesso a pagina de cadastro')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    assert context.driver.find_element(By.CLASS_NAME, "titulo-dept").text == "IDENTIFICAÇÃO"
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    assert context.driver.find_element(By.CLASS_NAME, "titulo-dept").text == "MINHA CONTA"

@when(u'acesso a pagina de login')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    assert context.driver.find_element(By.CLASS_NAME, "titulo-dept").text == "IDENTIFICAÇÃO"

@when(u'preencho os campos de cadastro com nome completo {nome} e cpf {cpf} e email {email} e senha {senha} e cep {cep} e numero do endereco {numeroEnd} e numero de telefone {tel}')
def step_impl(context, nome, cpf, email, senha, cep, numeroEnd, tel):
    context.driver.find_element(By.ID, "ContentSite_txtName").send_keys(nome)
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys(cpf)
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(email)
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys(senha)
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys(cep)
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys(numeroEnd)
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys(tel)
    context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()

@when(u'preencho os campos de email {email} e senha {senha}')
def step_impl(context, email, senha):
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(email)
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(senha)
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()

@when(u'preencho os campos de email  e senha {senha}')
def step_impl(context, senha):
    # não preenche usuário
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(senha)
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()

@when(u'coloco o primeiro item do banner no carrinho')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(1) .title-item").click()
    assert context.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == "MARAVILHOSAS ORQUÍDEAS"
    assert context.driver.find_element(By.CLASS_NAME, "precoPor_prod").text == "R$ 145,90"
    context.driver.find_element(By.ID, "ContentSite_txtZip").send_keys("02177-060")
    context.driver.find_element(By.CSS_SELECTOR, ".jOpenShippingPopup").click()
    time.sleep(2) # foi necessário colocar para o teste rodar
    context.driver.find_element(By.CSS_SELECTOR, ".jConfirmShippingData").click()
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()

@when(u'finalizo a compra na página do carrinho')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title-defaut-interna").text == "MEU CARRINHO"
    assert context.driver.find_element(By.CSS_SELECTOR, ".prodBasket_nome > a").text == "Maravilhosas Orquídeas"
    assert context.driver.find_element(By.CLASS_NAME, "precoPor_basket").text == "R$ 145,90"
    context.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click()

@then(u'o cadastro é realizado com sucesso para o usuario {usuario}')
def step_impl(context, usuario):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    assert context.driver.find_element(By.CSS_SELECTOR, "#lblWelcome > b").text == usuario

    context.driver.quit()

@then(u'o login do usuário {usuario} é realizado com sucesso')
def step_impl(context, usuario):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    assert context.driver.find_element(By.CSS_SELECTOR, "#lblWelcome > b").text == usuario

    context.driver.quit()

@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CLASS_NAME, "font_erro").text == mensagem

    context.driver.quit()

@then(u'sou direcionado para a página de login')
def step_impl(context):
    time.sleep(2) # foi necessário colocar para o teste rodar
    assert context.driver.find_element(By.CLASS_NAME, "titulo-dept").text == "IDENTIFICAÇÃO"

    context.driver.quit()