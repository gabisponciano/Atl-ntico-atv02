def questao03():

      entrada01 = input("Digite os números com espaço:")
      lista01 = [int(n) for n in entrada01.split()]

      entrada02 = input("Digite os números com espaço:")
      lista02 = [int(x) for x in entrada02.split()]

      output = []

      for n in lista01:
            if n not in lista02:
                  output.append(n)

      for x in lista02:            
            if x not in lista01:
                  output.append(x)

      if output:
            print("Os números não repetidos são: ", output)
      else:
            print("As listas são iguais")

questao03()