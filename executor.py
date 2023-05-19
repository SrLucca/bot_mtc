from selenium import webdriver
from openpyxl import Workbook
from time import sleep
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def codigo(link,navegador):
    
    


    cont = 0
    x = 0
    y = 0

    split = link.split('q=')
    print(split)
    print(navegador)


    
    if navegador == 2:


        driver = webdriver.Edge()
        driver.maximize_window()
        #print(link)
        driver.get(f"https://scholar.google.com.br/scholar?start=0&q={split[1]}")


        root = os.getcwd()

        
        wait = WebDriverWait(driver, 10)

        wb = Workbook()


        planilha = wb.worksheets[0]

        while(True):
            
            try:
                os.mkdir('planilhas')
            except FileExistsError:
                os.chdir(f'{root}\\planilhas')

                items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.gs_rt a')))

                for item in items:

                    x += 1
                    y += 1

                    open_planilha = wb.worksheets.append(object)

                    nome_artigo = item.text
                    link_artigo = item.get_attribute('href')
                    print('Artigo: ',nome_artigo,'\nLink: ', link_artigo,'\n')
                    planilha[f'A{x}'] = nome_artigo
                    planilha[f'B{y}'] = link_artigo
                    
                    
                
                botao = driver.find_element(by=By.PARTIAL_LINK_TEXT , value=f"Mais")
                botao.click()
                wb.save("planilha.xlsx")
                
                

            
    
    return