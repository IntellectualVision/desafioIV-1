import customtkinter as ctk
import string, random
import clipboard 

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

def gerar_senha():  
    senha = ""
    letras_numeros = string.ascii_letters + string.digits
    letras_caracter = string.ascii_letters + string.punctuation 
    letras_numeros_caracter = string.ascii_letters + string.digits + string.punctuation

    try:
        if opcoes.get() == "Apenas letras":
            for i in range(int(tamanho_senha.get())):
                rand = random.choice(string.ascii_letters)
                senha += rand
        elif opcoes.get() == "Letras e Numeros":
            for i in range(int(tamanho_senha.get())):
                rand = random.choice(letras_numeros)
                senha += rand
        elif opcoes.get() =="letras e Caracteres":
            for i in range(int(tamanho_senha.get())):
                rand = random.choice(letras_caracter)
                senha += rand
        elif opcoes.get() == "Letras Numeros e Caracteres":
            for i in range(int(tamanho_senha.get())):
                rand = random.choice(letras_numeros_caracter)
                senha += rand
        senha_gerada = ctk.CTkLabel(master=frame_secundario, text=senha)
        senha_gerada.pack(pady=12, padx=10)

        def copiar_senha():
            clipboard.copy(str(senha))

        botao_copiar_senha = ctk.CTkButton(master=frame_secundario, text="Copiar Senha", command=copiar_senha)
        botao_copiar_senha.pack(pady=12, padx=10)
    
    except ValueError:
        insira_um_numero = ctk.CTkLabel(master=frame_principal, text="insira um numero!")
        insira_um_numero.grid(column=0, row=4, columnspan=2, pady=12, padx=10)
        
root = ctk.CTk()
root.geometry("500x350")

frame_principal = ctk.CTkFrame(master=root)
frame_principal.grid(column=0, row=0)
frame_principal.place(relx = 0.5, rely = 0.5, anchor =ctk.CENTER)

frame_secundario = ctk.CTkFrame(master=frame_principal)
frame_secundario.grid(column=0, row=5, columnspan=2)

titulo = ctk.CTkLabel(master=frame_principal, text="Gerador de Senhas")
titulo.grid(column=0, row=1, columnspan=2, pady=12, padx=10)

label_tamanho_senha = ctk.CTkLabel(master=frame_principal, text="Insira o Tamanho da Senha")
label_tamanho_senha.grid(column=0, row=2, pady=12, padx=10)

tamanho_senha = ctk.CTkEntry(master=frame_principal)
tamanho_senha.grid(column=1, row=2, pady=12, padx=10)

opcoes = ctk.CTkComboBox(master=frame_principal,
                         values=["Apenas letras",
                                 "Letras e Numeros",
                                 "letras e Caracteres",
                                 "Letras Numeros e Caracteres"])
opcoes.grid(column=0, row=3, pady=12, padx=10)

botao_gerar_senha = ctk.CTkButton(master=frame_principal, text="Gerar Senha", command=gerar_senha)
botao_gerar_senha.grid(column=1, row=3, pady=12, padx=10)
            
root.mainloop()
