from fila_prioritaria import FilaPrioritaria

fila_teste = FilaPrioritaria()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))

print(fila_teste.estatistica('25/02/2021', 1030, 'detail'))
print(fila_teste.estatistica('25/02/2021', 1030, ''))