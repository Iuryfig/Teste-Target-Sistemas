def faturamento_dos_dias(dia_faturamento):
    
    menor_faturamento = min(dia_faturamento)
    maior_faturamento = max(dia_faturamento)

    media_mensal = sum(dia_faturamento) / len(dia_faturamento)
    dias_acima_media = sum(1 for faturamento in dia_faturamento if faturamento > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

faturamento_diario = [1500, 2300, 1000, 3200, 2500, 1800, 2100, 4000, 3100, 2900, 0, 1200, 220]
                      
menor, maior, acima_media = faturamento_dos_dias(faturamento_diario)

print(f"O menor valor de faturamento ocorrido em um dia do mês: R$ {menor:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {acima_media}")
