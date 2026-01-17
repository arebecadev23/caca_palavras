// static/script.js

console.log("Script do Caça-Palavras carregado! 🚀");

let selecionando = false;
let caminho = [];

// Captura as palavras da lista lateral para validação
let palavras_restantes = new Set(
    Array.from(document.querySelectorAll("#palavras li"))
        .map(li => li.textContent.trim())
);

console.log("Palavras a encontrar:", palavras_restantes);

// --- Lógica Visual de Seleção ---

function adicionarAoCaminho(cell) {
    if (!caminho.includes(cell)) {
        caminho.push(cell);
        cell.classList.add("selected");
    }
}

function iniciarSelecao(e) {
    selecionando = true;
    caminho = [];
    let cell = e.target.closest('.cell'); 
    if (cell && !cell.classList.contains('found')) {
        adicionarAoCaminho(cell);
    }
}

function continuarSelecao(e) {
    if (!selecionando) return;
    
    // Suporte para Mouse e Touch
    let target;
    if (e.touches) {
        target = document.elementFromPoint(e.touches[0].clientX, e.touches[0].clientY);
    } else {
        target = e.target;
    }

    let cell = target ? target.closest('.cell') : null;
    
    if (cell && !caminho.includes(cell)) {
        adicionarAoCaminho(cell);
    }
}

function finalizarSelecao() {
    if (!selecionando) return;
    selecionando = false;

    // Transforma as células selecionadas em texto
    let palavraFormada = caminho.map(c => c.innerText).join("");
    let palavraInvertida = palavraFormada.split("").reverse().join("");

    console.log("Tentou:", palavraFormada);

    let achou = false;
    let palavraEncontrada = "";

    // Verifica se é uma das palavras (normal ou invertida)
    if (palavras_restantes.has(palavraFormada)) {
        achou = true;
        palavraEncontrada = palavraFormada;
    } else if (palavras_restantes.has(palavraInvertida)) {
        achou = true;
        palavraEncontrada = palavraInvertida;
    }

    if (achou) {
        console.log("ACHOU!", palavraEncontrada);
        
        // 1. Pinta o Grid de Verde
        caminho.forEach(c => {
            c.classList.remove("selected");
            c.classList.add("found");
        });

        // 2. Risca na Lista Lateral
        document.querySelectorAll("#palavras li").forEach(li => {
            if (li.textContent.trim() === palavraEncontrada) {
                li.classList.remove("pendente");
                li.classList.add("completa"); // Essa classe faz riscar (veja o CSS)
            }
        });

        // 3. Remove da memória
        palavras_restantes.delete(palavraEncontrada);
        
        // 4. Verifica Vitória
        if (palavras_restantes.size === 0) {
            document.getElementById("mensagem-final").classList.remove("hidden");
        }
    } else {
        // Errou: Limpa a cor roxa (seleção)
        caminho.forEach(c => c.classList.remove("selected"));
    }
    
    // Zera o caminho para a próxima tentativa
    caminho = [];
}

// --- Event Listeners (Compatível com Celular e PC) ---

document.addEventListener("mousedown", (e) => {
    if(e.target.closest('.cell')) iniciarSelecao(e);
});
document.addEventListener("mousemove", continuarSelecao);
document.addEventListener("mouseup", finalizarSelecao);

// Touch Events (Celular)
document.addEventListener("touchstart", (e) => {
    if(e.target.closest('.cell')) {
        e.preventDefault(); // Evita rolar a tela enquanto joga
        iniciarSelecao(e);
    }
}, {passive: false});

document.addEventListener("touchmove", (e) => {
    e.preventDefault();
    continuarSelecao(e);
}, {passive: false});

document.addEventListener("touchend", finalizarSelecao);