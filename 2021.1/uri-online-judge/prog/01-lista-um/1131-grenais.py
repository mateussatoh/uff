def novoVencedor(vitoriasInter, vitoriasGremio, empates):
  print("%d grenais" %(vitoriasInter+vitoriasGremio+empates))
  print("Inter:%d" %vitoriasInter)
  print("Gremio:%d" %vitoriasGremio)
  print("Empates:%d" %empates)

  if(vitoriasInter == vitoriasGremio):
    print("Nao houve vencedor")
  else:
    if(vitoriasInter > vitoriasGremio):
        print("Inter venceu mais")
    else:
        print("Gremio venceu mais")

def novoJogo(vitoriasInter, vitoriasGremio, empates):  
  golsInter,golsGremio = list(map(int,input().split()))
  if(golsInter == golsGremio):
      empates += 1
  else:
      if(golsInter < golsGremio):
        vitoriasGremio += 1
      else:
        vitoriasInter += 1
  print("Novo grenal (1-sim 2-nao)")
  escolha = int(input())
  if(escolha == 2):
    novoVencedor(vitoriasInter, vitoriasGremio, empates)
  else:
    novoJogo(vitoriasInter, vitoriasGremio, empates)

novoJogo(0,0,0)