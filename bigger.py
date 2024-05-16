import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkinter import font


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class Database: 
    def __init__(self, db_patch):
        self.conexao = sqlite3.connect(db_patch)
        self.cursor = self.conexao.cursor()

    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS qualityusers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL,
                            "password" TEXT NOT NULL
        )''') 

        self.conexao.commit()

class GifAnimator:
    def __init__(self, gif_path, label):
        self.gif = Image.open(gif_path)
        self.label = label
        self.label.config(highlightthickness=0)
        self.animate_gif()

    def animate_gif(self):
        try:
            self.gif.seek(self.gif.tell() + 1)
        except EOFError:
            self.gif.seek(0)
        self.photo = ImageTk.PhotoImage(self.gif)
        self.label.configure(image=self.photo)
        self.label.after(100, self.animate_gif)

class Login: 
    def __init__ (self,parent, cursor):

        self.parent = parent
        self.cursor = cursor

        self.login_frame = ctk.CTkFrame(master=self.parent, width=400, height=450, border_width=10)
        self.login_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        label = ctk.CTkLabel(master=self.login_frame, text="Bigger2.0", font=("Oswald", 32), text_color="#00FFFF")
        label.place(x=130, y=80)

        self.username = ctk.CTkEntry(master=self.login_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14))
        self.username.place(x=50, y=150)
        self.username_label = ctk.CTkLabel(master=self.login_frame, text="O campo de usuário é obrigatório", text_color="#00FFFF", font=("Roboto", 12))
        self.username_label.place(x=52, y=180)

        self.senha = ctk.CTkEntry(master=self.login_frame, placeholder_text="Senha de usuário", width=300, font=("Roboto", 14), show='*')
        self.senha.place(x=50, y=220)
        self.senha_label = ctk.CTkLabel(master=self.login_frame, text="O campo de senha é obrigatório", text_color="#00FFFF", font=("Roboto", 12))
        self.senha_label.place(x=52, y=250)

        self.lembrar_user = ctk.CTkCheckBox(master=self.login_frame, text="Lembrar-se de mim").place(x=52, y=280)

        self.login_button = ctk.CTkButton(master=self.login_frame, text="LOGIN", width=300)
        self.login_button.place(x=52, y=320)
        self.registro_button = ctk.CTkButton(master=self.login_frame, text="REGISTRE-SE").place(x=52, y=360)
        self.troca_senha = ctk.CTkButton(master=self.login_frame, text="ESQUECI MINHA SENHA").place(x=200, y=360)


class Application:
    def __init__(self):
        self.tela = ctk.CTk()
        self.tela.geometry("1000x450")
        self.tela.title("Login QualiGames")
        self.tela.resizable(False, False)

        self.db_manager = Database("QualityUsers.db")
        self.db_manager.criar_tabela()

        self.gif_label = Label(self.tela)
        self.gif_label.pack(side=LEFT, fill=BOTH, expand=True)
        self.animator = GifAnimator("gifanimado2.gif", self.gif_label)

        self.login_frame = Login(self.tela, self.db_manager.cursor)

        self.tela.mainloop()

try:
    Application()
except Exception as e:
    print("Ocorreu um erro:", e)       