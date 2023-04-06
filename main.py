num = int(input())
if num <= 0:
    print('Número inválido')
else:
    primo = True
    contador = 2
    while(contador < num):
        if num % contador == 0:
            primo = False
            break
        contador += 1
    if primo:
        print('Primo')
    else:
        print('Não primo')
