from selenium import webdriver
from openpyxl import Workbook
from time import sleep

def codigo(driver):
    
    wb = Workbook()


    planilha = wb.worksheets[0]
    
    sleep(3)


    cont = 0
    x = 1
    y = 1


    while(True):

        link = input("Cole aqui o link da sua pesquisa no Google Scholar").split("q=")
        
        #print(link)
        

        driver.get("https://scholar.google.com.br/scholar?start={}&q={}".format(cont,link))
        
        cont += 10

        botao = driver.find_elements_by_id("gs_nm").click()


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