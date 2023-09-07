from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.google.com.br/?hl=pt-BR')
pesquisa = navegador.find_element(By.NAME, "q")  

pesquisa.send_keys('letra de ado binkusuno sake', Keys.ENTER)

pesquisa = navegador.find_element(By.XPATH, '//*[@id="kp-wp-tab-default_tab:kc:/music/recording_cluster:lyrics"]/div[1]/div/div')

texto_copiado = pesquisa.text

print(texto_copiado)
