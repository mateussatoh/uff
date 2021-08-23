valor = float(input())

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
  valor = valor - notasUm*1
  notasUm=float('%.2f'% notasUm)
  valor=float('%.2f'% valor)
  m50 = valor // 0.5
  valor = valor - m50*0.5
  m50=float('%.2f'% m50)
  valor=float('%.2f'% valor)
  m25 = valor // 0.25   
  valor = valor - m25*0.25
  m25=float('%.2f'% m25)
  valor=float('%.2f'% valor)
  m10 = valor // 0.10
  valor = valor - m10*0.10
  m10=float('%.2f'% m10)
  valor=float('%.2f'% valor)
  m5 = valor // 0.05
  valor = valor - m5*0.05
  m5=float('%.2f'% m5)
  valor=float('%.2f'% valor)
  m1 = valor * 100
  m1=float('%.2f'% m1)
  valor=float('%.2f'% valor)
  return [notasCem, notasCinquenta, notasVinte,notasDez, notasCinco, notasDois, notasUm, \
          m50 ,m25 ,m10 ,m5 ,m1 ]

print('NOTAS:')
print('%d nota(s) de R$ 100.00' %decomporValor(valor)[0])
print('%d nota(s) de R$ 50.00' %decomporValor(valor)[1])
print('%d nota(s) de R$ 20.00' %decomporValor(valor)[2])
print('%d nota(s) de R$ 10.00' %decomporValor(valor)[3])
print('%d nota(s) de R$ 5.00' %decomporValor(valor)[4])
print('%d nota(s) de R$ 2.00' %decomporValor(valor)[5])
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' %decomporValor(valor)[6])
print('%d moeda(s) de R$ 0.50' %decomporValor(valor)[7])
print('%d moeda(s) de R$ 0.25' %decomporValor(valor)[8])
print('%d moeda(s) de R$ 0.10' %decomporValor(valor)[9])
print('%d moeda(s) de R$ 0.05' %decomporValor(valor)[10])
print('%d moeda(s) de R$ 0.01' %decomporValor(valor)[11])

