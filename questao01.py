def questao01():
      entrada = input("Digite os números desejados com espaço: ")

      lista = [int(n) for n in entrada.split()]
      output = []
      for n in lista:
            if n % 2 != 0:
                  output.append(n)

      if output:
        print("Os números impares são: ", output)

questao01()


