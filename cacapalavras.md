# Caça-Palavras

## Introdução

A primeira parte do caça-palavras consiste em criar a matriz de palavras e usar táticas de layout.

## Implementação

### Matriz do Caça-Palavras

```python
caca_palavras = [
    "SISTEMASOPERACIONAIS",
    "RDDFVIGMEMORIARAMGHF",
    "WARLLESRTYUIOOPNBVGC",
    "REBECAJWBFHWJBFHFHEH"
]
```

A variável foi criada para pegar a largura das palavras e deixar de forma simples para o usuário.

Apesar de ser tratada como matriz, essa parte do código é uma lista de strings.

```python
largura = len(caca_palavras[0])  # Buscar o tamanho das palavras
altura = len(caca_palavras)  # Altura da matriz

palavra = input("Digite uma palavra: ")
palavra = palavra.upper()  # Buscar usando letras maiúsculas
palavra_invertida = palavra[::-1]  # Buscar de forma inversa a palavra antes digitada
print("Palavra a ser procurada:", palavra)
```

### Busca de Palavras

#### Método de Busca Anterior

Antes estavamos utilizando o metodo de percorrer tudo e transpor a matriz, ale´me de inverter as palavras para encontrar. Como está agora?

Busca por meio de indices.

como cheguei a essa conclusão?

se cada palavra estava sendo enumerada, por que não utilizar esses numeros para encontrar as palavras, como em um plano cartesiano.

dito e feito.

#### Definição das Direções

```python
direcoes = [
    (0,1, "Horizontal direita"),
    (0, -1, "Horizontal esquerda"),
    ( 1,0, "Vertical para baixo"),
    (-1,0, "Vertical para cima")
]

```

Essa parte sobre direções diz respeito à forma como o sistema irá fazer a busca de palavras.

é uma lista de vetores em movimento.

a estrutura é:

(movimento_das_linhas, movimento_em_colunas, nome_para_print)

#### Loop Principal

```python
for a in range(altura): #vai buscar na altura ou seja, na vertical
    for l in range(largura): #vai buscar na largura, ou seja, na horizontal
        #depois que buscar SE achar:
```

Esses são os loops principais, onde o "a" é o que representa a linha (Altura) e vai represnetar o eixo vertical da matriz.

l → índice da coluna (largura)

Percorre todas as colunas

Representa o eixo horizontal

📌 Juntos (a, l) definem:

uma posição exata da matriz

#### Verificação da Primeira Letra

```python

        if caca_palavra[a][l] != palavra[0]:
            continue
```

Só começa a busca se a primeira letra bater.

O que significa que sem isso eu ficaria testando TODAS as pessibilidades em TODAS as posições, mesmo se a letra inicial não batesse c a outra .

Diferencial de buscar a partir de indice?

✔️ economia absurda de processamento
✔️ algoritmo mais elegante
✔️ pensamento otimizado

#### Algoritmo de Verificação

```python
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
                k += 1 #prox letra // além disso o K é o que da avanço na apalavra e avança a matriz.

            if k == len(palavra):
              print("\nPalavra encontrada!")
              print("Direção:", nome_dir)
              print("Início na linha:", a + 1, "coluna:", l + 1)
              encontrada = True
```

#### Fórmula do Algoritmo

```python

lugarAlt = a + k * dir_alt
lugarLarg = l + k * dir_larg
```

“A cada letra k, ande k passos na direção escolhida”

a, l → ponto inicial

k → passo atual

dir_alt, dir_larg → direção

#### Verificando os Limites da Matriz

#verificação de limites, para que a peswuisa sej afeita dentro da matriz

```python

                if lugarAlt < 0 or lugarAlt >= altura or lugarLarg < 0 or lugarLarg >= largura:
                    break
```

Evita acessar posições que não existem, parece meio confusom mas a interpretação seria:

👉 Leitura humana do código:

Então, se a posição da linha (lugarAlt) for menor que 0,

ou se a posição da linha for maior ou igual ao total de linhas da matriz,

ou se a posição da coluna (lugarLarg) for menor que 0,

ou se a posição da coluna for maior ou igual ao total de colunas da matriz,

isso significa que a próxima letra estaria fora do caça-palavras.

Nesse caso, interrompa essa busca nessa direção.

🧠 Quebra por partes (bem didático)

lugarAlt < 0

→ significa que o algoritmo tentou subir além da primeira linha.

lugarAlt >= altura

→ significa que ele tentou descer além da última linha existente.

lugarLarg < 0

→ significa que ele tentou ir para a esquerda além da primeira coluna.

lugarLarg >= largura

→ significa que ele tentou ir para a direita além da última coluna.

Se qualquer uma dessas situações acontecer, a posição é inválida.

#### Verificação de Letras

```python

if caca_palavra[lugarAlt][lugarLarg] != palavra[k]:
                    break
                k += 1
```

Então, se a letra que está na posição calculada da matriz

(linha = lugarAlt, coluna = lugarLarg)

for diferente da letra da palavra que estamos comparando no momento (palavra[k]),

isso significa que a palavra não continua corretamente nessa direção.

Nesse caso, interrompa imediatamente essa tentativa de busca.

Essa verificação garante que a sequência de letras encontrada na matriz corresponda exatamente à palavra buscada, interrompendo a busca ao primeiro caractere divergente.
