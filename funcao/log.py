# Funções fornecidas
def calcular_ln(x, iteracoes=100):
    if x <= 0: 
        return float('-inf')  
    e = 2.718
    y = 0.0
    
    for i in range(iteracoes):
        saldo = e**y
        y = y + 2 * (x - saldo) / (x + saldo)
    
    return y

def calcular_log_mudanca_base(numero, base):
    if numero <= 0:
        return "Erro: O número deve ser maior que zero."
    if base <= 0 or base == 1:
        return "Erro: A base deve ser maior que zero e diferente de 1."

    ln_numero = calcular_ln(numero)
    ln_base = calcular_ln(base)
    
    return ln_numero / ln_base

numero = float(input("Digite o número: "))
base = float(input("Digite a base: "))

resultado = calcular_log_mudanca_base(numero, base)
print(f"log_{base}({numero}) -> {resultado}")