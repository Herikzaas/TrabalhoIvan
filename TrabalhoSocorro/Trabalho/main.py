from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import wget
import time

driver = webdriver.Chrome()

url = "https://www.amazon.com.br/s?i=wine&rh=n%3A19778030011%2Cp_36%3A17270755011&s=popularity-rank&content-id=amzn1.sym.26bd5128-332b-47ca-8212-4c68076b5e6f&pd_rd_r=8843be3e-923a-4a4e-8d2d-0158220c89cf&pd_rd_w=4MKTp&pd_rd_wg=b2pkF&pf_rd_p=26bd5128-332b-47ca-8212-4c68076b5e6f&pf_rd_r=QGYEHF9WPBX8BD2J27WY&ref=Oct_d_oup_S"

table = pd.DataFrame(columns=['Codigo','Nome','Preco','Img'])

driver.get(url)

produtos = driver.find_elements(By.CSS_SELECTOR, "h2 a.a-link-normal")

for cafe in produtos :
    link = cafe.get_attribute('href')
    driver.execute_script("window.open(arguments[0]);", link)
    driver.switch_to.window(driver.window_handles[-1])

    nome = driver.find_element(By.ID,'productTitle')
    precoInt = driver.find_element(By.CLASS_NAME,'a-price-whole')
    precoDec = driver.find_element(By.CLASS_NAME,'a-price-fraction')
    img = driver.find_element(By.ID, 'imgTagWrapperId')
    print(img)
    urlImg = img.get_attribute('src')
    extensao = urlImg.split(".")[-1]
    urlDestino = "Trabalho\\img\\" + id + "." + extensao

    wget.download(urlImg, urlDestino)

    print(nome.text)
    print(f"{precoInt.text},{precoDec.text}")


    
    time.sleep(5)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


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
