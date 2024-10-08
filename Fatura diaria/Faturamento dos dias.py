import json

def calcular_faturamento():
    # Ler os dados do arquivo JSON
    with open('faturamento.json') as file:
        dados = json.load(file)

    # Extrair os valores de faturamento
    faturamentos = [registro['valor'] for registro in dados['faturamento']]
    
    # Filtrar os valores para ignorar os dias sem faturamento
    faturamentos_filtrados = [f for f in faturamentos if f > 0]

    # Calcular o menor e o maior valor de faturamento
    menor_faturamento = min(faturamentos_filtrados)
    maior_faturamento = max(faturamentos_filtrados)

    # Calcular a média mensal
    media_mensal = sum(faturamentos_filtrados) / len(faturamentos_filtrados)

    # Contar o número de dias acima da média mensal
    dias_acima_media = sum(1 for f in faturamentos_filtrados if f > media_mensal)

    # Exibir os resultados
    print(f"Menor faturamento do mês: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento do mês: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

# Chamar a função
calcular_faturamento()
