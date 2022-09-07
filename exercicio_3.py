#EXPONENCIAL PELA SÉRIE DE TAYLOR

def somatorio(x, n):
  serie = 0
  for i in range(n+1):
    serie += (x**i)/fatorial(i)   
  return serie

def fatorial(i):
  resultado = 1
  for n in range(1, i+1):
    resultado *= n
  return resultado

n = int(input("Digite o número de termos: "))   
x = int(input("Digite o valor do exponencial: "))

print("\n")

print("O valor de e^{} é: {}".format(x, somatorio(x, n)))
