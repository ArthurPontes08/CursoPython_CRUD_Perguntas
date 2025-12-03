import tkinter as tk 
from tkinter import ttk, messagebox 
import logica 

def iniciar_interface(): 
 janela = tk.Tk() 
 janela.title("CRUD de Perguntas") 
 janela.geometry("850x500") 
 perguntas = logica.carregar_dados()
