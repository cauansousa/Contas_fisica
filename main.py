import scipy.constants as sci
import math


class contas():
  def __init__(self):
    self.c = sci.c
    self.u = sci.mu_0
    self.pi = sci.pi

  def show(self, em, bm, i, f, lamb, k, omg):
    print(f'EM: {em:.3} V/m')
    print(f'BM: {bm:.3} T')
    print(f'INTENSIDADE: {i:.3} W/m²')
    print(f'FREQ: {f:.3} Hz')
    print(f'LAMB: {lamb:.3} m')
    print(f'NÚMERO DE ONDA: {k:.3} m⁻¹')
    print(f'OEMGA: {omg:.3} rad/s')

  def Em(self, em):
    bm = em / self.c
    i = (em * em) / (2 * self.u * self.c)
    self.show(em, bm, i, 0.0, 0.0, 0.0, 0.0)

  def Bm(self, bm):
    em = bm * self.c
    i = pow(bm, 2) * self.c/ (2 * self.u)
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
  Escolha qual variável você possuir:

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
    conta.Em(float(input('Valor:')))
  elif op == 2:
    conta.Bm(float(input('Valor:')))    
  elif op == 3:
    conta.inten(float(input('Valor:')))
  elif op == 4:
    conta.freq(float(input('Valor:')))
  elif op == 5:
    conta.lamb(float(input('Valor:')))
  elif op == 6:
    conta.k(float(input('Valor:')))
  elif op == 7:
    conta.omg(float(input('Valor:')))
  else:
    print('Opção inválida')
    continue

  if input('Deseja continuar? (s/n): ') == 'n':
    break

