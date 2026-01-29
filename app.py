from flask import Flask, render_template, request, redirect, url_for, session
from funcoes import criar_grade, resolver_grade, preencher_restante

app = Flask(__name__)
# DICA SÊNIOR: Em produção, isso viria de variáveis de ambiente (.env)
app.secret_key = "segredo-super-rebeca-seguro" 

# Configuração dos Níveis
NIVEIS = {
    "facil": 10,   # 10x10 (Rápido)
    "medio": 15,   # 15x15 (Equilibrado)
    "dificil": 20  # 20x20 (Desafio Hardcore)
}

@app.route("/")
def index():
    # Limpa a sessão antiga ao voltar para o início para evitar lixo
    session.clear()
    return render_template("index.html")

@app.route("/gerar", methods=["POST"])
def gerar():
    entrada = request.form.get("palavras", "")
    escolha_nivel = request.form.get("nivel", "medio") # Padrão é médio se falhar

    if not entrada:
        return redirect(url_for("index"))

    # Define o tamanho com base na escolha
    tamanho_grid = NIVEIS.get(escolha_nivel, 15)

    palavras = [p.strip() for p in entrada.upper().split()]
    # Remove duplicatas
    palavras = list(dict.fromkeys(palavras))
    # Ordena da maior para menor (CRUCIAL para o algoritmo funcionar bem)
    palavras.sort(key=len, reverse=True)
    
    # Validação Sênior: Se a palavra for maior que o tabuleiro, ignora ela
    palavras = [p for p in palavras if len(p) <= tamanho_grid]

    # Cria a grade com o tamanho dinâmico
    grade = criar_grade(tamanho_grid)

    # Tenta resolver usando Backtracking
    sucesso = resolver_grade(grade, palavras)
    
    if not sucesso:
        return "Erro: Não foi possível encaixar todas as palavras neste nível. Tente um nível maior ou menos palavras."

    # Preenche os vazios
    preencher_restante(grade)

    # Salva na sessão
    session["palavras"] = palavras
    session["grade"] = grade
    session["tamanho_grid"] = tamanho_grid # Guardamos o tamanho para o CSS usar
    
    return redirect(url_for("jogar"))

@app.route("/jogar")
def jogar():
    if "grade" not in session:
        return redirect(url_for("index"))
        
    return render_template("game.html",
                           grade=session["grade"],
                           palavras=session["palavras"],
                           tamanho=session["tamanho_grid"])

# --- ESSA PARTE É A QUE ESTAVA FALTANDO ---
if __name__ == "__main__":
    app.run(debug=True)