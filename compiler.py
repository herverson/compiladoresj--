reservadas = ['if', 'else', 'while', 'System.out.println', 'this', 'new', 'boolean', 'class', 'extends', 'public', 'static', 'void', 'main', 'return', 'int']
pontuacao = ['.', '(', ')', '[', ']', '{', '}', ',', ';']
operadores = ['==', '&&', '-', '+', '*', '!', '=', '!=', '<', '>']
numeros = "0123456789"
validateVariavel = "0123456789_"
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def geradorTokens(token):
  print(token)
  if (token in reservadas or token in pontuacao or token in operadores):
    return "<" + token + ", >"
  
  index = 0
  totalTimesCountNumber = 0
  totalTimesIterate = 0
  number = ""
  for i in token:
    if i in numeros:
      number += i
      totalTimesCountNumber += 1
    totalTimesIterate += 1
  
  if (totalTimesCountNumber == totalTimesIterate):
    # identificou numero, portanto, deve parar execucao
    return "<num, " + number + ">"
  
  primeiraLeitura = True
  index = 0
  variavel = ""
  for i in token:
    if i in letras:
      primeiraLeitura = False
      variavel += i
    # Valida o caracter como numero ou underline (_)
    elif i in validateVariavel:
      # Se iniciar com numero ou underline e um erro
      if primeiraLeitura:
        raise ValueError("ERRO LÉXICO: " + token)
      primeiraLeitura = False
      variavel += i
    else:
      raise ValueError("ERRO LÉXICO: " + token)
  
  # variaveis  
  idIndex = variavel
  idIndexString = idIndex
  
  return "<Identifier, " + idIndexString + ">"

def removeComments():
  pass


print(geradorTokens('System.out.println'))

