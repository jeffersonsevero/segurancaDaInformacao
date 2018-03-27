from itertools import permutations




textoCriptografado = 'mllvo gjw axie, viog vlgbg dfptll n zoe fe gyyom j xof nr tuegr fg tfusfe ayqwxt rrpjnfy xg, mlm nbnju, tphuc kzg fltrf i ytamuyvi ig pzi qs or rrzzrgmtt spg acwfq, ux nnz xj eiqln ry akgphrfy'

alfabeto = 'abcdefghijklmnopqrstuvxz'


# Tamanho do textoCifrado = 150



def tirarEspacosFacil(texto):
    vetor = []
    textoSemEspaco = texto.replace(" ", "").replace(",", "")
    for letra in textoSemEspaco:
        vetor.append(letra)
    return vetor


def deixarChaveComMesmoTamanhoTexto(chave):
    novaChave = []
    a = chave * 19
    for letra in a:
        novaChave.append(letra)
    del novaChave[-1]
    del novaChave[-1]


    return novaChave



def fatiarTextoFacil(texto):
    fatias = []



    for i in range(8):
        fatias.append(texto[i::8])

    return fatias


def decrypt(ciphertext, key):
    keyLong = deixarChaveComMesmoTamanhoTexto(key)
    key_length = len(key)
    key_as_int = [ord(i) for i in keyLong]
    ciphertextInt = [ord(i) for i in ciphertext]

    #print(ciphertextInt)

    plainText = ''

    for i in range(len(ciphertextInt)):
        value = (ciphertextInt[i] - key_as_int[i % key_length]) % 26
        plainText += chr(value + 65)

    return plainText


def bruteForce(alfabeto, tamanhoDaChave):

    for combinacao in permutations(alfabeto, tamanhoDaChave):
        frases = decrypt(tirarEspacosFacil(textoCriptografado), combinacao)

        print(frases)

    for frase in frases:
        if 'AMOR' in frase:
            break
        print(combinacao)



bruteForce(alfabeto, 8)





