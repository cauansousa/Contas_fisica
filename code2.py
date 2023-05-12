from math import sqrt

# Estado fundamental = 1

# Série de Lyman - nf = 1
# Série de Balmer - nf = 2
# Série de Paschen - nf = 3
# Série de Brackett - nf = 4
# Série de Pfund - nf = 5

# Absorção - vai no n menor pro n maior
# Emissão - vai do n maior pro n menor
# estado excitado = n + 1 (terceiro estado excitado - n = 4)

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

# CONSTANTES
#lyman = 1 ultravioleta
#balmer = 2 visivel e ultravioleta
#paschen = 3 infravermelho
#brackett = 4 infravermelho
#pfund = 5 infravermelh

h = 6.6262e-34  # so usa quando tem massa na conta
h2 = 4.136e-15
pi = 3.1415
c = 3e8
R = 1.097e7

#Calcular menor frequencia significa o maior comprimento de onda, logo, soma 1 no n
#Calcular maior frequencia significa o menor comprimento de onda, logo, substitui N por 0, sendo assim, ignorar o n

def espectro(n, i):  # correto
  lamb = 1 / (1.097e7 * ((1 / (i * i)) - (1 / (n * n))))
  return lamb - 1


def rn(n):  # correto
  rn = pow(n, 2) * 5.29e-11
  return rn


def vn(n):  # correto
  vn = 2.19e6 / n
  return vn


def lambn(n):  # correto
  lambn = 6.626e-34 / (9.109e-31 * (2.19e6 / n))
  return lambn


def Kn(n):  # correto
  Kn = 13.6 / (pow(n, 2))
  return Kn


def Un(n):  # correto
  Un = -27.2 / (pow(n, 2))
  return Un


def En(n):  # correto
  En = -13.6 / (pow(n, 2))
  return En


# ABSORÇÃO DE FÓTON PELO H
# ENTRADA: ninicial, nfinal
# SAÍDA: Efóton, ffóton, lambfóton

# Efóton = energia de um fóton
# ffóton = frequência de onda de um fóton
# lambfóton = comprimento de onda de um fóton


def Efotonab(ni, nf):  # correto
  a = (1.097e7 / (ni * ni)) - (1.097e7 / (nf * nf))
  lambfoton = 1 / a
  Efoton = (4.136e-15 * 3e8) / lambfoton
  return Efoton


def ffotonab(ni, nf):  # correto
  a = (1.097e7 / (ni * ni)) - (1.097e7 / (nf * nf))
  lambfoton = 1 / a
  ffoton = 3e8 / lambfoton
  return ffoton


def lambfotonab(ni, nf):  # correto
  a = (1.097e7 / (ni * ni)) - (1.097e7 / (nf * nf))
  lambfoton = 1 / a
  return lambfoton


# EMISSÃO DE FÓTON PELO H
# ENTRADA: ninicial, nfinal
# SAÍDA: Efóton, ffóton, lambfóton

# Efóton = energia de um fóton
# ffóton = frequência de onda de um fóton
# lambfóton = comprimento de onda de um fóton


def Efotonem(ni, nf):  # correto
  a = (1.097e7 / (nf * nf)) - (1.097e7 / (ni * ni))
  lambfoton = 1 / a
  Efoton = (4.136e-15 * 3e8) / lambfoton
  return Efoton


def ffotonem(ni, nf):  # correto
  a = (1.097e7 / (nf * nf)) - (1.097e7 / (ni * ni))
  lambfoton = 1 / a
  ffoton = 3e8 / lambfoton
  return ffoton


def lambfotonem(ni, nf):  # correto
  a = (1.097e7 / (nf * nf)) - (1.097e7 / (ni * ni))
  lambfoton = 1 / a
  return lambfoton


# ABSORÇÃO DE FÓTON PELO H
# ENTRADA: ninicial e f ou lamb
# SAÍDA: nf


