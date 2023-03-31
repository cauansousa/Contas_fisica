from math import sqrt





# PROPRIEDADES DO ÁTOMO DE H
# ENTRADA PELO TECLADO: n
# SAÍDA: rn, vn, lambn, Kn, Un, En

# rn = raio da órbita de ordem n no modelo de Bohr
# vn = velocidade orbital na órbita de ordem n no modelo de Bohr
# lambn = comprimento de onda de De Broglie de uma partícula
# Kn = energia cinética no modelo de Bohr
# Un = energia potencial no modelo de Bohr
# En = energias totais no modelo de Bohr

# eo = constante elétrica
# n = número quântico principal (n = 1, 2, 3 ...)
# h = constante de Planck
# m = massa do elétron
# e = módulo de carga do elétron

h = 6.6262e-34
pi = 3.1415
c = 3e8
R = 1.097e7


def rn(n): # correto
  rn = pow(n, 2) * 5.29e-11
  return rn

def vn(n): # correto
  vn = 2.19e6 / n
  return vn

def lambn(n): # correto
  lambn = 6.626e-34 / (9.109e-31 * (2.19e6 / n))
  return lambn
 
def Kn(n): # correto
  Kn = 13.6 / (pow (n, 2))
  return Kn

def Un(n): # correto
  Un = -27.2 / (pow(n, 2))
  return Un

def En(n): # correto
  En = -13.6 / (pow(n, 2))
  return En

  

# ABSORÇÃO DE FÓTON PELO H
# ENTRADA: ninicial, nfinal
# SAÍDA: Efóton, ffóton, lambfóton

# Efóton = energia de um fóton
# ffóton = frequência de onda de um fóton
# lambfóton = comprimento de onda de um fóton
  
def Efotonab(ni, nf): # correto
  a = (1.097e7 / (ni*ni)) - (1.097e7 / (nf*nf))
  lambfoton = 1 / a
  Efoton = (4.136e-15 * 3e8) / lambfoton
  return Efoton
  
def ffotonab(ni, nf): # correto
  a = (1.097e7 / (ni*ni)) - (1.097e7 / (nf*nf))
  lambfoton = 1 / a
  ffoton = 3e8 / lambfoton
  return ffoton

def lambfotonab(ni, nf): # correto
  a = (1.097e7 / (ni*ni)) - (1.097e7 / (nf*nf))
  lambfoton = 1 / a
  return lambfoton


# EMISSÃO DE FÓTON PELO H
# ENTRADA: ninicial, nfinal
# SAÍDA: Efóton, ffóton, lambfóton

# Efóton = energia de um fóton
# ffóton = frequência de onda de um fóton
# lambfóton = comprimento de onda de um fóton

def Efotonem(ni, nf): # correto
  a = (1.097e7 / (nf*nf)) - (1.097e7 / (ni*ni))
  lambfoton = 1 / a
  Efoton = (4.136e-15 * 3e8) / lambfoton
  return Efoton
  
def ffotonem(ni, nf): # correto
  a = (1.097e7 / (nf*nf)) - (1.097e7 / (ni*ni))
  lambfoton = 1 / a
  ffoton = 3e8 / lambfoton
  return ffoton

def lambfotonem(ni, nf): # correto
  a = (1.097e7 / (nf*nf)) - (1.097e7 / (ni*ni))
  lambfoton = 1 / a
  return lambfoton



# ABSORÇÃO DE FÓTON PELO H
# ENTRADA: ninicial e f ou lamb
# SAÍDA: nf

def nf_ni_f_ab(ni, f): # correto
  Einicial = -13.6/(ni*ni)
  Efoton = 4.136e-15 * f
  Efinal = Efoton + Einicial
  nf = sqrt(-13.6/Efinal)
  return round(nf)

def nf_ni_lamb_ab(ni, lamb): # correto
  Einicial = -13.6/(ni*ni)
  f = c / lamb
  Efoton = 4.136e-15 * f
  Efinal = Efoton + Einicial
  nf = sqrt(-13.6/Efinal)
  return round(nf)



# EMISSÃO DE FÓTON PELO H
# ENTRADA: nfinal e f ou lamb
# SAÍDA: ni

def ni_nf_f_ab(nf, f): # correto
  Efinal = -13.6 / (nf*nf)
  Efoton = 4.136e-15 * f
  Einicial = Efinal - Efoton
  ni = sqrt(-13.6/Einicial)
  return round(ni)

def ni_nf_lamb_ab(nf, lamb): # correto
  Efinal = -13.6 / (nf*nf)
  f = c / lamb
  Efoton = 4.136e-15 * f
  Einicial = Efinal - Efoton
  ni = sqrt(-13.6/Einicial)
  return round(ni)



# ABSORÇÃO DE FÓTON PELO H
# ENTRADA: ninicial e f ou lamb
# SAÍDA: nf

def nf_ni_f_em(ni, f): # correto
  Einicial = -13.6/(ni*ni)
  Efoton = 4.136e-15 * f
  Efinal = Einicial - Efoton
  nf = sqrt(-13.6/Efinal)
  return round(nf)

def nf_ni_lamb_em(ni, lamb): # correto
  Einicial = -13.6/(ni*ni)
  f = c / lamb
  Efoton = 4.136e-15 * f
  Efinal = Einicial - Efoton
  nf = sqrt(-13.6/Efinal)
  return round(nf)
  


# EMISSÃO DE FÓTON PELO H
# ENTRADA: nfinal e f ou lamb
# SAÍDA: ni

def ni_nf_f_em(nf, f): # correto
  Efinal = -13.6 / (nf*nf)
  Efoton = 4.136e-15 * f
  Einicial = Efinal + Efoton
  ni = sqrt(-13.6/Einicial)
  return round(ni)

def ni_nf_lamb_em(nf, lamb): # correto
  Efinal = -13.6 / (nf*nf)
  f = c / lamb
  Efoton = 4.136e-15 * f
  Einicial = Efinal + Efoton
  ni = sqrt(-13.6/Einicial)
  return round(ni)


a = nf_ni_lamb_em(3, 102.6397e-9)
print(a)
#print(f'a: {a:.3}')

while True:
