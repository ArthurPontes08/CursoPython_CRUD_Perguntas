import tkinter as tk 
from tkinter import ttk, messagebox
import logica_crud as logica  # import corrigido

# Janela principal
janela = tk.Tk() 
janela.title("CRUD de Perguntas") 
janela.geometry("850x500") 

# Variáveis globais
perguntas = logica.carregar_dados()
selecionado_index = None

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

colunas = ("pergunta", "opcoes", "resposta")
tree = ttk.Treeview(frame_bottom, columns=colunas, show="headings")
tree.heading("pergunta", text="Pergunta")
tree.heading("opcoes", text="Opções")
tree.heading("resposta", text="Resposta")
tree.column("pergunta", width=350)
tree.column("opcoes", width=300)
tree.column("resposta", width=150)

scrollbar = ttk.Scrollbar(frame_bottom, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# =================== Funções ====================
def atualizar_treeview():
    tree.delete(*tree.get_children())
    for i, p in enumerate(perguntas):
        opcoes_texto = ", ".join(p.get("opcoes", []))
        tree.insert("", "end", iid=str(i), values=(p.get("pergunta", ""), opcoes_texto, p.get("resposta", "")))

def limpar_campos():
    global selecionado_index
    entrada_pergunta.delete(0, "end")
    entrada_opcao1.delete(0, "end")
    entrada_opcao2.delete(0, "end")
    entrada_opcao3.delete(0, "end")
    entrada_correta.delete(0, "end")
    selecionado_index = None
    tree.selection_remove(tree.selection())

def ao_selecionar(event):
    global selecionado_index
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

def atualizar_ui():
    global selecionado_index
    if selecionado_index is None:
        messagebox.showinfo("Info", "Selecione uma pergunta para atualizar.")
        return

    pergunta = entrada_pergunta.get().strip()
    op1 = entrada_opcao1.get().strip()
    op2 = entrada_opcao2.get().strip()
    op3 = entrada_opcao3.get().strip()
    correta = entrada_correta.get().strip()

    nova = {
        "pergunta": pergunta,
        "opcoes": [op for op in (op1, op2, op3) if op],
        "resposta": correta
    }

    logica.atualizar(perguntas, selecionado_index, nova)
    perguntas[:] = logica.carregar_dados()
    atualizar_treeview()
    limpar_campos()

def excluir_ui():
    global selecionado_index
    if selecionado_index is None:
        messagebox.showinfo("Info", "Selecione uma pergunta para excluir.")
        return

    if not messagebox.askyesno("Confirma", "Deseja excluir a pergunta selecionada?"):
        return

    logica.excluir(perguntas, selecionado_index)
    perguntas[:] = logica.carregar_dados()
    atualizar_treeview()
    limpar_campos()

# =================== Botões ====================
btn_adicionar = ttk.Button(frame, text="Criar Pergunta", command=adicionar_ui)
btn_adicionar.grid(row=3, column=0, padx=5, pady=10)

btn_atualizar = ttk.Button(frame, text="Atualizar", command=atualizar_ui)
btn_atualizar.grid(row=3, column=1, padx=5, pady=10)

btn_excluir = ttk.Button(frame, text="Excluir", command=excluir_ui)
btn_excluir.grid(row=3, column=2, padx=5, pady=10)

btn_limpar = ttk.Button(frame, text="Limpar", command=limpar_campos)
btn_limpar.grid(row=3, column=3, padx=5, pady=10)
