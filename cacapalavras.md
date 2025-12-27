# Caça-Palavras

## Introdução

A primeira parte do caça-palavras consiste em criar a matriz de palavras e usar táticas de layout.

## Matriz do Caça-Palavras

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

## Transposição da Matriz

```python
# Transpor a matriz
caca_palavras_t = []
for i in range(largura):
    s = ""
    for j in range(altura):
        s += caca_palavras[j][i]
    caca_palavras_t.append(s)
```

### Por que transpor a matriz?

A busca horizontal por palavras é direta, pois cada linha já é uma string contínua.  
Entretanto, na busca vertical, os caracteres da mesma coluna estão distribuídos em diferentes strings, o que impede uma verificação direta.

Para resolver esse problema, realiza-se a transposição da matriz, que consiste em transformar colunas em linhas, facilitando a busca vertical como se fosse horizontal.