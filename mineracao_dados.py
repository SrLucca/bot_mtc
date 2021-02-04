from selenium import webdriver
from openpyxl import Workbook
from time import sleep

#OPENPYXL


wb = Workbook()


planilha = wb.worksheets[0]

#SELENIUM



#div = driver.find_element_by_class_name('gs_rt')

#elementos = div.find_elements_by_tag_name('a')
#for links in elementos:
    #print(links.text)

driver = webdriver.Chrome(executable_path=r"C:\Users\lukss\Desktop\bot_mtc\chromedriver.exe")

sleep(3)


cont = 0
x = 1
y = 1




while(True):
        
    driver.get("https://scholar.google.com.br/scholar?start={}&q=%22Chatbot%22+AND+%22com%C3%A9rcio+eletr%C3%B4nico%22&hl=pt-BR&as_sdt=0,5&as_ylo=2019&as_yhi=2021".format(cont))
    
    cont += 10

    for a in driver.find_elements_by_xpath('.//a'):
        
        
        nome = a.get_attribute('text')
        link = a.get_attribute('href')

        planilha['A{}'.format(x)] = nome
        planilha['B{}'.format(y)] = link
        x += 1
        y += 1



        print(nome)
        print(link)

        wb.save(r"C:\Users\lukss\Desktop\bot_mtc\Teste_10.xlsx")


        
                                                    
