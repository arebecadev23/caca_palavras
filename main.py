caca_palavra = ["SISTEMASOPERACIONAPPR",
                 "RDDFVIGMEMORIARAMGAOA",
                 "WARLLESRTYUIOOPNBVPAQ",
                 "REBECAJWBFHWJBFHFHAUL"]
direcoes = [
    (0,1, "Horizontal direita"),
    (0, -1, "Horizontal esquerda"),
    ( 1,0, "Vertical para baixo"),
    (-1,0, "Vertical para cima")
]

#vai medir as colunas e a largura
def mostrar_tabuleiro(caca_palavra, largura):

#direções para calculo
# # Cabeçalho dos números
    print("   ", end="")
    for i in range(1, largura + 1):
        print(str(i).rjust(2), end=" ") #.rjust(2) vai criar um espaço d caracteres e alinhar 
    print() #####fghj

# # Linha separadora
    print("   " + "---" * largura)

# # Linhas do caça-palavras
    for i, linha in enumerate(caca_palavra, start=1): #enumera as linhas 
        print(str(i).rjust(2) + "- ", end="") #rjust 
        for letra in linha:
            print(letra.rjust(2), end=" ") #vou dar dois espaços para cada letra
        print()

def buscar_palavra(caca_palavra, direcoes):

    palavra = input("Digite a palavra: ").upper()
    altura = len(caca_palavra)
    largura = len(caca_palavra[0])
    encontrada = False
    for a in range(altura): #vai buscar na altura ou seja, na vertical
        for l in range(largura): #vai buscar na largura, ou seja, na horizontal
        #depois que buscar SE achar:
            if caca_palavra[a][l] != palavra[0]:
                continue
            for dir_alt, dir_larg, nome_dir in direcoes: #variaveis para identificar as direções e seus sentridos
                k = 0 #indice que vai percorrer toda a palavra
                while k < len(palavra): #quando o indice for menor que o comprimento da palavra...
                #calcula a posição
                    lugarAlt = a + k * dir_alt
                    lugarLarg = l + k * dir_larg

                #verificação de limites, para que a peswuisa sej afeita dentro da matriz 
                    if lugarAlt < 0 or lugarAlt >= altura or lugarLarg < 0 or lugarLarg >= largura:
                        break
                    if caca_palavra[lugarAlt][lugarLarg] != palavra[k]:
                        break
                    k += 1 #prox letra

                if k == len(palavra):
                    print("\nPalavra encontrada!")
                    print("Direção:", nome_dir)
                    print("Início na linha:", a + 1, "coluna:", l + 1)
                    encontrada = True

    if not encontrada:
        print("\nA palavra não foi encontrada.")


#Garante que o código só roda quando o arquivo é executado, não quando é importado
if __name__ == "__main__":
    largura = len(caca_palavra[0])
    mostrar_tabuleiro(caca_palavra, largura)
    buscar_palavra(caca_palavra, direcoes)
