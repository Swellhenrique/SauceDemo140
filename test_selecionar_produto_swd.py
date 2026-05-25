#  1 - bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - classe (Opcional)
class Test_Produtos(): 

# 2.1 Atributos
  url = "https://www.saucedemo.com"                                                  # endereço do site alvo 

# 2.2 Funções e Métodos
  def setup_method(self,method):                                                     # método de inicialização do teste
    self.driver = webdriver.Chrome()                                                 # instancia o objeto do Selenium WebDriver como Chrome 
    self.driver.implicitly_wait(10)                                                  # define o tempo de espera padrão por encontrar elementos em 10 segundos
   
  def teardown_method(self, method):                                                 # método de finalização do testes
   self.driver.quit()                                                                # encerra / destroi o objeto do selenium WebDriver da memória
    
  def test_selecionar_produto(self):                                                 # método de teste
    self.driver.get(self.url)                                                        # abre o navegador 
    self.driver.find_element(By.ID,"user-name").send_keys("standard_user")           # localiza o campo de nome de usuário e insere o valor "standard_user" 
    self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")           # localiza o campo de senha e insere o valor "secret_sauce"



    