import json

def calcular_faturamento():
    
    with open('faturamento.json') as file:
        dados = json.load(file)

    faturamentos = [registro['valor'] for registro in dados['faturamento']]

    faturamentos_filtrados = [f for f in faturamentos if f > 0]

    menor_faturamento = min(faturamentos_filtrados)
    maior_faturamento = max(faturamentos_filtrados)

    media_mensal = sum(faturamentos_filtrados) / len(faturamentos_filtrados)

    dias_acima_media = sum(1 for f in faturamentos_filtrados if f > media_mensal)
                           
    print(f"Menor faturamento do mês: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento do mês: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

calcular_faturamento()