def nf_ni_f_ab(ni, f):  # correto
  Einicial = -13.6 / (ni * ni)
  Efoton = 4.136e-15 * f
  Efinal = Efoton + Einicial
  nf = sqrt(-13.6 / Efinal)
  return round(nf)


def nf_ni_lamb_ab(ni, lamb):  # correto
  Einicial = -13.6 / (ni * ni)
  f = c / lamb
  Efoton = 4.136e-15 * f
  Efinal = Efoton + Einicial
  nf = sqrt(-13.6 / Efinal)
  return round(nf)


# ABSORÇÂO DE FÓTON PELO H
# ENTRADA: nfinal e f ou lamb
# SAÍDA: ni


def ni_nf_f_ab(nf, f):  # correto
  Efinal = -13.6 / (nf * nf)
  Efoton = 4.136e-15 * f
  Einicial = Efinal - Efoton
  ni = sqrt(-13.6 / Einicial)
  return round(ni)


def ni_nf_lamb_ab(nf, lamb):  # correto
  Efinal = -13.6 / (nf * nf)
  f = c / lamb
  Efoton = 4.136e-15 * f
  Einicial = Efinal - Efoton
  ni = sqrt(-13.6 / Einicial)
  return round(ni)


# EMISSÃO DE FÓTON PELO H
# ENTRADA: ninicial e f ou lamb
# SAÍDA: nf


def nf_ni_f_em(ni, f):  # correto
  Einicial = -13.6 / (ni * ni)
  Efoton = 4.136e-15 * f
  Efinal = Einicial - Efoton
  nf = sqrt(-13.6 / Efinal)
  return round(nf)


def nf_ni_lamb_em(ni, lamb):  # correto
  Einicial = -13.6 / (ni * ni)
  f = c / lamb
  Efoton = 4.136e-15 * f
  Efinal = Einicial - Efoton
  nf = sqrt(-13.6 / Efinal)
  return round(nf)


# EMISSÃO DE FÓTON PELO H
# ENTRADA: nfinal e f ou lamb
# SAÍDA: ni


def ni_nf_f_em(nf, f):  # correto
  Efinal = -13.6 / (nf * nf)
  Efoton = 4.136e-15 * f
  Einicial = Efinal + Efoton
  ni = sqrt(-13.6 / Einicial)
  return round(ni)


def ni_nf_lamb_em(nf, lamb):  # correto
  Efinal = -13.6 / (nf * nf)
  f = c / lamb
  Efoton = 4.136e-15 * f
  Einicial = Efinal + Efoton
  ni = sqrt(-13.6 / Einicial)
  return round(ni)


# OUTRAS FUNÇÕES PARA A NL 2A


# Para descobrir se da para absorver um foton
# se o resultado for até 0.10 acima de um número inteiro a resposta é sim
def descobre_n_lamb(f):
  efoton = h2 * f
  return efoton


# Maior comprimento de onda e menor freqência de cada série
# Série de Lyman - nf = 1, ni = 2
# Série de Balmer - nf = 2, ni = 3
# Série de Paschen - nf = 3, ni = 4
# Série de Brackett - nf = 4, ni = 5
# Série de Pfund - nf = 5, ni = 6


def maior_comp(nf, ni):
  Ei = -13.6 / (nf * nf)
  Ef = -13.6 / (ni * ni)
  Efoton = Ef - Ei
  lamb = (h2 * c) / Efoton
  return lamb


def menor_freq(nf, ni):
  Ei = -13.6 / (nf * nf)
  Ef = -13.6 / (ni * ni)
  Efoton = Ef - Ei
  lamb = (h2 * c) / Efoton
  f = c / lamb
  return f


# Menor comprimento de onda e maior frequência de cada série
# Série de Lyman - nf = 1, ni = infinito
# Série de Balmer - nf = 2, ni = infinito
# Série de Paschen - nf = 3, ni = infinito
# Série de Brackett - nf = 4, ni = infinito
# Série de Pfund - nf = 5, ni = infinito


