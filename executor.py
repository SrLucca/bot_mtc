from selenium import webdriver
from openpyxl import Workbook
from msedge.selenium_tools import EdgeOptions, Edge
from time import sleep

def codigo(link,navegador):
    
    wb = Workbook()


    planilha = wb.worksheets[0]
    
    sleep(3)


    cont = 0
    x = 1
    y = 1




    if navegador == 2:
        options = EdgeOptions()
        options.use_chromium = True

        driver = Edge(options = options)
        #print(link)


        driver.get("https://scholar.google.com.br/scholar?start=0&q={}".format(link[1]))
        
        while(True):
            botao = driver.find_element_by_partial_link_text('Mais')
            botao.click()
            


        #for a in driver.find_elements_by_xpath('.//a'):
            
            
            #nome = a.get_attribute('text')
            #link = a.get_attribute('href')

            #planilha['A{}'.format(x)] = nome
            #planilha['B{}'.format(y)] = link
            #x += 1
            #y += 1



            #print(nome)
            #print(link)

            #wb.save(r"C:\Users\lukss\Desktop\bot_mtc\Teste_10.xlsx")
    
    return