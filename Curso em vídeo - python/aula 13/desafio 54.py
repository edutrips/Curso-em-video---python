from datetime import date
atual = date.today().year
nasc = int(input('Em que ano a pessoa nasceu? '))
idade = atual - nasc
if idade >=18:
    print('Essa pessoa é de maior')
else:
    print('Essa pessoa é de menor')