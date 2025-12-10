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

def atualizar_treeview():
        tree.delete(*tree.get_children())
        for i, p in enumerate(perguntas):
            opcoes_texto = ", ".join(p.get("opcoes", []))
            tree.insert("", "end", iid=str(i), values=(p.get("pergunta", ""), opcoes_texto, p.get("resposta", "")))

def limpar_campos():
        entrada_pergunta.delete(0, "end")
        entrada_opcao1.delete(0, "end")
        entrada_opcao2.delete(0, "end")
        entrada_opcao3.delete(0, "end")
        entrada_correta.delete(0, "end")
        nonlocal selecionado_index
        selecionado_index = None
        tree.selection_remove(tree.selection())

def ao_selecionar(event):
        nonlocal selecionado_index
        sel = tree.selection()
        if sel:
            iid = sel[0]
            try:
                idx = int(iid)
            except ValueError:
                return

            selecionado_index = idx
            p = perguntas[idx]

            entrada_pergunta.delete(0, "end")
            entrada_pergunta.insert(0, p.get("pergunta", ""))

            ops = p.get("opcoes", [])
            entrada_opcao1.delete(0, "end"); entrada_opcao1.insert(0, ops[0] if len(ops) > 0 else "")
            entrada_opcao2.delete(0, "end"); entrada_opcao2.insert(0, ops[1] if len(ops) > 1 else "")
            entrada_opcao3.delete(0, "end"); entrada_opcao3.insert(0, ops[2] if len(ops) > 2 else "")

            entrada_correta.delete(0, "end")
            entrada_correta.insert(0, p.get("resposta", ""))
        else:
            limpar_campos()

tree.bind("<<TreeviewSelect>>", ao_selecionar)

def adicionar_ui():
        pergunta = entrada_pergunta.get().strip()
        op1 = entrada_opcao1.get().strip()
        op2 = entrada_opcao2.get().strip()
        op3 = entrada_opcao3.get().strip()
        correta = entrada_correta.get().strip()

        if not pergunta or not correta:
            messagebox.showwarning("Aviso", "Pergunta e resposta correta são obrigatórias.")
            return

        nova = {
            "pergunta": pergunta,
            "opcoes": [op for op in (op1, op2, op3) if op],
            "resposta": correta
        }

        logica.adicionar(perguntas, nova)
        perguntas[:] = logica.carregar_dados()
        atualizar_treeview()
        limpar_campos()









btn_adicionar = ttk.Button(frame_top, text="Criar Pergunta")
btn_adicionar.grid(row=3, column=0, padx=5, pady=10)

btn_atualizar = ttk.Button(frame_top, text="Atualizar")
btn_atualizar.grid(row=3, column=1, padx=5, pady=10)

btn_excluir = ttk.Button(frame_top, text="Excluir")
btn_excluir.grid(row=3, column=2, padx=5, pady=10)

btn_limpar = ttk.Button(frame_top, text="Limpar")
btn_limpar.grid(row=3, column=3, padx=5, pady=10)




janela.mainloop()





 
