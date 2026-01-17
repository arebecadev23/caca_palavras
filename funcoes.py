import random
import string

def criar_grade(tamanho):
    """Cria uma matriz vazia NxN."""
    return [["" for _ in range(tamanho)] for _ in range(tamanho)]

def preencher_restante(grade):
    """Preenche os espaços vazios com letras aleatórias."""
    alfabeto = string.ascii_uppercase
    for i in range(len(grade)):
        for j in range(len(grade)):
            if grade[i][j] == "":
                grade[i][j] = random.choice(alfabeto)

# --- LÓGICA DE BACKTRACKING (Profissional) ---

def verificar_encaixe(grade, palavra, lin, col, dl, dc):
    """Verifica se a palavra cabe na posição e direção sem conflitos."""
    tam = len(grade)
    for i, letra in enumerate(palavra):
        nl, nc = lin + i*dl, col + i*dc
        
        # 1. Verifica se saiu do tabuleiro
        if not (0 <= nl < tam and 0 <= nc < tam):
            return False
            
        # 2. Verifica colisão: só pode se for vazio ou a MESMA letra
        if grade[nl][nc] != "" and grade[nl][nc] != letra:
            return False
    return True

def escrever_palavra(grade, palavra, lin, col, dl, dc):
    """Escreve a palavra na grade."""
    for i, letra in enumerate(palavra):
        grade[lin + i*dl][col + i*dc] = letra

def resolver_grade(grade, palavras_restantes):
    """
    Função Recursiva: Tenta encaixar todas as palavras.
    Retorna True se conseguir, False se falhar (e volta atrás).
    """
    # Caso base: A lista de palavras acabou? Sucesso!
    if not palavras_restantes:
        return True
    
    palavra_atual = palavras_restantes[0]
    tam = len(grade)
    
    # Gera todas as posições possíveis (linha, coluna)
    posicoes = [(l, c) for l in range(tam) for c in range(tam)]
    
    # Define as 8 direções
    direcoes = [
        (0, 1), (0, -1), (1, 0), (-1, 0),       # Retas
        (1, 1), (-1, -1), (1, -1), (-1, 1)      # Diagonais
    ]
    
    # Embaralha para o jogo ser sempre diferente
    random.shuffle(posicoes)
    random.shuffle(direcoes)
    
    for lin, col in posicoes:
        for dl, dc in direcoes:
            if verificar_encaixe(grade, palavra_atual, lin, col, dl, dc):
                
                # 1. BACKUP: Salva o que estava nas células antes de escrever
                backup = []
                for k in range(len(palavra_atual)):
                    backup.append(grade[lin + k*dl][col + k*dc])
                
                # 2. AÇÃO: Escreve a palavra
                escrever_palavra(grade, palavra_atual, lin, col, dl, dc)
                
                # 3. RECURSÃO: Tenta encaixar o RESTO das palavras
                if resolver_grade(grade, palavras_restantes[1:]):
                    return True # Deu certo até o fim!
                
                # 4. BACKTRACKING (Desfazer): Se deu errado lá na frente, restaura o backup
                for k, valor_original in enumerate(backup):
                    grade[lin + k*dl][col + k*dc] = valor_original
                    
    return False # Não foi possível encaixar essa palavra em lugar nenhum