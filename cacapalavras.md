# Caça-Palavras - Documentação de Projeto

## Sumário
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Projeto](#arquitetura-do-projeto)
3. [Parte 1: Algoritmo de Busca](#parte-1-algoritmo-de-busca)
4. [Parte 2: Aplicação Web com Flask](#parte-2-aplicação-web-com-flask)
5. [Parte 3: Template Engine Jinja2](#parte-3-template-engine-jinja2)
6. [Tecnologias Utilizadas](#tecnologias-utilizadas)

---

## Visão Geral

**Caça-Palavras** é uma aplicação web interativa que permite aos usuários jogar caça-palavras em tempo real. O projeto combina um backend Python com Flask e um algoritmo eficiente de busca de palavras em matrizes.

### Objetivos
- Criar uma experiência lúdica e intuitiva para jogadores
- Implementar um algoritmo otimizado de busca de palavras
- Separar claramente a lógica de negócio da interface gráfica

---

## Arquitetura do Projeto

### Estrutura de Diretórios
```
├── app.py                  # Aplicação principal (Flask)
├── funcoes.py              # Lógica e funções do jogo
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do usuário
├── static/
│   ├── script.js          # JavaScript do frontend
│   └── style.css          # Estilos CSS
└── templates/
    ├── index.html         # Página inicial
    ├── game.html          # Interface do jogo
    └── tabuleiro.html     # Tabuleiro interativo
```

### Separação de Responsabilidades
- **app.py**: Camada de apresentação (rotas e templates)
- **funcoes.py**: Lógica de negócio (algoritmo de busca)
- **Frontend**: Interface visual (HTML, CSS, JavaScript)

---

## Parte 1: Algoritmo de Busca

### 1.1 Estrutura de Dados: Matriz

A matriz do caça-palavras é implementada como uma lista de strings, onde cada string representa uma linha:

```python
caca_palavras = [
    "SISTEMASOPERACIONAIS",
    "RDDFVIGMEMORIARAMGHF",
    "WARLLESRTYUIOOPNBVGC",
    "REBECAJWBFHWJBFHFHEH"
]
```

#### Cálculo de Dimensões
```python
largura = len(caca_palavras[0])   # Número de colunas
altura = len(caca_palavras)        # Número de linhas
```

#### Pré-processamento da Entrada
```python
palavra = input("Digite uma palavra: ")
palavra = palavra.upper()           # Normalizar para maiúsculas
palavra_invertida = palavra[::-1]   # Suportar buscas invertidas
```

---

### 1.2 Definição das Direções de Busca

O algoritmo suporta 4 direções de busca, representadas como vetores de movimento:

```python
direcoes = [
    (0, 1, "Horizontal direita"),
    (0, -1, "Horizontal esquerda"),
    (1, 0, "Vertical para baixo"),
    (-1, 0, "Vertical para cima")
]
```

**Estrutura de cada direção**: `(movimento_linhas, movimento_colunas, nome_descritivo)`

| Direção | Movimento (a, l) | Descrição |
|---------|------------------|-----------|
| Direita | (0, 1) | Navega horizontalmente para a direita |
| Esquerda | (0, -1) | Navega horizontalmente para a esquerda |
| Baixo | (1, 0) | Navega verticalmente para baixo |
| Cima | (-1, 0) | Navega verticalmente para cima |

---

### 1.3 Algoritmo de Busca: Implementação

#### Etapa 1: Iteração pela Matriz
```python
for a in range(altura):      # Itera pelas linhas (eixo vertical)
    for l in range(largura): # Itera pelas colunas (eixo horizontal)
        # Cada posição (a, l) é verificada como possível ponto inicial
```

**Conceito**: Cada par `(a, l)` define uma posição exata na matriz, usando coordenadas cartesianas.

#### Etapa 2: Filtragem da Primeira Letra
```python
if caca_palavra[a][l] != palavra[0]:
    continue  # Pula para próxima posição se primeira letra não bater
```

**Vantagem**: Reduz drasticamente o número de iterações, economizando processamento.

#### Etapa 3: Verificação em Todas as Direções
```python
for dir_alt, dir_larg, nome_dir in direcoes:
    k = 0  # Índice para percorrer a palavra
    
    while k < len(palavra):
        # Calcular a posição na matriz
        lugarAlt = a + k * dir_alt
        lugarLarg = l + k * dir_larg
        
        # Validar limites da matriz
        if lugarAlt < 0 or lugarAlt >= altura or \
           lugarLarg < 0 or lugarLarg >= largura:
            break
        
        # Verificar se a letra coincide
        if caca_palavra[lugarAlt][lugarLarg] != palavra[k]:
            break
        
        k += 1  # Avançar para próxima letra
    
    # Se toda a palavra foi encontrada
    if k == len(palavra):
        print("\nPalavra encontrada!")
        print("Direção:", nome_dir)
        print("Início na linha:", a + 1, "coluna:", l + 1)
        encontrada = True
```

---

### 1.4 Fórmula Matemática do Algoritmo

A posição de cada letra é calculada usando a seguinte fórmula:

$$\text{posição} = (a + k \cdot \text{dir\_alt}, l + k \cdot \text{dir\_larg})$$

Onde:
- **a, l**: Coordenadas do ponto inicial
- **k**: Índice atual na palavra (0, 1, 2, ...)
- **dir_alt, dir_larg**: Componentes do vetor direção

**Interpretação**: "A cada letra k, avance k passos na direção escolhida"

---

### 1.5 Validação de Limites

A verificação garante que a busca não ultrapasse os limites da matriz:

```python
if lugarAlt < 0 or lugarAlt >= altura or \
   lugarLarg < 0 or lugarLarg >= largura:
    break
```

| Condição | Significado | Ação |
|----------|-------------|------|
| `lugarAlt < 0` | Tentou subir além da primeira linha | Interromper busca |
| `lugarAlt >= altura` | Tentou descer além da última linha | Interromper busca |
| `lugarLarg < 0` | Tentou ir para esquerda do início | Interromper busca |
| `lugarLarg >= largura` | Tentou ir para direita do fim | Interromper busca |

---

### 1.6 Verificação de Correspondência de Letras

```python
if caca_palavra[lugarAlt][lugarLarg] != palavra[k]:
    break  # Interromper se letra não corresponder
k += 1      # Avançar para próxima letra se corresponder
```

**Garantia**: Apenas sequências exatas são reconhecidas. Qualquer desvio cancela a busca naquela direção.

---

### 1.7 Otimizações e Benefícios

| Otimização | Benefício |
|-----------|-----------|
| Filtrar pela primeira letra | Reduz iterações desnecessárias |
| Usar índices (coordenadas) | Permite busca eficiente em 2D |
| Validar limites antecipadamente | Evita exceções de acesso |
| Separar por direções | Código modular e legível |

---

## Parte 2: Aplicação Web com Flask

### 2.1 O que é Flask?

Flask é um framework web Python minimalista que permite transformar um programa Python em uma aplicação web com interface gráfica.

#### Comparação

| Sem Flask | Com Flask |
|-----------|-----------|
| Código executa apenas no terminal | Interface visual em navegador |
| Sem interação do usuário | Usuário interage via cliques e formulários |
| Sem persistência de estado | Dados mantidos entre requisições |
| Interface pobre | Interface moderna e responsiva |

---

### 2.2 Importações e Configuração

#### Importações Principais
```python
from flask import Flask, render_template, request, redirect, url_for, session
```

| Módulo | Propósito |
|--------|-----------|
| `Flask` | Cria a aplicação web |
| `render_template` | Renderiza templates HTML com dados Python |
| `request` | Captura dados do formulário HTML |
| `redirect` | Redireciona para outra rota |
| `url_for` | Gera URLs seguras dinamicamente |
| `session` | Armazena dados temporários do usuário |

---

### 2.3 Inicialização da Aplicação

```python
app = Flask(__name__)
app.secret_key = "segredo-super-rebeca-seguro"
```

#### Conceitos

| Conceito | Explicação |
|----------|-----------|
| `Flask(__name__)` | Cria a aplicação; `__name__` ajuda localizar templates e arquivos estáticos |
| `secret_key` | Chave de criptografia para sessões; garante segurança dos dados do usuário |

---

### 2.4 Rotas HTTP

Rotas conectam URLs a funções Python, estabelecendo a comunicação entre frontend e backend.

#### 2.4.1 Rota Inicial

```python
@app.route("/")
def index():
    session.clear()  # Limpar dados de sessões anteriores
    return render_template("index.html")
```

**Fluxo**:
1. Usuário acessa a URL `/`
2. Flask executa a função `index()`
3. Dados da sessão anterior são limpos
4. Template `index.html` é renderizado

**Conceitos envolvidos**:
- Rota HTTP
- Renderização de template
- Gerenciamento de estado (sessão)

---

#### 2.4.2 Rota de Geração do Jogo

```python
@app.route("/gerar", methods=["POST"])
def gerar():
    entrada = request.form.get("palavras", "")
    escolha_nivel = request.form.get("nivel", "medio")
    # ... lógica de geração
```

**Método HTTP**: POST
- Usado para enviar dados (input do formulário)
- Diferente de GET (apenas recupera dados)

**Recebimento de Dados**:
```python
request.form.get("nome_do_campo", "valor_padrão")
```

---

#### 2.4.3 Fluxo da Rota de Geração

```python
@app.route("/gerar", methods=["POST"])
def gerar():
    # 1. Receber dados do formulário
    entrada = request.form.get("palavras", "")
    escolha_nivel = request.form.get("nivel", "medio")
    
    # 2. Processar (chamar funções lógicas)
    # palavras = processar_entrada(entrada)
    # grade = resolver_grade(palavras, escolha_nivel)
    
    # 3. Salvar na sessão (memória temporária)
    session["palavras"] = palavras
    session["grade"] = grade
    session["tamanho_grid"] = tamanho_grid
    
    # 4. Redirecionar para próxima página
    return redirect(url_for("jogar"))
```

**Responsabilidade do Flask**: Apenas orquestração. A lógica real (geração da grade) fica em `funcoes.py`.

---

#### 2.4.4 Armazenamento em Sessão

```python
session["palavras"] = palavras
session["grade"] = grade
session["tamanho_grid"] = tamanho_grid
```

**O que é Sessão?**
- Armazena dados temporários associados ao usuário
- Funciona como "memória de curto prazo" do site
- Evita recalcular dados desnecessariamente
- Limpa após logout ou limpeza manual

**Vantagem**: Não precisa recalcular a grade a cada página visualizada.

---

#### 2.4.5 Rota do Jogo

```python
@app.route("/jogar")
def jogar():
    # Validação de segurança
    if "grade" not in session:
        return redirect(url_for("index"))
    
    # Enviar dados para o template
    return render_template("game.html",
                           grade=session["grade"],
                           palavras=session["palavras"],
                           tamanho=session["tamanho_grid"])
```

**Validação de Estado**:
- Verifica se a grade foi gerada antes
- Redireciona para início se tentar acessar a URL diretamente

**Template Engine (Jinja2)**:
- Passa dados Python para HTML
- Permite renderização dinâmica

---

### 2.5 Ponto de Entrada da Aplicação

```python
if __name__ == "__main__":
    app.run(debug=True)
```

| Conceito | Explicação |
|----------|-----------|
| `if __name__ == "__main__"` | Garante que o servidor só inicia ao executar diretamente |
| `app.run()` | Inicia o servidor local |
| `debug=True` | Modo desenvolvimento: reload automático e erro detalhado |

---

## Tecnologias Utilizadas

| Tecnologia | Função |
|-----------|--------|
| **Python 3** | Linguagem de programação principal |
| **Flask** | Framework web para criar rotas e gerenciar requisições |
| **Jinja2** | Template engine para renderizar HTML dinamicamente |
| **HTML5** | Estrutura da interface |
| **CSS3** | Estilização da interface |
| **JavaScript** | Interatividade no frontend |

---

## Parte 3: Template Engine Jinja2

### 3.1 Conceito Fundamental

O **Jinja2** é um motor de templates (template engine) utilizado pelo Flask para renderizar páginas HTML dinâmicas.

**Objetivo principal**: Permitir que dados Python sejam inseridos em templates HTML, criando conteúdo dinâmico.

#### Como Funciona

O fluxo de processamento é:

1. **Python** processa a lógica e prepara os dados
2. **Flask** chama `render_template()` passando os dados
3. **Jinja2** interpreta o template e substitui variáveis
4. **HTML final** é gerado e enviado ao navegador

```
Python → Flask → Jinja2 → HTML → Navegador
(lógica) (orquestração) (renderização) (apresentação)
```

---

### 3.2 Por que Jinja2 é Necessário?

#### Limitações do HTML Puro

HTML é uma linguagem **estática**, ou seja:

| Limitação | Impacto |
|-----------|--------|
| Sem laços (`for`) | Impossível iterar listas |
| Sem condições (`if`) | Impossível lógica condicional |
| Sem variáveis | Impossível exibir dados dinâmicos |
| Sem computação | Impossível fazer cálculos |

#### Necessidade no Projeto Caça-Palavras

O conteúdo da página **muda constantemente**:

| Aspecto | Variação |
|--------|----------|
| Tamanho da grade | Depende do nível escolhido |
| Letras do tabuleiro | Diferentes para cada jogo |
| Lista de palavras | Altera conforme entrada do usuário |
| Posição das células | Varia dinamicamente |

**Conclusão**: Sem Jinja2, seria necessário gerar HTML manualmente no Python (prática ruim).

---

### 3.3 Relação entre Flask e Jinja2

#### Fluxo de Dados

```python
@app.route("/jogar")
def jogar():
    # 1. Dados são preparados no Python
    grade = [["A", "B"], ["C", "D"]]
    palavras = ["SISTEMA", "REBECA"]
    
    # 2. Flask envia dados para Jinja2
    return render_template("game.html", 
                          grade=grade,
                          palavras=palavras)
```

#### Processamento no Jinja2

```html
<!-- 3. Jinja2 interpreta as variáveis -->
<div class="tabuleiro">
  {% for linha in grade %}
    <div class="linha">
      {% for letra in linha %}
        <span class="celula">{{ letra }}</span>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<!-- 4. HTML final é gerado -->
<div class="tabuleiro">
  <div class="linha">
    <span class="celula">A</span>
    <span class="celula">B</span>
  </div>
  <div class="linha">
    <span class="celula">C</span>
    <span class="celula">D</span>
  </div>
</div>
```

**Jinja2 é a ponte entre backend (Python) e frontend (HTML)**.

---

### 3.4 Sintaxe Básica do Jinja2

#### 3.4.1 Impressão de Variáveis

```jinja2
{{ variavel }}
```

**Uso**: Exibe valores enviados pelo Python no HTML.

**Exemplo**:
```python
# Python
return render_template("index.html", titulo="Caça-Palavras")
```

```html
<!-- HTML com Jinja2 -->
<h1>{{ titulo }}</h1>

<!-- Resultado -->
<h1>Caça-Palavras</h1>
```

---

#### 3.4.2 Laço de Repetição

```jinja2
{% for item in lista %}
  {{ item }}
{% endfor %}
```

**Uso**: Itera sobre listas, tuplas ou dicionários.

**Exemplo**:
```python
# Python
palavras = ["SISTEMA", "MEMORIA", "REBECA"]
return render_template("game.html", palavras=palavras)
```

```html
<!-- HTML com Jinja2 -->
<ul>
  {% for palavra in palavras %}
    <li>{{ palavra }}</li>
  {% endfor %}
</ul>

<!-- Resultado -->
<ul>
  <li>SISTEMA</li>
  <li>MEMORIA</li>
  <li>REBECA</li>
</ul>
```

**Nota**: Cada iteração tem acesso a `loop` (variável especial):
- `loop.index`: Posição atual (começa em 1)
- `loop.index0`: Posição atual (começa em 0)
- `loop.first`: True se é primeira iteração
- `loop.last`: True se é última iteração

---

#### 3.4.3 Condicional

```jinja2
{% if condicao %}
  Conteúdo se verdadeiro
{% elif outra_condicao %}
  Conteúdo se outra condição
{% else %}
  Conteúdo padrão
{% endif %}
```

**Uso**: Exibe conteúdo baseado em condições.

**Exemplo**:
```python
# Python
return render_template("game.html", nivel="dificil", pontos=1500)
```

```html
<!-- HTML com Jinja2 -->
{% if nivel == "dificil" %}
  <p>Modo Difícil - Boa sorte!</p>
{% elif nivel == "medio" %}
  <p>Modo Médio</p>
{% else %}
  <p>Modo Fácil</p>
{% endif %}

{% if pontos > 1000 %}
  <span class="badge">Parabéns!</span>
{% endif %}
```

---

### 3.5 Exemplo Aplicado: Renderizando a Grade

#### Dados do Python

```python
# funcoes.py
def resolver_grade(palavras, nivel):
    if nivel == "facil":
        tamanho = 8
    elif nivel == "medio":
        tamanho = 12
    else:
        tamanho = 16
    
    grade = gerar_matriz(tamanho)
    return grade, tamanho

# app.py
@app.route("/jogar")
def jogar():
    grade = session.get("grade")
    tamanho = session.get("tamanho_grid")
    
    return render_template("game.html",
                          grade=grade,
                          tamanho=tamanho)
```

#### Template HTML com Jinja2

```html
<!-- templates/game.html -->
<div class="tabuleiro" style="grid-template-columns: repeat({{ tamanho }}, 1fr);">
  {% for linha in grade %}
    {% for letra in linha %}
      <div class="celula" data-letra="{{ letra }}">
        {{ letra }}
      </div>
    {% endfor %}
  {% endfor %}
</div>

<!-- Estilo CSS -->
<style>
  .tabuleiro {
    display: grid;
    gap: 5px;
  }
  
  .celula {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #ccc;
    cursor: pointer;
  }
</style>
```

#### HTML Gerado (Exemplo para tamanho=4)

```html
<div class="tabuleiro" style="grid-template-columns: repeat(4, 1fr);">
  <div class="celula" data-letra="S">S</div>
  <div class="celula" data-letra="I">I</div>
  <div class="celula" data-letra="S">S</div>
  <div class="celula" data-letra="T">T</div>
  
  <div class="celula" data-letra="R">R</div>
  <!-- ... mais células ... -->
</div>
```

---

### 3.6 Exemplo Avançado: Listagem de Palavras com Condicional

#### Template HTML com Jinja2

```html
<!-- templates/game.html -->
<div class="palavras-lista">
  <h3>Palavras para encontrar ({{ palavras|length }})</h3>
  
  {% if palavras %}
    <ul>
      {% for palavra in palavras %}
        <li class="palavra-item">
          {% if loop.index <= 5 %}
            <span class="dificuldade-facil">{{ loop.index }}. {{ palavra }}</span>
          {% elif loop.index <= 10 %}
            <span class="dificuldade-media">{{ loop.index }}. {{ palavra }}</span>
          {% else %}
            <span class="dificuldade-dificil">{{ loop.index }}. {{ palavra }}</span>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
  {% else %}
    <p class="vazio">Nenhuma palavra foi inserida. Comece um novo jogo!</p>
  {% endif %}
</div>
```

**Funcionalidades demonstradas**:
- `{{ palavras|length }}`: Filtro para contar elementos
- `loop.index`: Acesso ao número da iteração
- Condicionais dentro de loops
- Mensagem alternativa se lista vazia

---

### 3.7 Conceitos-Chave do Jinja2

| Conceito | Descrição | Benefício |
|----------|-----------|-----------|
| **Templates Dinâmicos** | HTML que se adapta aos dados | Reutilização de código |
| **Separação de Responsabilidades** | Lógica em Python, apresentação em HTML | Manutenção facilitada |
| **Integração Backend/Frontend** | Dados fluem do Python para HTML | Comunicação clara |
| **Reutilização de Código** | Templates podem incluir sub-templates | DRY (Don't Repeat Yourself) |
| **Segurança** | Sanitização automática de dados | Prevenção de XSS |

---

### 3.8 Fluxo Completo: Do Python ao Navegador

```
┌─────────────────────────────────────────────────────────────┐
│ 1. USUÁRIO ACESSA URL /jogar                                │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. FLASK EXECUTA @app.route("/jogar")                       │
│    - Valida se grade está na sessão                          │
│    - Recupera dados da sessão                                │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. JINJA2 PROCESSA game.html                                │
│    - Substitui {{ grade }} pela matriz real                 │
│    - Executa loops {% for %}                                │
│    - Avalia condicionais {% if %}                           │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. HTML FINAL É GERADO                                      │
│    - Contém apenas HTML puro (sem Jinja2)                   │
│    - Pronto para ser enviado ao navegador                   │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. NAVEGADOR RECEBE HTML E RENDERIZA                        │
│    - Exibe a grade com as letras                            │
│    - Exibe a lista de palavras                              │
│    - JavaScript adiciona interatividade                      │
└─────────────────────────────────────────────────────────────┘
```

---

### 3.9 Por Que Jinja2 Foi Escolhido para o Projeto?

| Razão | Vantagem |
|-------|----------|
| **Conteúdo Dinâmico** | Tamanho da grade varia por nível |
| **Iteração sobre Dados** | Cria células da matriz automaticamente |
| **Lógica Condicional** | Diferentes estilos para diferentes dificuldades |
| **Segurança** | Protege contra injeção XSS |
| **Integração com Flask** | Funciona perfeitamente com Flask |
| **Simplicidade** | Sintaxe clara e fácil de aprender |

---

### 3.10 Resumo: Jinja2 no Projeto

**Em poucas palavras**:

O Jinja2 permite que o projeto **Caça-Palavras** renderize páginas HTML que se adaptam automaticamente aos dados processados no Python, criando uma experiência dinâmica e responsiva para o usuário, sem necessidade de recarregar a página ou gerar HTML manualmente no backend.

**Exemplo prático**:
- Usuário escolhe nível "difícil"
- Python gera grade 16x16 com palavras
- Jinja2 cria 256 células HTML automaticamente
- Navegador exibe tabuleiro interativo
- Usuário clica para encontrar palavras

Tudo isso sem que o desenvolvedor tenha que escrever 256 linhas de HTML manualmente!

---

## Tecnologias Utilizadas

| Tecnologia | Função |
|-----------|--------|
| **Python 3** | Linguagem de programação principal |
| **Flask** | Framework web para criar rotas e gerenciar requisições |
| **Jinja2** | Template engine para renderizar HTML dinamicamente |
| **HTML5** | Estrutura da interface |
| **CSS3** | Estilização da interface |
| **JavaScript** | Interatividade no frontend |

---

## Conclusão

O projeto **Caça-Palavras** demonstra a integração de:

1. **Algoritmo eficiente**: Busca otimizada com índices e validação de limites
2. **Arquitetura web**: Separação clara entre backend (lógica) e frontend (apresentação)
3. **Framework Flask**: Orquestração de requisições e gerenciamento de estado
4. **Template Engine Jinja2**: Renderização dinâmica de HTML com dados Python

Essa estrutura modular em 4 camadas (algoritmo, framework, template engine, frontend) facilita manutenção, testes e extensões futuras do projeto, demonstrando boas práticas de engenharia de software.

## “O Procfile é um arquivo de configuração usado no deploy que informa ao servidor qual comando deve ser executado para iniciar a aplicação.”