def tabuleiro(caca_palavra, palavra):
    altura = len(caca_palavra)
    largura = len(caca_palavra[0])

    direcoes = [
    (0,1, "Horizontal direita"),
    (0, -1, "Horizontal esquerda"),
    ( 1,0, "Vertical para baixo"),
    (-1,0, "Vertical para cima") ]

#busca.py

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
              return True, nome_dir, a + 1, l + 1
        


#main.py
def mostrar_tabuleiro(caca_palavra):
    altura = len(caca_palavra)
    largura = len(caca_palavra[0])

    # Cabeçalho das colunas
    print("    ", end="")
    for col in range(1, largura + 1):
        print(str(col).rjust(2), end=" ")
    print()

    # Linha separadora
    print("    " + "---" * largura)

    # Linhas do tabuleiro
    for i, linha in enumerate(caca_palavra, start=1):
        print(str(i).rjust(2) + " |", end=" ")
        for letra in linha:
            print(letra.rjust(2), end=" ")
        print()
