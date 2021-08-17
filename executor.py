from selenium import webdriver
from openpyxl import Workbook
from msedge.selenium_tools import EdgeOptions, Edge
from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def codigo(link,navegador):
    
    


    cont = 0
    x = 1
    y = 1

    split = link.split('q=')
    print(split)
    print(navegador)


    
    if navegador == 2:


        options = EdgeOptions()
        options.use_chromium = True

        driver = Edge(options = options)
        driver.maximize_window()
        #print(link)
        driver.get("https://scholar.google.com.br/scholar?start=0&q={}".format(split[1]))


        root = os.getcwd()

        
        wait = WebDriverWait(driver, 10)

        while(True):
            
            try:
                os.mkdir('planilhas')
            except FileExistsError:
                os.chdir(f'{root}\\planilhas')

                wb = Workbook()


                planilha = wb.worksheets[0]

                items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.gs_rt a')))

                for item in items:

                    nome_artigo = item.text
                    link_artigo = item.get_attribute('href')
                    print('Artigo: ',nome_artigo,'\nLink: ', link_artigo,'\n')
                    planilha['A{}'.format(x)] = nome_artigo
                    planilha['B{}'.format(y)] = link_artigo
                
                botao = driver.find_element_by_partial_link_text('Mais')
                botao.click()
                wb.save("planilha.xlsx")
                
                x += 1
                y += 1

            
    
    return