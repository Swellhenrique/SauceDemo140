#  1 - bibliotecas / imports 
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que entro no site Sauce Demo')
@given(u'que acesso o site Sauce Demo')
@given(u'que acesso no site Sauce Demo')
def step_impl(context):
    # setup / inicialização 
    context.driver = webdriver.Chrome()                        # instancia o objeto do Selenium WebDriver especializado para o navegador Chrome 
    context.driver.maximize_window()                           # maximiza a janela do navegador
    context.driver.implicitly_wait(10)                         # tempo de espera padrão por encontrar elementos em 10 segundos
    # Passo em si
    context.driver.get("https://www.saucedemo.com")           # abre o navegador e acessa o endereço do site alvo

# preencher com usuario e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)     # preencher o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)        # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()             # clicar no botão de login
    
# preencher com usuario em branco, mas preencher a senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
   # nao preenche o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)        # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()             # clicar no botão de login

# preencher com usuario, mas deixar senha em branco    
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)     # preencher o usuario
    # nao preenche a senha
    context.driver.find_element(By.ID, "login-button").click()             # clicar no botão de login

#clica no login sem ter preechido o usuario e a senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context,):
    # nao preencho o usuario
    # nao preencho a senha
    context.driver.find_element(By.ID, "login-button").click()             # clicar no botão de login

#preenche com usuario e senha através do (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)     # preencher o usuario
        # se o usuario estiver em <branco> nao há preenchimento
    if senha != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)        # preencher a senha
        # se a senha estiver em <branco> nao há preenchimento

    context.driver.find_element(By.ID, "login-button").click()             # clicar no botão de login

@when(u'adiciono o produto Sauce Labs Backpack no carrinho')
def step_impl(context):
    assert context.driver.find_element(By.ID, 'item_4_title_link').text == 'Sauce Labs Backpack'
    assert context.driver.find_element(By.CSS_SELECTOR, '.inventory_item:nth-child(1) .inventory_item_price').text == '$29.99'
    context.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    assert context.driver.find_element(By.ID, 'shopping_cart_container').text == '1'
    context.driver.find_element(By.CSS_SELECTOR, '*[data-test="shopping-cart-link"]').click()

@when(u'removo o produto Sauce Labs Backpack do carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, 'remove-sauce-labs-backpack').click()

@when(u'realizo o logout')
def step_impl(context):
    context.driver.find_element(By.ID, 'react-burger-menu-btn').click()
    context.driver.find_element(By.ID, 'logout_sidebar_link').click()
    

@then(u'sou direcionado para página Home')
@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, '.title').text == 'Products'                     # confirma se esta escrito products no elemento



@then(u'valido no carrinho o produto Sauce Labs Backpack com quantidade 1 e preco $29.99')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, '.title').text == 'Your Cart'
    assert context.driver.find_element(By.CSS_SELECTOR, '*[data-test="item-quantity"]').text == '1'
    assert context.driver.find_element(By.ID, 'item_4_title_link').text == 'Sauce Labs Backpack'
    assert context.driver.find_element(By.CSS_SELECTOR, '*[data-test="inventory-item-price"]').text == '$29.99'



@then(u'retorno para tela de login')
def step_impl(context):
    assert context.driver.find_element(By.ID, 'login-button').is_displayed()
    context.driver.quit()                    # encerra / destroi o objeto do selenium WebDriver da memoria


@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"
      # confirma se a mensagem de erro é exibida
    
    context.driver.quit()                          # encerra / destroi o objeto do selenium WebDriver da memória

#verifica a mensagem para o Scenario Outline 
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem
      # confirma se a mensagem de erro é exibida
    
    context.driver.quit()                          # encerra / destroi o objeto do selenium WebDriver da memória
 

