def testeSenha():
  senha = int(input())
  if(senha == 2002):
    print("Acesso Permitido")
  else:
    print("Senha Invalida")
    testeSenha()

testeSenha()