valor = int(input())

print(valor)

def decomporValor(valor):
  notasCem = valor // 100
  valor =valor - 100 * notasCem
  notasCinquenta = valor // 50
  valor =valor - 50 * notasCinquenta
  notasVinte = valor // 20
  valor =valor - 20 * notasVinte
  notasDez = valor // 10
  valor =valor - 10 * notasDez
  notasCinco = valor // 5
  valor =valor - 5 * notasCinco
  notasDois = valor // 2
  valor =valor - 2 * notasDois
  notasUm = valor // 1
  return [notasCem, notasCinquenta, notasVinte,notasDez, notasCinco, notasDois, notasUm]
    

print('%d nota(s) de R$ 100,00' %decomporValor(valor)[0])
print('%d nota(s) de R$ 50,00' %decomporValor(valor)[1])
print('%d nota(s) de R$ 20,00' %decomporValor(valor)[2])
print('%d nota(s) de R$ 10,00' %decomporValor(valor)[3])
print('%d nota(s) de R$ 5,00' %decomporValor(valor)[4])
print('%d nota(s) de R$ 2,00' %decomporValor(valor)[5])
print('%d nota(s) de R$ 1,00' %decomporValor(valor)[6])