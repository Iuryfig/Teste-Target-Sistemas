
def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida 
    return invertida

texto = input("Digite uma string para inverter: ")

texto_invertido = inverter_string(texto)
print(f"A string invertida é: {texto_invertido}")
