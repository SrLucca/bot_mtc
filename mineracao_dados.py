from selenium import webdriver
from executor import codigo
from msedge.selenium_tools import EdgeOptions, Edge
#OPENPYXL


#SELENIUM

#COLOCAR O DRIVER DA VERSAO DO MEU NAVEGADOR


print("Selecione qual é seu navegador")
print("1 - Google Chrome")
print("2 - Microsoft Edge")
navegador = int(input(">> "))


if navegador == 1:
    driver = webdriver.Chrome(executable_path=r"C:\Users\lukss\Documents\GitHub\bot_mtc\chromedriver.exe")
    codigo(driver)

if navegador == 2:
    options = EdgeOptions()
    options.use_chromium = True
    options.binary_location = r"C:\Users\lukss\Documents\GitHub\bot_mtc\msedgedriver.exe"

    driver = Edge(options = options)
    codigo(driver)

        