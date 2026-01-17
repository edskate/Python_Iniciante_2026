faturamento =  1000  # Exemplo de valor de faturamento
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas # somar
imposto = faturamento * 0.1 #  multiplicar calcular imposto de 10%
lucro = faturamento - custo - imposto # subtrair custo e imposto do faturamento


print("Faturamento:", faturamento)
print(lucro)
margin_lucro = lucro /  faturamento   # dividir
print(margin_lucro)


restituicao = imposto * 0.1 # calcular restituição de 5% do imposto
print(restituicao)


# Mod resto da divisão

# 10 % 3 

print(10 % 3 )

tempo_em_meses = 160
tempo_em_anos = tempo_em_meses // 12 # divisão inteira
print(tempo_em_anos)
print(tempo_em_meses % 12)
