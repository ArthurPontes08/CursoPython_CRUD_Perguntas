import tkinter as tk 
from tkinter import ttk, messagebox 

janela = tk.Tk() 
janela.title("CRUD de Perguntas") 
janela.geometry("850x500") 


# === Interface === 
# === Interface ===
frame = ttk.LabelFrame(janela, text="Cadastro / Edição de Perguntas")
frame.pack(fill="x", padx=10, pady=10)

# === Linha 0 — Pergunta ===
ttk.Label(frame, text="Pergunta:").grid(row=0, column=0, padx=5, pady=5, sticky="w")

entrada_pergunta = ttk.Entry(frame, width=85)
entrada_pergunta.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="we")

# === Linha 1 — Opção 1 e Opção 2 ===
ttk.Label(frame, text="Opção 1:").grid(row=1, column=0, padx=5, pady=5, sticky="w")

entrada_opcao1 = ttk.Entry(frame, width=35)
entrada_opcao1.grid(row=1, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frame, text="Opção 2:").grid(row=1, column=2, padx=5, pady=5, sticky="w")

entrada_opcao2 = ttk.Entry(frame, width=35)
entrada_opcao2.grid(row=1, column=3, padx=5, pady=5, sticky="w")

# === Linha 2 — Opção 3 e Resposta Correta ===
ttk.Label(frame, text="Opção 3:").grid(row=2, column=0, padx=5, pady=5, sticky="w")

entrada_opcao3 = ttk.Entry(frame, width=35)
entrada_opcao3.grid(row=2, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frame, text="Resposta Correta:").grid(row=2, column=2, padx=5, pady=5, sticky="w")

entrada_correta = ttk.Entry(frame, width=35)
entrada_correta.grid(row=2, column=3, padx=5, pady=5, sticky="w")

# =================== TREEVIEW (LISTA) ====================

frame_bottom = ttk.LabelFrame(janela, text="Lista de Perguntas")
frame_bottom.place(x=10, y=180, width=880, height=300)

# Criando a tabela
colunas = ("pergunta", "opcoes", "resposta")

tree = ttk.Treeview(frame_bottom, columns=colunas, show="headings")

# Cabeçalhos (títulos das colunas)
tree.heading("pergunta", text="Pergunta")
tree.heading("opcoes", text="Opções")
tree.heading("resposta", text="Resposta")

# Largura das colunas
tree.column("pergunta", width=350)
tree.column("opcoes", width=300)
tree.column("resposta", width=150)

# Scrollbar (barra de rolagem)
scrollbar = ttk.Scrollbar(frame_bottom, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)






janela.mainloop()





 
