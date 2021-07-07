from selenium import webdriver
from openpyxl import Workbook
from msedge.selenium_tools import EdgeOptions, Edge
from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def codigo(link,navegador):
    
    wb = Workbook()


    planilha = wb.worksheets[0]
    
    sleep(3)


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
        root = os.getcwd()

        try:
            os.mkdir('planilhas')
        
        except FileExistsError:
            os.chdir('planilhas')

        wait = WebDriverWait(driver, 10)

        driver.get("https://scholar.google.com.br/scholar?start=0&q={}".format(split[1]))
        
        while(True):
            
            items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.gs_rt a')))
            for item in items:

                nome_artigo = item.text
                link_artigo = item.get_attribute('href')
                print('Artigo: ',nome_artigo,'\nLink: ', link_artigo,'\n')
                planilha['A{}'.format(x)] = nome_artigo
                planilha['B{}'.format(y)] = link_artigo
            
            botao = driver.find_element_by_partial_link_text('Mais')
            botao.click()
            


            
            #x += 1
            #y += 1


            
    
    return