from selenium import webdriver
from executor import codigo
import os

#OPENPYXL


#SELENIUM



os.system("cls")
print("Selecione qual é seu navegador")
print("1 - Google Chrome")
print("2 - Microsoft Edge")
navegador = int(input(">> "))


if navegador == 1:
    driver = webdriver.Chrome(executable_path=r"C:\Users\lukss\Documents\GitHub\bot_mtc\chromedriver.exe")
    link = input("Cole aqui o link da sua pesquisa no Google Scholar").split("q=")
    codigo(driver)

if navegador == 2:
    
    link = input("Cole aqui o link da sua pesquisa no Google Scholar").split("q=")
    codigo(link,navegador)

        