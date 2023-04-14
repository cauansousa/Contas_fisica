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

# CONSTANTES
#lyman = 1 ultravioleta
#balmer = 2 visivel e ultravioleta
#paschen = 3 infravermelho
#brackett = 4 infravermelho
#pfund = 5 infravermelho


#Espectro do Hidrogênio

def espectro(n, i): # correto
  lamb = 1 / (1.097e7 * ((1 / (i*i)) - (1 / (n*n)) ))
  return lamb

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

def descobre_n_lamb(lamb):
  foton = ((h*c) / (lamb))
  ef = (-13.6 - foton)
  n = sqrt(13.6 / abs(ef))
  print("asdasdasda",n)
  return n  

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

print('''
Integrantes:
  Cauan Sousa RA: 24.122.089-6
  Felipe Orlando Lanzara RA: 24.122.055-7
  Pedro Barbosa Ribeiro RA: 24.122.048-2
  ''')

while True:
  op = int(input('''
  1 - Propiedades do átomo de Hidrogênio
  2 - Emissão de fóton pelo H
  3 - Absorção de fóton pelo H
  4 - Espectro do H
  5 - Sair
  '''))
  if op == 1:
    n = int(input('Digite o valor de n: '))
    print('''
    Resultados:
    Rn = {:.3e} m
    Vn = {:.3e} m/s
    Lambda = {:.3e} m
    E = {:.3e} eV
    K = {:.3e} eV
    U = {:.3e} eV
    '''.format(rn(n),vn(n),lambn(n), En(n), Kn(n), Un(n)))
  elif op == 2:
    x = int(input('''
    Você tem:
    1 - ni e nf
    2 - ni e f
    3 - ni e lamb
    4 - nf e f
    5 - nf e lamb
    '''))
    if op == 1:
      n = int(input('Digite o valor de n: '))
      print('''
      Resultados:
      Rn = {:.3e} m
      Vn = {:.3e} m/s
      Lambda = {:.3e} m
      E = {:.3e} eV
      K = {:.3e} eV
      U = {:.3e} eV
      '''.format(rn(n),vn(n),lambn(n), En(n), Kn(n), Un(n)))
      input("Pressione uma tecla para continuar...")
    elif op == 2:
      x = int(input('''
      Você tem:
      1 - ni e nf
      2 - ni e f
      3 - ni e lamb
      4 - nf e f
      5 - nf e lamb
      '''))
      if x == 1:
        ni = int(input('Digite o valor de ni: '))
        nf = int(input('Digite o valor de nf: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        ffóton = {:.3e} Hz
        lambfóton = {:.3e} m
        '''.format(Efotonem(ni, nf), ffotonem(ni, nf), lambfotonem(ni, nf)))
        input("Pressione uma tecla para continuar...")
      elif x == 2:
        ni = int(input('Digite o valor de ni: '))
        f = float(input('Digite o valor de f: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        lambfóton = {:.3e} m
        '''.format(Efotonem(ni, nf_ni_f_em(ni, f)), lambfotonem(ni, nf_ni_f_em(ni, f))))
        input("Pressione uma tecla para continuar...")
      elif x == 3:
        ni = int(input('Digite o valor de ni: '))
        lamb = float(input('Digite o valor de lamb: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        ffóton = {:.3e} Hz
        '''.format(Efotonem(ni, nf_ni_lamb_em(ni, lamb)), ffotonem(ni, nf_ni_lamb_em(ni, lamb))))
        input("Pressione uma tecla para continuar...")
      elif x == 4:
        nf = int(input('Digite o valor de nf: '))
        f = float(input('Digite o valor de f: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        lambfóton = {:.3e} m
        '''.format(Efotonem(ni_nf_f_em(nf, f), nf), lambfotonem(ni_nf_f_em(nf, f), nf)))
        input("Pressione uma tecla para continuar...")
      elif x == 5:
        nf = int(input('Digite o valor de nf: '))
        lamb = float(input('Digite o valor de lamb: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        ffóton = {:.3e} Hz
        '''.format(Efotonem(ni_nf_lamb_em(nf, lamb), nf), ffotonem(ni_nf_lamb_em(nf, lamb), nf)))
        input("Pressione uma tecla para continuar...")
    elif op == 3:
      x = int(input('''
      Você tem:
      1 - ni e nf
      2 - ni e f
      3 - ni e lamb
      4 - nf e f
      5 - nf e lamb
      '''))
      if x == 1:
        ni = int(input('Digite o valor de ni: '))
        nf = int(input('Digite o valor de nf: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        ffóton = {:.3e} Hz
        lambfóton = {:.3e} m
        '''.format(Efotonab(ni, nf), ffotonab(ni, nf), lambfotonab(ni, nf)))
        input("Pressione uma tecla para continuar...")
      elif x == 2:
        ni = int(input('Digite o valor de ni: '))
        f = float(input('Digite o valor de f: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        lambfóton = {:.3e} m
        '''.format(Efotonab(ni, nf_ni_f_ab(ni, f)), lambfotonab(ni, nf_ni_f_ab(ni, f))))
        input("Pressione uma tecla para continuar...")
      elif x == 3:
        ni = int(input('Digite o valor de ni: '))
        lamb = float(input('Digite o valor de lamb: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        ffóton = {:.3e} Hz
        '''.format(Efotonab(ni, nf_ni_lamb_ab(ni, lamb)), ffotonab(ni, nf_ni_lamb_ab(ni, lamb))))
        input("Pressione uma tecla para continuar...")
      elif x == 4:
        nf = int(input('Digite o valor de nf: '))
        f = float(input('Digite o valor de f: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        lambfóton = {:.3e} m
        '''.format(Efotonab(ni_nf_f_ab(nf, f), nf), lambfotonab(ni_nf_f_ab(nf, f), nf)))
      elif x == 5:
        nf = int(input('Digite o valor de nf: '))
        lamb = float(input('Digite o valor de lamb: '))
        print('''
        Resultados:
        Efóton = {:.3e} eV
        ffóton = {:.3e} Hz
        '''.format(Efotonab(ni_nf_lamb_ab(nf, lamb), nf), ffotonab(ni_nf_lamb_ab(nf, lamb), nf)))
        input("Pressione uma tecla para continuar...")
    elif op == 4:
      print('''
      Resultados:
      Efóton = {:.3e} eV
      lambfóton = {:.3e} m
      '''.format(Efotonem(ni, nf_ni_f_em(ni, f)), lambfotonem(ni, nf_ni_f_em(ni, f))))
    elif x == 3:
      ni = int(input('Digite o valor de ni: '))
      lamb = float(input('Digite o valor de lamb: '))
      print('''
      Resultados:
      Efóton = {:.3e} eV
      ffóton = {:.3e} Hz
      '''.format(Efotonem(ni, nf_ni_lamb_em(ni, lamb)), ffotonem(ni, nf_ni_lamb_em(ni, lamb))))
    elif x == 4:
      nf = int(input('Digite o valor de nf: '))
      f = float(input('Digite o valor de f: '))
      print('''
      Resultados:
      Efóton = {:.3e} eV
      lambfóton = {:.3e} m
      '''.format(Efotonem(ni_nf_f_em(nf, f), nf), lambfotonem(ni_nf_f_em(nf, f), nf)))
    elif x == 5:
      nf = int(input('Digite o valor de nf: '))
      lamb = float(input('Digite o valor de lamb: '))
      print('''
      Resultados:
      Efóton = {:.3e} eV
      ffóton = {:.3e} Hz
      '''.format(Efotonem(ni_nf_lamb_em(nf, lamb), nf), ffotonem(ni_nf_lamb_em(nf, lamb), nf)))
  elif op == 3:
    x = int(input('''
    Você tem:
    1 - ni e nf
    2 - ni e f
    3 - ni e lamb
    4 - nf e f
    5 - nf e lamb
    '''))
    if x == 1:
      ni = int(input('Digite o valor de ni: '))
      nf = int(input('Digite o valor de nf: '))
      print('''
      Resultados:
      Efóton = {:.3e} eV
      ffóton = {:.3e} Hz
      lambfóton = {:.3e} m
      '''.format(Efotonab(ni, nf), ffotonab(ni, nf), lambfotonab(ni, nf)))
    elif x == 2:
      ni = int(input('Digite o valor de ni: '))
      f = float(input('Digite o valor de f: '))
      print('''
      Resultados:
      Efóton = {:.3e} eV
      lambfóton = {:.3e} m
      '''.format(Efotonab(ni, nf_ni_f_ab(ni, f)), lambfotonab(ni, nf_ni_f_ab(ni, f))))
    elif x == 3:
      ni = int(input('Digite o valor de ni: '))
      lamb = float(input('Digite o valor de lamb: '))
      print('''
      Resultados:
      Efóton = {:.3e} eV
      ffóton = {:.3e} Hz
      '''.format(Efotonab(ni, nf_ni_lamb_ab(ni, lamb)), ffotonab(ni, nf_ni_lamb_ab(ni, lamb))))
    elif x == 4:
      nf = int(input('Digite o valor de nf: '))
      f = float(input('Digite o valor de f: '))
      print('''
      Resultados:
      Efóton = {:.3e} eV
      lambfóton = {:.3e} m
      '''.format(Efotonab(ni_nf_f_ab(nf, f), nf), lambfotonab(ni_nf_f_ab(nf, f), nf)))
    elif x == 5:
      nf = int(input('Digite o valor de nf: '))
      lamb = float(input('Digite o valor de lamb: '))
      print('''
      Resultados:
      Efóton = {:.3e} eV
      ffóton = {:.3e} Hz
      '''.format(Efotonab(ni_nf_lamb_ab(nf, lamb), nf), ffotonab(ni_nf_lamb_ab(nf, lamb), nf)))
  elif op == 4:
    resp = espectro(int(input('Digite o valor do nível: ')), int(input('''
    Qual equação você quer usar?
    1 - lyman 
    2 - balmer
    3 - paschen
    4 - brackett
    5 - pfund
    ''')))

    print('''
    Resultados:
    lambdA = {:.3e} m
    '''.format(resp))
  elif op == 5:
    break
  else:
    print('Opção inválida!')
