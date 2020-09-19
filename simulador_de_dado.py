''' Simular o uso de um dado, gerando valores aleatórios de 1 até 6 '''

import random
import PySimpleGUI as sg

class Simulador:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de jogar o dado? '
        ''' Layout, janela, valores da tela e fazer algo'''
        self.layout = [
            [sg.Text('Quer jogar o dado? ')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        self.janela = sg.Window('Simulador de dado',layout=self.layout)

        self.eventos, self.valores = self.janela.Read()
        
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.Valordodado()

            elif self.eventos == 'não' or self.eventos == 'n':
                print('Ok, sem problemas')

            else:
                print('Por favor, digite sim ou não')
        except:
            print('Ocorreu um erro ao receber a sua resposta')
        
    def Valordodado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = Simulador()
simulador.Iniciar()


