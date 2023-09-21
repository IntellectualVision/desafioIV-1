# import string
# import random

# while True:
#     comprimento = int(input("Comprimento da senha: "))

#     if comprimento <= 0:
#         print("Número inválido! Digite um número maior ou igual a 1")
#     else:
#         break

# while True:
#     tem_numero = input("Incluir número? (S/N): ").upper

#     if tem_numero not in ['S', 'N']:
#         print("Opção inválida! Digite S ou N")
#     else:
#         break

# while True:
#     tem_simbolo = input("Incluir símbolos? (S/N): ").upper

#     if tem_simbolo not in ['S', 'N']:
#         print("Opção inválida! Digite S ou N")
#     else:
#         break

# SENHA = ""
# caracteres = list(string.ascii_letters)

# if tem_numero:
#     caracteres += list(string.digits)
# if tem_simbolo:
#     caracteres += list(string.punctuation)

# while len(SENHA) < comprimento:
#     SENHA += random.choice(caracteres)

# print(f"Sua senha gerada é: {SENHA}")

# import streamlit as st

# st.title("Meu Aplicativo Streamlit")
# st.write("Bem-vindo ao meu aplicativo!")

# # Adicione elementos interativos, como botões e caixas de texto
# user_input = st.text_input("Digite algo:")
# st.write("Você digitou:", user_input)

# # Execute o aplicativo com o seguinte comando
# if __name__ == "__main__":
#     st.run()

import string
import random
import streamlit as st

st.title("Gerador de Senhas")

# Solicita ao usuário o comprimento da senha
comprimento = st.number_input("Comprimento da senha:", min_value=1, value=8)

# Solicita ao usuário a inclusão de números
tem_numero = st.checkbox("Incluir números")

# Solicita ao usuário a inclusão de símbolos
tem_simbolo = st.checkbox("Incluir símbolos")

# Função para gerar a senha com base nas escolhas do usuário
def gerar_senha(comprimento, tem_numero, tem_simbolo):
    caracteres = list(string.ascii_letters)
    if tem_numero:
        caracteres += list(string.digits)
    if tem_simbolo:
        caracteres += list(string.punctuation)

    senha = ""
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
    
    return senha

# Botão para gerar a senha
if st.button("Gerar Senha"):
    senha_gerada = gerar_senha(comprimento, tem_numero, tem_simbolo)
    st.write(f"Sua senha gerada é: {senha_gerada}")
