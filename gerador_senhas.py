import time
import string
import random
import streamlit as st

def estimar_tempo_quebra_senha(tamanho_senha, taxa_tentativas_por_segundo):
    # A fórmula assume uma tentativa por segundo
    tentativas_por_segundo = taxa_tentativas_por_segundo
    segundos_por_minuto = 60
    minutos_por_hora = 60
    horas_por_dia = 24
    dias_por_ano = 365

    possibilidades = len(string.ascii_letters) ** tamanho_senha
    segundos_para_quebra = possibilidades / tentativas_por_segundo
    minutos_para_quebra = segundos_para_quebra / segundos_por_minuto
    horas_para_quebra = minutos_para_quebra / minutos_por_hora
    dias_para_quebra = horas_para_quebra / horas_por_dia
    anos_para_quebra = dias_para_quebra / dias_por_ano

    return anos_para_quebra

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
    inicio = time.time()  # Registra o tempo inicial
    senha_gerada = gerar_senha(comprimento, tem_numero, tem_simbolo)
    fim = time.time()  # Registra o tempo final
    tempo_gasto_segundos = fim - inicio  # Tempo em segundos
    tempo_gasto_milissegundos = tempo_gasto_segundos * 1000  # Tempo em milissegundos

    st.write(f"Sua senha gerada é: {senha_gerada}")

    # Exibe uma estimativa do tempo para quebrar a senha por força bruta
    tentativas = 1000000
    tempo_estimado_quebra = estimar_tempo_quebra_senha(comprimento, tentativas)
    st.write(f"Tempo estimado para quebrar senha de tamanho {comprimento} por força bruta com {tentativas} tentativas/s (letras)\n: {tempo_estimado_quebra} anos")

    # Exibe o tempo gasto para gerar a senha em milissegundos
    st.write(f"Tempo gasto para gerar a senha: {tempo_gasto_milissegundos:.4f} milissegundos")
