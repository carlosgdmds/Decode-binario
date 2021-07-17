arquivo = open("arquivo.txt",'r')
n = 0
frase = []
linha = []
soma = 0
listaLetras = []
listaLetrasChar = []

def decToChar(decimal):
	listaLetrasChar.append(chr(decimal))

def decode(frase):
	global soma
	#print("Here 3 ")
	for i, letra in enumerate(frase):
		multi = (2**i)
		resultado = int(letra) * multi
		soma +=resultado
	listaLetras.append(soma)
	soma = 0

for linha in arquivo:
	for letra in linha.strip():
		if n >= 8:
			n = 0
			decode(list(reversed(frase)))
			frase = []
		frase.append(letra)
		n+=1
for decimal in listaLetras:
	decToChar(decimal)

fraseFinal = ""
for letra in listaLetrasChar:
	fraseFinal = fraseFinal + letra

print(fraseFinal)
