#importa as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import wget
import time

#cria uma variavel para o chrome
driver = webdriver.Chrome()

#url do site ultilizado
url = "https://www.amazon.com.br/s?i=wine&rh=n%3A19778030011%2Cp_36%3A17270755011&s=popularity-rank&content-id=amzn1.sym.26bd5128-332b-47ca-8212-4c68076b5e6f&pd_rd_r=8843be3e-923a-4a4e-8d2d-0158220c89cf&pd_rd_w=4MKTp&pd_rd_wg=b2pkF&pf_rd_p=26bd5128-332b-47ca-8212-4c68076b5e6f&pf_rd_r=QGYEHF9WPBX8BD2J27WY&ref=Oct_d_oup_S"

table = pd.DataFrame(columns=['Codigo','Nome','Preco','Img'])

driver.get(url)

#criando uma lista com todos os produtos da pagina, que tenham o css especifico 
produtos = driver.find_elements(By.CSS_SELECTOR, "h2 a.a-link-normal")

#variavel contadora para a contagem de imagens
cont = 0

#for para entrar em cada produto da lista
for cafe in produtos :
    link = cafe.get_attribute('href') #pegando o link do produto
    driver.execute_script("window.open(arguments[0]);", link) #abrindo o link em uma nova guia
    driver.switch_to.window(driver.window_handles[-1])

    nome = driver.find_element(By.ID,'productTitle') #pegando as variaveis do produto
    precoInt = driver.find_element(By.CLASS_NAME,'a-price-whole')
    precoDec = driver.find_element(By.CLASS_NAME,'a-price-fraction')

    Image = driver.find_element(By.ID, "landingImage") #pegando a imagem do produto
    urlOrigem = Image.get_attribute('src') #buscando o link da imagem para realizar o download
    extensao = urlOrigem.split(".")[-1] #vendo qual a extensao da imagem
    urlDestino = "Trabalho\\img\\" + str(cont) + "." + extensao #onde a imagem vai ser salva e qual seu nome
    wget.download(urlOrigem, urlDestino)
    
    print(nome.text)
    preco = (f"{precoInt.text},{precoDec.text}")#juntando o preco inteiro e o decimal
    
    cont += 1 # id dos produtos
    table.loc[cont-1] = [cont,nome.text,preco,urlDestino] #colocando as variaveis na tabela

    time.sleep(5)
    driver.close() #fechando a guia e abrindo a anterior, dos produtos normais
    driver.switch_to.window(driver.window_handles[0])

table.to_excel('cafes.xlsx', index=False) # transformando a tabela em .xlsx

input("Digite algo para terminar")


# for caf in produtos:
#         link = caf.get_attribute('href')
#         driver.execute_script("window.open(arguments[0]);", link)
#         driver.switch_to.window(driver.window_handles[-1])
#         time.sleep(2)
#         nome = driver.find_element(By.ID,'productTitle')
#         precoInt = driver.find_element(By.CLASS_NAME,'a-price-whole')
#         precoDec = driver.find_element(By.CLASS_NAME,'a-price-fraction')
#         print(nome.text)
#         print(f"{precoInt.text},{precoDec.text}")
#         driver.get(url)
#         time.sleep(1)
# input('Digite algo para fechar o navegador')
