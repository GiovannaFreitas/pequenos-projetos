''' Simular o uso de um dad0 gerando valores aleatórios de 1 até 6 '''

import random
import PySimpleGUI as sg

class Simulador:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de jogar o dado? '
        self.layout = [
            [sg.Text('Quer jogar o dado? ')],
            [sg.Button('SIM'), sg.Button('NÃO')]
        ]

    def Iniciar(self):
        self.janela = sg.Window('Simulador de dado',layout=self.layout)
        self.eventos, self.valores = self.janela.Read()
        
        try:
            if self.eventos == 'SIM' or self.eventos == 'S':
                self.Valordodado()

            elif self.eventos == 'NÃO' or self.eventos == 'N':
                print('Ok, sem problemas')

            else:
                print('Por favor, digite SIM ou NÃO')
        except:
            print('Ocorreu um erro ao receber a sua resposta')
        
    def Valordodado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        

simulador = Simulador()
simulador.Iniciar()


