def fibonacci():
    """
    Retorna uma lista com sequencia de fibonacci
    :return: Fibonacci_list
    """
    t1 = 0
    t2 = 1
    fib_list = [t1, t2]
    cont = 3
    while cont <= 100:
        aux = t1 + t2
        fib_list.append(aux)
        t1 = t2
        t2 = aux
        cont += 1
    return fib_list


num = int(input('informe um numero: '))
fibonacci_sequence = fibonacci()

# verifica se o numero pertence ou nao a sequencia em um range de 0 a 100
if num in fibonacci_sequence:
    print(' SIM! O numero informado pertence a sequência de Fibonacci')
else:
    print(' NÃO! O numero informado não pertence a sequência de Fibonacci')


