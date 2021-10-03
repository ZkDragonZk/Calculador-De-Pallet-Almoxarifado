from time import sleep
from colorama import Fore, init
init(convert=True)

print(f''' 

============= PAINEL DE LOGIN =============

sistema para calcular o pesos dos pallet.

criado por mim: ZkDragonZk , Estudante De TI

===========================================

''')

print('')
lastro = int(input('Digite o lastro: '))
print('')
altura = int(input('Digite a altra: '))
print('')
pesokg = int(input('Digite o Peso de 1 caixa: '))
print('')
resultado = (lastro * altura) * pesokg
print(f'{Fore.RED}O Pallet Pesa No Total:' ' {} Kg'.format(resultado))
sleep(40)