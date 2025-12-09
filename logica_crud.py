import json, os
import tkinter as tk
from tkinter import messagebox

arquivo = "perguntas.json"

# Função para json
def carregar_dados():
    if os.path.exists(arquivo):
        with open (arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

