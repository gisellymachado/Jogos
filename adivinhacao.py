print('******************************')
print('******Jogo da adivinhação*****')
print('******************************')

numero_secreto = 42
total_de_pontos = 1000
nivel = [1, 2, 3]
print('Nível 1 (20 tentativas) \nNível 2 (10 tentativas) \nNível 3 (5 tentativas)')

for nivel_escolhido in nivel:
	nivel_escolhido = int(input('Digite o número do nível: '))
	if nivel_escolhido in nivel:
		print('O nível {} foi escolhido.'.format(nivel_escolhido))
		print('Pontuação inicial: {}.'.format(total_de_pontos))
		break
	else:
		print('Esse nível não é válido.')

nivel1 = nivel_escolhido == 1
nivel2 = nivel_escolhido == 2
nivel3 = nivel_escolhido == 3

if(nivel1):
	total_de_tentativas = 20
elif(nivel2):
	total_de_tentativas = 10
elif(nivel3):
	total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
	print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

	chute = int(input("Digite um número: "))
	print('Você digitou: {}'.format(chute))

	acertou = chute == numero_secreto
	maior = chute > numero_secreto
	menor = chute < numero_secreto

	if(acertou):
		print('Você acertou!')
		pontuacao_final = total_de_pontos - ((total_de_pontos / total_de_tentativas) * (rodada - 1))
		print('Sua pontuação final foi de: {}'.format(pontuacao_final))
		break
	elif(maior):
		print('Você errou! O seu chute foi maior que o número secreto.')
		pontuacao_atual = total_de_pontos - ((total_de_pontos / total_de_tentativas) * rodada)
		if(rodada < total_de_tentativas):		
			print('Sua pontuação atual é: {}.'.format(pontuacao_atual))
		else: 
			print('Sua pontuação final foi de: {}'.format(pontuacao_atual))
	elif(menor):
		print('Você errou! O seu chute foi menor que o número secreto.')
		pontuacao_atual = total_de_pontos - ((total_de_pontos / total_de_tentativas) * rodada)
		if(rodada < total_de_tentativas):		
			print('Sua pontuação atual é: {}.'.format(pontuacao_atual))
		else: 
			print('Sua pontuação final foi de: {}'.format(pontuacao_atual))

print('******************************')
print('**********Fim do Jogo*********')
print('******************************')