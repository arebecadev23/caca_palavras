caca_palavra = ["SISTEMASOPERACIONAPPR",
                "RDDFVIGMEMORIARAMGAOA",
                "WARLLESRTYUIOOPNBVPAQ",
                "REBECAJWBFHWJBFHFHAUL"]


largura = len(caca_palavra[0])  # para pegar a largura das palavras
altura = len(caca_palavra)
# Cabeçalho dos números
print("   ", end="")
for i in range(1, largura + 1):
    print(str(i).rjust(2), end=" ") #.rjust(2) vai criar um espaço d caracteres e alinhar 
print()

# Linha separadora
print("   " + "---" * largura)

# Linhas do caça-palavras
for i, linha in enumerate(caca_palavra, start=1): #enumera as linhas 
    print(str(i).rjust(2) + "- ", end="") #rjust 
    for letra in linha:
        print(letra.rjust(2), end=" ") #vou dar dois espaços para cada letra
    print()

#entradada de dados 
#BUSCA AS PALAVRAS DENTRO DO QUE JÁ EXISTE
palavra = input("Digite uma palavra: ")
palavra = palavra.upper() #busca usando letras MAISUCULAS
palavra_invertida =  palavra[::-1] #buscar de forma inversa a palavra antes digitada
print("Palavra ser procurada: ", palavra)
#Transpor a matriz 
caca_palavra_t = []
for i in range(largura):
    s = ""
    for j in range(altura):
        s += caca_palavra[j][i]
    caca_palavra_t.append(s)

encontrada = False #antes o status da palavra era falso, fazendo
#com que a palavra antes procurada e ENCONTRADA, tivesse seu ststus apagado.


for p in [palavra, palavra_invertida]: 
    #procurar na horizontal 
    direcao = "Normal"
    for linha in caca_palavra:
        if p in linha:
            print("Direção: ", direcao)
            print("Palavra encontrada!")
            print("sentido: Horizontal")
            encontrada = True
            lin = caca_palavra.index(linha)+1 
            col = linha.find(p)+1 #se eu  busco por P então devo por o P.
            print("linha: ", lin)
            print("Coluna: ", col)
    #procurar na vertical
    direcao = "inversa"
    for linha in caca_palavra_t:
        if p in linha: 
            print("Direção: ", direcao)

            print("Palavra encontrada!")
            print("sentido: Vertical")
            encontrada = True
            lin = caca_palavra.index(linha)+1 
            col = linha.find(p)+1
            print("linha: ", lin)
            print("Coluna: ", col)

if not encontrada:
    print("A palavra não foi encontrada! ")
    
