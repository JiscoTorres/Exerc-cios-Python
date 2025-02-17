d = {'c':97, 'a':96, 'b':98}

for _ in sorted(d):
  print(d[_], end='')

# Qual a resposta correta:
#   A. 97 96 98
#   B. 98 97 96
#   C. ERROR
#   D. 96 98 97


# Resposta letra "D". - Pois ele irá organizar os as respostas das variáveis indicadas pelas letras a,b & c apartir da ordem alfabética. Primeiro A depoi B e por fim c. 



#------------------------------------------------------#

a= 100.1342
print(round(a, 3)) 

# Qual a resposta correta:
#   A. 100.134
#   B. 100.1342
#   C. 100.3
#   D. None of above. 
    

#Resposta letra "A". - Nesse exemplo, o valor de a(100.1342) será printado na tela; porém, com o comando round aparecerão somente os 3 primeiros números após a virgula. O argumento diz quantas casas decimais exibir. 


#--------------------------------------------------------#

d={0:'a', 1:'b', 2:'c'}
for x in d.keys():
  print(d[x])

# Qual a resposta correta:
#   A. 0  1  2
#   B. a  b  c
#   C. 0a  1b  2c
#   D. None of the mentioned.


# Resposta letra "B". - O método keys() retorna como chaves de um dicionário, que nesse caso será utilizado como chaves novamente no laço para retornar os valores!


#--------------------------------------------------------#

a=('p'*2)*3
b=('p'*3)*2

print(a==b)


# Qual a resposta correta que aparecerá no console:
#   A. TRUE
#   B. FALSE
#   C. ERROR
#   D. None of these.


#Resposta letra "A". - Esse "==" irá pedir a confirmação para saber se a afirmativa dos dois serem exatamente igual está correta. A resposta seria a repitição de 'p' 6 vezes em ambas as variaveis, ou seja, pppppp.



#--------------------------------------------------------#

list1= [11, 2, 23]
list2= [2, 11, 23]
print(list1==list2)

# Qual a resposta correta que aparecerá no console:
#   A. ERROR
#   B. TRUE
#   C. FALSE
#   D. None of these.

# Resposta letra "C". - Visto que as sequências dos números apresentadas nas listas não seguem um padrão igual. 
