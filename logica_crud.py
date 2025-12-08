import json, os
import tkinter as tk
from tkinter import messagebox

arquivo = "perguntas.json"

# Função para json
def carregar_dados():
    if os.path.exists(arquivo):
        with open (arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

def salvar_dados(perguntas):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(perguntas, f, indent=4, ensure_ascii=False)

# Função CRUD        
def adicionar(perguntas, nova):
    try:
      perguntas.append(nova)
      salvar_dados(perguntas)
    except ValueError:
        messagebox.showerror("É necessario preencher o campo vazio.")

def atualizar(perguntas, indice, nova):
    try:
     perguntas[indice] = nova
     salvar_dados(perguntas)
    except ValueError:
        messagebox.showerror("É necessario preencher o campo vazio.")

def excluir(perguntas, indice):
    perguntas.pop(indice)
    salvar_dados(perguntas)                             

# Função de Limpar
def limpar(perguntas):
 perguntas.delete(0, tk.END) 

