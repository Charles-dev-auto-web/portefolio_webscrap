# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 14:36:42 2025

@author: Charles
"""

from colorama import init, Fore, Style
from tkinter import *
from tkinter import simpledialog, messagebox
import sys
from scrappeur_ldlc_cartes import crte_ldlc
from scrappeur_amazon import scrap_amazon

MOT_DE_PASSE = "1234"



def get_amazon_scrap():
    root_ama = Tk()
    root_ama.geometry("800x800")
    root_ama.title("scrap amazon")
    ll_scrap_a = Label(root_ama, text=scrap_amazon(), wraplength=2550, justify="left", anchor="nw", font=("Arial", 16))
    ll_scrap_a.pack(fill='both', expand=True)
    amaframe.grid(row=0, column=0, sticky=W)
    root_ama.mainloop()

def get_ldlc_scrap():
    root_ldlc = Tk()
    root_ldlc.geometry("800x800")
    root_ldlc.title("scrap ldlc")
    ll_scrap_l = Label(root_ldlc, text=crte_ldlc(), wraplength=2550, justify="left", anchor="nw", font=("Arial", 16))
    ll_scrap_l.pack(fill='both', expand=True)
    ldlcframe.grid(row=0, column=0, sticky=W)
    root_ldlc.mainloop()


root = Tk()
root.geometry("800x800")

def demander_mot_de_passe():
    mdp = simpledialog.askstring("mot de passe", "Entrer le mot de passe :", show="*")
    root.title("Acces sécurisé")
    if mdp != MOT_DE_PASSE:
        messagebox.showerror("Erreur", "Mot de passe incorrect !")
        sys.exit(0)
    else:
        afficher_interface_principale()

frame = Frame(root)
def afficher_interface_principale():
    root.title("Principal")
    ll = Label(frame, text="Welcome in the appllication !", font=("Arial", 25))
    ll.pack()
    ll_amazon_btn = Button(frame, text="scrap cartes amazon", font=("Arial", 16), command=get_amazon_scrap)
    ll_amazon_btn.pack()
    ll_ldlc_btn = Button(frame, text="scrap cartes ldlc", font=("Arial", 16), command=get_ldlc_scrap)
    ll_ldlc_btn.pack()
    ll_top_achat_btn = Label(frame, text="RTX 4070 Ti Super unavalaible on TopAchat", font=("Arial", 16))
    ll_top_achat_btn.pack()

root.withdraw()
root.after(500, demander_mot_de_passe())
root.geometry("800x800")
root.deiconify()
frame.grid(row=1, column=0, sticky=W)
frame.pack(expand="YES")

root.mainloop()
