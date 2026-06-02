#  1 - bibliotecas / imports 
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # setup / inicialização 
    context.driver = webdriver.Chrome()                                          # instancia o objeto do Selenium WebDriver especializado para o navegador Chrome 
    context.driver.maximize_window()                                                           # maximiza a janela do navegador
    context.driver.implicitly_wait(10)                                                        # tempo de espera padrão por encontrar elementos em 10 segundos
    # Passo em si
    context.driver.get("https://www.saucedemo.com")                                                # abre o navegador e acessa o endereço do site alvo


@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)     # preencher o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)        # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()             # clicar no botão de login


@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"                     # confirma se esta escrito products no elemento
   # time.sleep(2)                                                                                       # espera 2 segundos  - remover depois

    # teardown / finalização
    context.driver.quit()                                                                # encerra / destroi o objeto do selenium WebDriver da memória


  
