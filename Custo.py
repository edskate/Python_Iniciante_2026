print("=" * 40)
print("   SISTEMA DE CONTROLE FINANCEIRO")
print("=" * 40)

# Entrada de dados
projeto = input("Nome do projeto ou show: ")

faturamento = float(input("Digite o faturamento (R$): "))
custo = float(input("Digite o custo total (R$): "))

# Cálculos
lucro = faturamento - custo

# Resultado
print("\n📊 RELATÓRIO FINANCEIRO")
print("-" * 40)
print("Projeto:", projeto)
print("Faturamento: R$", faturamento)
print("Custo:       R$", custo)
print("Lucro:       R$", lucro)

# Análise
if lucro > 0:
    print("✅ Situação: LUCRO")
elif lucro < 0:
    print("⚠️ Situação: PREJUÍZO")
else:
    print("⚖️ Situação: EMPATE")

print("-" * 40)
print("Sistema finalizado com sucesso ✅")

