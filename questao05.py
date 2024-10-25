def questao05():
      entrada = input("Escreva seu nome e sua idade:")
      tupla = []
      for pessoa in entrada.split(";"):
            nome, idade = pessoa.split(",")
            tupla.append((nome,int(idade)))
      
      ordem = sorted(tupla)
      print("Lista de pessoas ordenada:", ordem)

questao05()