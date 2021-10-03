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
pesokg = 25
resultado = (lastro * altura) * pesokg
print('O Pallet Pesa No Total: {}Kg '.format(resultado))