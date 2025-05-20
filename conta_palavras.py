import tkinter as tk
from tkinter import messagebox
from collections import defaultdict

# Função que simula o "mapper" do MapReduce
def mapper(texto):
    resultado = []
    for linha in texto.strip().split('\n'):
        for palavra in linha.strip().split():
            resultado.append((palavra.lower(), 1))
    return resultado

# Função que simula o "reducer" do MapReduce
def reducer(mapeado):
    reduzido = defaultdict(int)
    for palavra, contagem in mapeado:
        reduzido[palavra] += contagem
    return dict(reduzido)

# Função chamada pelo botão da interface
def executar_mapreduce():
    texto = entrada_texto.get("1.0", tk.END)
    if not texto.strip():
        messagebox.showwarning("Aviso", "Digite algum texto.")
        return

    mapeado = mapper(texto)
    reduzido = reducer(mapeado)

    saida_texto.delete("1.0", tk.END)
    saida_texto.insert(tk.END, f"{'Palavra':<15} | Quantidade\n")
    saida_texto.insert(tk.END, "-" * 30 + "\n")

    for palavra in sorted(reduzido):
        saida_texto.insert(tk.END, f"{palavra:<15} | {reduzido[palavra]}\n")

# Interface
janela = tk.Tk()
janela.title("Simulador MapReduce - Contador de Palavras")
janela.geometry("550x450")

# Entrada de texto
tk.Label(janela, text="Digite o texto para simular MapReduce:", font=("Arial", 12)).pack(pady=5)
entrada_texto = tk.Text(janela, height=8, font=("Arial", 11))
entrada_texto.pack(padx=10, pady=5, fill=tk.BOTH)

# Botão
tk.Button(janela, text="Executar MapReduce", command=executar_mapreduce, font=("Arial", 12)).pack(pady=10)

# Saída
saida_texto = tk.Text(janela, height=12, font=("Courier New", 11))
saida_texto.pack(padx=10, pady=5, fill=tk.BOTH)

# Loop principal
janela.mainloop()
