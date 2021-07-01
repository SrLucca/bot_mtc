import PySimpleGUI as sg
import os
from PySimpleGUI.PySimpleGUI import Image
from foda import enviar

sg.theme('DarkAmber')

layout = [
    [sg.Text('O Venture Ama o Santos')],
    [sg.Text('Mande uma mensagem para João')],
    [sg.InputText(size=(50,12))],
    [sg.Image(r'C:\Users\lukss\Documents\GitHub\bot_mtc\venture.png', size=(600,600))],
    [sg.Button('Enviar'), sg.Button('Cancelar')],
    [sg.Output(size=(40,10))],
]

window = sg.Window('Mensagem Para João', layout)

while(True):
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    
    enviar(values[0])
    print(values[0])

    
window.close()

