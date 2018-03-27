def gerar_Matriz(chave):
	mat = []
	for e in chave:
		if e not in mat:
			mat.append(e)

	alfabeto = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

	for i in alfabeto:
		if i not in mat:
			mat.append(i)

	new_matriz = [[], [], [], [], []]

	new_matriz[0] = mat[0:5]
	new_matriz[1] = mat[5:10]
	new_matriz[2] = mat[10:15]  # adicionando as linhas em new_matriz
	new_matriz[3] = mat[15:20]
	new_matriz[4] = mat[20:25]

	return new_matriz


def formatarTexto(mensagem):  # tira espaços, adiciona x em letras repetidas e adiciona x caso alguma letra fique sozinha no final
	vet = []
	for i in mensagem:
		vet.append(i)
	for e in vet:
		if e == ' ':
			vet.remove(e)
	for i in range(len(vet) - 1):
		if vet[i] == vet[i + 1]:
			vet.insert(i + 1, 'X')

	if len(vet) % 2 != 0:
		vet.append('X')

	return vet


def separarEmDuplas(vet):
	duplas = []
	for i in range(len(vet)//2):
		i = i + i
		duplas.append((vet[i],vet[i + 1]))
	return duplas

def pegaLinhaEColuna(matriz, letra):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] == letra:
				return i,j

def pega_letra(matriz, linha, coluna):
	return matriz[linha][coluna]


def cifrar(matriz, letra1, letra2):
	letra_1_linha, letra_1_coluna = pegaLinhaEColuna(matriz, letra1)
	letra_2_linha ,letra_2_coluna = pegaLinhaEColuna(matriz, letra2)

	if letra_1_linha == letra_2_linha:
		letra1_criptografada = pega_letra(matriz, letra_1_linha, (letra_1_coluna + 1) % 5)
		letra2_criptografada = pega_letra(matriz, letra_2_linha, (letra_2_coluna + 1) % 5)

		return letra1_criptografada, letra2_criptografada

	if letra_1_coluna == letra_2_coluna:
		letra1_criptografada = pega_letra(matriz, (letra_1_linha + 1) % 5, letra_1_coluna)
		letra2_criptografada = pega_letra(matriz, (letra_2_linha + 1) % 5, letra_2_coluna )

		return letra1_criptografada, letra2_criptografada
	else:
		letra1_criptografada = pega_letra(matriz, letra_1_linha, letra_2_coluna % 5)
		letra2_criptografada = pega_letra(matriz, letra_2_linha, letra_1_coluna % 5)

		return letra1_criptografada, letra2_criptografada

def decifrar(matriz, letra1, letra2):
	letra_1_linha, letra_1_coluna = pegaLinhaEColuna(matriz, letra1)
	letra_2_linha, letra_2_coluna = pegaLinhaEColuna(matriz, letra2)

	if letra_1_linha == letra_2_linha:
		letra1_criptografada = pega_letra(matriz, letra_1_linha, letra_1_coluna - 1 % 5 )
		letra2_criptografada = pega_letra(matriz, letra_2_linha, letra_2_coluna - 1 % 5)

		return letra1_criptografada, letra2_criptografada

	if letra_1_coluna == letra_2_coluna:
		letra1_criptografada = pega_letra(matriz, letra_1_linha - 1 % 5, letra_1_coluna)
		letra2_criptografada = pega_letra(matriz, letra_2_linha - 1 % 5, letra_2_coluna )

		return letra1_criptografada, letra2_criptografada
	else:
		letra1_criptografada = pega_letra(matriz, letra_1_linha, letra_2_coluna % 5)
		letra2_criptografada = pega_letra(matriz, letra_2_linha, letra_1_coluna % 5)

		return letra1_criptografada, letra2_criptografada


def imprime_duplas(duplas):
	for letra1, letra2 in duplas:
		print (letra1, letra2),



chave = 'NUMABOA'

matriz = gerar_Matriz(chave)
for linha in matriz:
	print (linha, "\n")

mensagem = 'ESSE NEGOCIO DEU MUITO TRABALHO'

duplas = separarEmDuplas(formatarTexto(mensagem))

duplas_cifradas = []
for letra1, letra2 in duplas:
	letra1_crip, letra2_crip = cifrar(matriz, letra1, letra2)
	duplas_cifradas.append([letra1_crip, letra2_crip])

imprime_duplas(duplas)
print('\n')
imprime_duplas(duplas_cifradas)

duplas_decifradas = []
for letra1, letra2 in duplas_cifradas:
	letra1_crip, letra2_crip = decifrar(matriz, letra1, letra2)
	duplas_decifradas.append([letra1_crip, letra2_crip])

print('\n')

imprime_duplas(duplas_cifradas)
print('\n')
imprime_duplas(duplas_decifradas)



S
