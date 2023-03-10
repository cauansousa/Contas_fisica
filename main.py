import scipy.constants as sci
import math


class contas():
  def __init__(self):
    self.c = sci.c
    self.u = sci.mu_0
    self.pi = sci.pi

  def show(self, em, bm, i, f, lamb, k, omg):
    print(f'EM: {em:.3}')
    print(f'BM: {bm:.3}')
    print(f'INTEN: {i:.3}')
    print(f'FREQ: {f:.3}')
    print(f'LAMB: {lamb:.3}')
    print(f'K: {k:.3}')
    print(f'OMG: {omg:.3}')

  def Em(self, em):
    bm = em / self.c
    i = (em * em) / (2 * self.u * self.c)
    self.show(em, bm, i, 0.0, 0.0, 0.0, 0.0)

  def Bm(self, bm):
    em = bm / self.c
    i = pow(bm * self.c, 2) / (2 * self.u * self.c)
    self.show(em, bm, i, 0.0, 0.0, 0.0, 0.0)

  def inten(self, i):
    em = math.sqrt(i * 2 * self.u * self.c)
    bm = math.sqrt(i * 2 * self.u * self.c) / self.c
    self.show(em, bm, i, 0.0, 0.0, 0.0, 0.0)

  def freq(self, f):
    lamb = self.c / f
    k = (2 * self.pi * f) / self.c
    omg = (2 * self.pi * f)
    self.show(0.0, 0.0, 0.0, f, lamb, k, omg)

  def lamb(self, lamb):
    f = self.c / lamb
    k = (2 * self.pi) / lamb
    omg = (2 * self.pi * self.c) / lamb
    self.show(0.0, 0.0, 0.0, f, lamb, k, omg)

  def k(self, k):
    f = (self.c * k) / (2 * self.pi)
    lamb = (2 * self.pi) / k
    omg = self.c * k
    self.show(0.0, 0.0, 0.0, f, lamb, k, omg)

  def omg(self, omg):
    f = omg / (2 * self.pi)
    lamb = (2 * self.pi * self.c) / omg
    k = omg / self.c
    self.show(0.0, 0.0, 0.0, f, lamb, k, omg)

conta = contas()

while True:
  print('''
  1 - EM
  2 - BM
  3 - INTEN
  4 - FREQ
  5 - LAMB
  6 - K
  7 - OMG
  ''')
  op = int(input('Opção: '))
  if op == 1:
    val = float(input('EM: '))
    exp = int(input('Expoente: '))
    conta.Em(val * pow(10, exp))
  elif op == 2:
    val = float(input('EM: '))
    exp = int(input('Expoente: '))
    conta.Bm(val * pow(10, exp))    
  elif op == 3:
    val = float(input('INTEN: '))
    exp = int(input('Expoente: '))
    conta.inten(val * pow(10, exp))
  elif op == 4:
    val = float(input('FREQ: '))
    exp = int(input('Expoente: '))
    conta.freq(val * pow(10, exp))
  elif op == 5:
    val = float(input('LAMB: '))
    exp = int(input('Expoente: '))
    conta.lamb(val * pow(10, exp))
  elif op == 6:
    val = float(input('K: '))
    exp = int(input('Expoente: '))
    conta.k(val * pow(10, exp))
  elif op == 7:
    val = float(input('OMG: '))
    exp = int(input('Expoente: '))
    conta.omg(val * pow(10, exp))
  else:
    print('Opção inválida')
    continue

  if input('Deseja continuar? (s/n): ') == 'n':
    break

