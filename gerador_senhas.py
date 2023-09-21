from random import randint


CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMEROS = "1234567890"
ESPECIAIS = r" \"!#$%&'()*+,-./:;<=>?@[]^_`{|}~"

senha_amostra = CARACTERES
senha = ""


def selecionar_tipo(senha_tipo, conjunto):
    if senha_tipo == 'S': return senha_amostra + conjunto
    if senha_tipo == 'N': return senha_amostra
    print("Error input inválido")
    return senha_amostra



senha_tamanho = int(input("informe o tamanho desejado para sua senha: "))

senha_numerica = input("Incluir números? (S/N): ").strip().upper()
senha_amostra = selecionar_tipo(senha_numerica, NUMEROS)

senha_simbolica = input("Incluir símbolos? (S/N): ").strip().upper()
senha_amostra = selecionar_tipo(senha_simbolica, ESPECIAIS)



for x in range(senha_tamanho):
    senha += senha_amostra[randint(0, len(senha_amostra) - 1)]

print(f"Sua senha está pronta: {senha} \n guarde-a em um lugar seguro!")