def menor_comp(nf):
  Ei = -13.6 / (nf * nf)
  Ef = 0
  Efoton = Ef - Ei
  lamb = (h2 * c) / Efoton
  return lamb


def maior_freq(nf):
  Ei = -13.6 / (nf * nf)
  Ef = 0
  Efoton = Ef - Ei
  lamb = (h2 * c) / Efoton
  f = c / lamb
  return f


# DESCOBRIR FREQUENCIA A PARTIR DAS PROPRIEDADES DO ÁTOMO


# Energia Potencial - tem que positivar o un na hora de chamar a função
# 9° estado excitado - ni = 10 (exemplo)
def freq_un(ni, un):
  nf = sqrt(27.2 / un)
  a = (1.097e7 / (nf * nf)) - (1.097e7 / (ni * ni))
  lambfoton = 1 / a
  f = c / lambfoton
  return f


# Energia Total - também tem que positivar
def freq_en(ni, en):
  nf = sqrt(13.6 / en)
  a = (1.097e7 / (nf * nf)) - (1.097e7 / (ni * ni))
  lambfoton = 1 / a
  f = c / lambfoton
  return f


# Energia Cinética - não precisa positivar
def freq_kn(ni, kn):
  nf = sqrt(13.6 / kn)
  a = (1.097e7 / (nf * nf)) - (1.097e7 / (ni * ni))
  lambfoton = 1 / a
  f = c / lambfoton
  return f


# Raio da órbita
def freq_rn(ni, rn):
  nf = sqrt(rn / (5.29e-11))
  a = (1.097e7 / (nf * nf)) - (1.097e7 / (ni * ni))
  lambfoton = 1 / a
  f = c / lambfoton
  return f


# Velocidade Orbital
def freq_vn(ni, rn):
  nf = vn / 2.19e6
  a = (1.097e7 / (nf * nf)) - (1.097e7 / (ni * ni))
  lambfoton = 1 / a
  f = c / lambfoton
  return f


def espectro(n, i):  # correto
  lamb = 1 / (1.097e7 * ((1 / (i * i)) - (1 / (n * n))))
  return lamb


#a = espectro()

# WHILE TRUE

