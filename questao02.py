def questao02():
      entrada = input("Digite os números desejados com espaço:")

      lista = [int(n) for n in entrada.split()]
      output = []

      for n in lista:
                  primo = True
                  if n> 1:
                        for y in range(2,n):
                              if n % y == 0:
                                    primo = False
                                    break
                        if primo:
                              output.append(n)

      if output:
            print("números primos são: ", output)

      else:
            print("Não existem números primos")

questao02()

