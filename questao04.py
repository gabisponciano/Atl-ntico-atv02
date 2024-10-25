def questao04():
      entrada = input("Digite os números com espaço:")
      lista = [int(n) for n in entrada.split()]
      
      output = sorted(lista)
      
      print(output[-2])

questao04()