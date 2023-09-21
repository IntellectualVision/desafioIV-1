import random
import string

def gerar_senha(comprimento, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Gerador de Senhas Aleatórias")
    comprimento = int(input("Informe o comprimento desejado para a senha: "))
    incluir_numeros = input("Incluir números na senha? (S/N): ").strip().lower() == 's'
    incluir_simbolos = input("Incluir símbolos na senha? (S/N): ").strip().lower() == 's'

    senha = gerar_senha(comprimento, incluir_numeros, incluir_simbolos)
    print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()