#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite algo: ')
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em minúsculas? ', a.islower())
print('Está em maiúsculas? ', a.isupper())
print('Está capitalizada? ', a.istitle())

#nesse código, o 'a' é um objeto, e todo objeto tem características e realiza funcionalidades. Tem atributos e métodos. Os métodos são demonstrados nesse parênteses no final de cada print e todo objeto string tem esses métodos.