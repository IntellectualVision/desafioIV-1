import sys
import time
import string
import random
import streamlit as st

def estimar_tempo_quebra_senha(tamanho_senha, taxa_tentativas_por_segundo, tem_numero, tem_simbolo):
    # A fórmula assume uma tentativa por segundo
    tentativas_por_segundo = taxa_tentativas_por_segundo
    segundos_por_minuto = 60
    minutos_por_hora = 60
    horas_por_dia = 24
    dias_por_ano = 365
    overflow = False

    tamanho_caracteres = len(string.ascii_letters)

    if tem_numero:
        tamanho_caracteres += len(string.digits)
    if tem_simbolo:
        tamanho_caracteres += len(string.punctuation)

    try:
        possibilidades = tamanho_caracteres ** tamanho_senha
        segundos_para_quebra = possibilidades / tentativas_por_segundo
        minutos_para_quebra = segundos_para_quebra / segundos_por_minuto
        horas_para_quebra = minutos_para_quebra / minutos_por_hora
        dias_para_quebra = horas_para_quebra / horas_por_dia
        anos_para_quebra = dias_para_quebra / dias_por_ano
    except OverflowError:
        overflow = True
        anos_para_quebra = sys.float_info.max

    return (overflow, anos_para_quebra)

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

    senha = random.choices(caracteres, k=comprimento)
    
    return ''.join(senha)

# Botão para gerar a senha
if st.button("Gerar Senha"):
    inicio = time.time()  # Registra o tempo inicial
    senha_gerada = gerar_senha(comprimento, tem_numero, tem_simbolo)
    fim = time.time()  # Registra o tempo final
    tempo_gasto_segundos = fim - inicio  # Tempo em segundos
    tempo_gasto_milissegundos = tempo_gasto_segundos * 1000  # Tempo em milissegundos

    st.write(f"Sua senha gerada é:")
    st.code(senha_gerada)

    tentativas = 1000000
    (limite_maximo, tempo_estimado_quebra) = estimar_tempo_quebra_senha(comprimento, tentativas, tem_numero, tem_simbolo)
    
    # Exibe uma estimativa do tempo para quebrar a senha por força bruta
    st.write(f"Tempo estimado para quebrar senha de tamanho {comprimento} por força bruta com {tentativas} tentativas/s:")
    st.code(f"{'Mais que' if limite_maximo else ''} {tempo_estimado_quebra:.2e} {'anos' if tempo_estimado_quebra >= 2 else 'ano'}")

    # Exibe o tempo gasto para gerar a senha em milissegundos
    st.write(f"Tempo gasto para gerar a senha: {tempo_gasto_milissegundos:.4f} milissegundos")
