import random
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        # layout
        sg.theme('Material2')
        layout = [
            [sg.text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.text('E-mail/Usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)),key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar senha')]
        ]
    
        # Declarar a janela
        
    def Iniciar(self):
        pass
    def salvar_senha(self):
        pass





gen = PassGen()
gen.Iniciar()