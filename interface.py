import PySimpleGUI as sg
import os
from PySimpleGUI.PySimpleGUI import Image
from executor import codigo

sg.theme('DarkAmber')

layout = [
    [sg.Text('Minarador Google Scholar')],
    [sg.Text('Insira o link da pesquina na pagina 1')],
    [sg.Text('Qual Navegador você usará?')],
    [sg.Button('Google Chrome')],
    [sg.Button('Microsoft Edge')],
    [sg.Button('Sair')],
    
]

window = sg.Window('Minerador Google Scholar', layout, size=(400,300))

while(True):
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    

window.close()

