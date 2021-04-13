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

while(True):
    print("Selecione qual é seu navegador")
    print("1 - Google Chrome")
    print("2 - Microsoft Edge")
    navegador = input(">> ")


    if navegador == 1:
        driver = webdriver.Chrome(executable_path=r"C:\Users\lukss\Desktop\bot_mtc\chromedriver.exe")

    if navegador == 2:
        options = EdgeOptions()
        options.use_chromium = True
        options.binary_location = r"C:\Users\lukss\Desktop\bot_mtc\msedgedriver.exe"

        driver = Edge(options = options)

        
    sleep(3)


    cont = 0
    x = 1
    y = 1


    while(True):

        link = input("Cole aqui o link da sua pesquisa no Google Scholar").split("q=")
        
        print(link)
        

        driver.get("https://scholar.google.com.br/scholar?start={}&q={}".format(cont,link))
        
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