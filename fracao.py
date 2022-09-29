# TAD
# Tipo Abstrato de Dados - orientação de dados é um exemplo

def mdc(a,b):
  while b != 0:
    r = a%b
    a = b
    b = r
  return a

class Fracao: #estrutura que está criando
  denominador = 1
  numerador = 1

  def __init__(self, numerador, denominador): 
   self.numerador = numerador
   self.denominador = denominador

  def add(self, fracao):  #self = this em outras linguagens
    num = (self.numerador * fracao.denominador) + (fracao.numerador * self.denominador) 
    den = self.denominador * fracao.denominador
    return Fracao(num, den)

  def solve(self):
    return self.numerador/self.denominador

  def sub(self, fracao):
    num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador) 
    den = self.denominador * fracao.denominador
    return Fracao(num, den)

  def mul(self, fracao):
    num = self.numerador * fracao.numerador
    den = self.denominador * fracao.denominador
    return Fracao(num, den)

  def simplify(self):
    if self.numerador == 0:
      return f"{int(self.numerador)}/{int(self.denominador)}"
    elif self.denominador == 0:
      return f"{self.numerador}"
    else:
      d = mdc(self.numerador,self.denominador)
      return f"{int(self.numerador//d)}/{int(self.denominador//d)}"

fracao1 = Fracao(3,6) #É como se fosse 1/2, instancia o objeto
fracao2 = Fracao(3,9)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.mul(fracao2)

print(f"fracao1: {fracao1.simplify()}")
print(f"fracao2: {fracao2.simplify()}")
print(f"Soma: {fracao3.simplify()}")
print(f"Subtração: {fracao4.simplify()}")
print(f"Multiplicação: {fracao5.simplify()}")