from random import sample
print(f'''{'=-'*20}  
{'GERADOR DE APOSTAS':^40}
{'=-'*20}''')
qnt = int(input( 'quantos jogos vc deseja sortear? ' ))
print(f'''{'##'*20} 
RESULTADOS:''')

for a in range(0,qnt):
	jogo = sample(range(1,61), 6)
	print ('•',jogo)
	
print('BOA SORTE!')
