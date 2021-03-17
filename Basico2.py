#FUNÇÕES EM PYTHON

def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

retorno = soma(75,1289)
print(retorno)

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

print (tem_sete_itens("olá pessoa"))

'''
escreva uma função que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa coleção

'''
def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

print (maior([1,2,3,5,7,9,5]))


#TRATAMENTO DE EXCESSÃO 

try:
    a = 1220 / 0
except:
    print("a dvisão por 0 não é possível")


try:
    a = 1220 / 0
except ZeroDivisionError:
    print("a dvisão por 0 não é possível")
except NameError:
    print("a dvisão por 0 não é possível")
except Exception as erro:
    print("aconteceu algum erro, o seguinte: ", erro)
