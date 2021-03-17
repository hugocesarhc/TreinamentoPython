nome = "hugo"
idade = 28
cidade = "brasília"

print(nome, "tem", idade, "anos", "e mora em", cidade) #em python posso concatenar usando vírgulas, mas posso fazer com "+" como no JAVA também

organizado = nome, idade, cidade

print(organizado)



# hashtag faz comentário sd eu uma linha no python
'''
dentro de 3 aspas simples eu consigo fazer um comentário
com mais de uma linha dentro do espaço das aspas
'''

nome = input("Qual o seu nome?")
idade = input("Qual a sua idade?")
documento = input("qual o seu documento?")
end = input("qual o seu endereço?")

print("Prezado,", nome, "de idade", idade, "anos", "série de documento", documento, "e endereço:",
      end, "solicitamos que refaça suas atividades")
      
#condicional
if (a > b) and (b > c):
    print('a contagem segue normal')
elif (a < c) or (c < b):
    print('contagem bagunçada')
else:
    print('contagem errada')
    
    
#LISTAS E STRINGS

frase = 'olá, tudo bem?'
listas_nomes = ['hugo', 'elirio', 'joão', 'alexandre', 'lucas', 'pedro', 'edu', 'pedro', 'Luisa', 'Beatriz']

'''
Se eu queiser determinar intervalos de busca dentro do python, eu preciso usar ":" os dois pontos
para buscar o ultimo item da posição da lista, ou seja, o ultimo indície basta digitar "-1"

'''
listas_nomes.append('Rafael') # insere um nome na lista, na ultima posição
listas_nomes.remove('hugo') # remove um nome da lista
listas_nomes.clear() #limpa a lista
listas_nomes.insert(2, 'Léo') #insere um nome na lista na posição que eu selecionar