while True:
  #try:
  op = int(
    input('''
    1 - Propiedades do átomo de Hidrogênio
    2 - Emissão de fóton pelo H
    3 - Absorção de fóton pelo H
    4 - transformaçoes
    5 - Maior e menor comprimento de onda e frequência de uma série
    6 - Frequência apartir de ni e Rn, Vn, Kn, Un ou En
    7 - Espectro de H
    8 - Sair
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
      '''.format(rn(n), vn(n), lambn(n), En(n), Kn(n), Un(n)))
    input("Pressione uma tecla para continuar...")
  elif op == 2:
    x = int(
      input('''
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
        nf = {} 
        '''.format(nf_ni_f_em(ni, f)))
      input("Pressione uma tecla para continuar...")
    elif x == 3:
      ni = int(input('Digite o valor de ni: '))
      lamb = float(input('Digite o valor de lamb: '))
      print('''
        Resultados:
        nf = {}
        '''.format(nf_ni_lamb_em(ni, lamb)))
      input("Pressione uma tecla para continuar...")
    elif x == 4:
      nf = int(input('Digite o valor de nf: '))
      f = float(input('Digite o valor de f: '))
      print('''
        Resultados:
        ni = {}
        '''.format(ni_nf_f_em(nf, f)))
      input("Pressione uma tecla para continuar...")
    elif x == 5:
      nf = int(input('Digite o valor de nf: '))
      lamb = float(input('Digite o valor de lamb: '))
      print('''
        Resultados:
        ni = {}
        '''.format(ni_nf_lamb_em(nf, lamb)))
      input("Pressione uma tecla para continuar...")
  elif op == 3:
    x = int(
      input('''
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
        nf = {}
        '''.format(nf_ni_f_ab(ni, f)))
      input("Pressione uma tecla para continuar...")
    elif x == 3:
      ni = int(input('Digite o valor de ni: '))
      lamb = float(input('Digite o valor de lamb: '))
      print('''
        Resultados:
        nf = {}
        '''.format(nf_ni_lamb_ab(ni, lamb)))
      input("Pressione uma tecla para continuar...")
    elif x == 4:
      nf = int(input('Digite o valor de nf: '))
      f = float(input('Digite o valor de f: '))
      print('''
        Resultados:
        ni = {}
        '''.format(ni_nf_f_ab(nf, f)))
    elif x == 5:
      nf = int(input('Digite o valor de nf: '))
      lamb = float(input('Digite o valor de lamb: '))
      print('''
        Resultados:
        ni = {}
        '''.format(ni_nf_lamb_ab(nf, lamb)))
      input("Pressione uma tecla para continuar...")
  elif op == 4:
    print('''
      Você tem:
      1 - lambda para nivel
      2 - frequencia para nivel
      ''')
    x = int(input('Digite a opção: '))
    if x == 1:
      lmb = float(input('Digite o valor de lambda: '))
      f = c / lmb
      print('''
        nivel = {:.3}
        '''.format(descobre_n_lamb(f)))
    elif x == 2:
      pass
    else:
      print('Opção inválida!')
  elif op == 5:
    print('''
      1 - Maior comprimento de uma onda
      2 - Menor comrpimento de uma onda
      3 - Maior frequência de uma série
      4 - Menor freqência de uma série
      ''')
    x = int(input('Digite a opção: '))
    if x == 1:
      nf = int(input("Digite o valor de nf: "))
      ni = int(input("Digite o valor de ni: "))
      print('''
        maior comprimento = {:.3e}
        '''.format(maior_comp(nf, ni)))
    if x == 2:
      nf = int(input("Digite o valor de nf: "))
      print('''
        menor comprimento = {:.3e}
        '''.format(menor_comp(nf)))
    if x == 3:
      nf = int(input("Digite o valor de nf: "))
      print('''
        maior frequência = {:.3e}
        '''.format(maior_freq(nf)))
    if x == 4:
      nf = int(input("Digite o valor de nf: "))
      ni = int(input("Digite o valor de ni: "))
      print('''
        menor frequência = {:.3e}
        '''.format(menor_freq(nf, ni)))
  elif op == 6:
    print('''
      1 - A partir de Rn
      2 - A partir de Vn
      3 - A partir de Kn
      4 - A partir de Un
      5 - A partir de En
      ''')
    x = int(input("Digite a opção: "))
    if x == 1:
      ni = int(input("Digite o valor de ni: "))
      rn = float(input("Digite o valor de Rn: "))
      print('''
        Frequência = {:.3e}
        '''.format(freq_rn(ni, rn)))
    elif x == 2:
      ni = int(input("Digite o valor de ni: "))
      vn = float(input("Digite o valor de Vn: "))
      print('''
        Frequência = {:.3e}
        '''.format(freq_vn(ni, vn)))
    elif x == 3:
      ni = int(input("Digite o valor de ni: "))
      kn = float(input("Digite o valor de Kn: "))
      print('''
        Frequência = {:.3e}
        '''.format(freq_kn(ni, kn)))
    elif x == 4:
      ni = int(input("Digite o valor de ni: "))
      un = float(input("Digite o valor de Un: "))
      print('''
        Frequência = {:.3e}
        '''.format(freq_un(ni, un)))
    elif x == 5:
      ni = int(input("Digite o valor de ni: "))
      en = float(input("Digite o valor de En: "))
      print('''
        Freqência = {:.3e}
        '''.format(freq_en(ni, en)))
  elif op == 7:
    resp = espectro(
      int(input('Digite o valor do nível: ')),
      int(
        input('''
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
  elif op == 8:
    break
  else:
    print('Opção inválida!')
# except:
#   print("Houve um erro! Tente novamente.")
#   input("Pressione uma tecla para continuar...")
