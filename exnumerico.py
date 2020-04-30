# O usuario digita um numero inteiro n e o programa executa uma lista de  'i' [1,2,3 ...n] em linhas separadas, 
# se um numero é divisivel por 3 e não por 5 ele mostra Fizz; se for divisivel por 5 e não por 3 ele mostra Buzz, se for divisivelpor ambos
# ele mostra FizzBuzz e se não for divisivel por nenhum deles ele mostra o numero 'i' da sequencia.

#using loop while
n = int(input())
cont = 0
while cont <= n:
    cont += 1
    if cont % 3 == 0 and cont % 5 == 0:
        print('FizzBuzz')
    if cont % 3 == 0 and cont % 5 != 0:
        print('Fizz')
    if cont % 5 == 0 and cont % 3 != 0:
        print('Buzz')
    if cont > n:
        break
    if cont % 3 != 0 and cont % 5 != 0:
        print(cont)

# using looping for
n = int(input())
for cont in range(1,n+1):
    if cont % 3 == 0 and cont % 5 == 0:
        print('FizzBuzz')
    if cont % 3 == 0 and cont % 5 != 0:
        print('Fizz')
    if cont % 5 == 0 and cont % 3 != 0:
        print('Buzz')
    if cont > n:
        break
    if cont % 3 != 0 and cont % 5 != 0:
        print(cont)

