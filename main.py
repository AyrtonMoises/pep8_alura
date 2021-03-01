from fabrica_fila import FabricaFila


fila_teste = FabricaFila.pega_fila('normal')
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.estatistica('25/02/2021', 1030, 'detail'))