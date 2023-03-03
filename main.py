import scipy.constants as sci
import math


class contas():
  c = sci.c
  u = sci.mu_0
  pi = sci.pi

  #print(f'{c:.4e}')

  def Em(self, em):
    bm = em / self.c
    i = (em * em) / (2 * self.u * self.c)
    return bm, i

  def Bm(self, bm):
    em = bm / self.c
    i = pow(bm * self.c, 2) / (2 * self.u * self.c)
    return em, i

  def inten(self, i):
    em = math.sqrt(i * 2 * self.u * self.c)
    bm = math.sqrt(i * 2 * self.u * self.c) / self.c
    return em, bm

  def freq(self, f):
    lamb = self.c / f
    k = (2 * self.pi * f) / self.c
    omg = (2 * self.pi * f)
    return lamb, k, omg

  def lamb(self, lamb):
    f = self.c / lamb
    k = (2 * self.pi) / lamb
    omg = (2 * self.pi * self.c) / lamb
    return f, k, omg

  def k(self, k):
    f = (self.c * k) / (2 * self.pi)
    lamb = (2 * self.pi) / k
    omg = self.c * k
    return f, lamb, omg

  def omg(self, omg):
    f = omg / (2 * self.pi)
    lamb = (2 * self.pi * self.c) / omg
    k = omg / self.c
    return f, lamb, k


conta = contas()

# f, k, omg = conta.lamb(4.76 * pow(10, -11))
# print(f'{f:.3}')
# print(f'{k:.3}')
# print(f'{omg:.3}')

# lamb, k, omg = conta.freq(1.02 * pow(10, 11))

# print(f'{lamb:.3}')
# print(f'{k:.3}')
# print(f'{omg:.3}')
