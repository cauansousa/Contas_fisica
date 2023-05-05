from math import *


# entra dois angulos e uma intensidade
# sai i1 e i2
def ang_i0(ang1, ang2, i0):
    i1 = i0 / 2
    teta = radians(ang2 - ang1)
    i2 = i1 * pow(cos(teta), 2)
    return i1, i2


# entra dois angulos e uma intensidade
# sai i0 e i2
def ang_i1(ang1, ang2, i1):
    i0 = i1 * 2
    teta = radians(ang2 - ang1)
    i2 = i1 * pow(cos(teta), 2)
    return i0, i2


# entra dois angulos e uma intensidade
# sai i0 e i1
def ang_i2(ang1, ang2, i2):
    teta = radians(ang2 - ang1)
    i1 = i2 / pow(cos(teta), 2)
    i0 = i1 * 2
    return i0, i1


# entra dois angulos e uma intensidade
# sai i0, i1 e i2
def ang3_i0(ang1, ang2, ang3, i0):
    i1 = i0 / 2
    teta1 = radians(ang2 - ang1)
    teta2 = radians(ang3 - ang2)
    i2 = i1 * pow(cos(teta1), 2)
    i3 = i2 * pow(cos(teta2), 2)
    return i1, i2, i3


def ang3_i1(ang1, ang2, ang3, i1):
    i0 = i1 * 2
    teta1 = radians(ang2 - ang1)
    teta2 = radians(ang3 - ang2)
    i2 = i1 * pow(cos(teta1), 2)
    i3 = i2 * pow(cos(teta2), 2)
    return i0, i2, i3


def ang3_i2(ang1, ang2, ang3, i2):
    teta1 = radians(ang2 - ang1)
    teta2 = radians(ang3 - ang2)
    i1 = i2 / pow(cos(teta1), 2)
    i0 = i1 * 2
    i3 = i2 * pow(cos(teta2), 2)
    return i0, i1, i3


def ang3_i3(ang1, ang2, ang3, i3):
    teta1 = radians(ang2 - ang1)
    teta2 = radians(ang3 - ang2)
    i2 = i3 / pow(cos(teta2), 2)
    i1 = i2 / pow(cos(teta1), 2)
    i0 = i1 * 2
    return i0, i1, i2


while True:
    print("""
1 - 2 angulos e i0
2 - 2 angulos e i1
3 - 2 angulos e i2
4 - 3 angulos e i0
5 - 3 angulos e i1
6 - 3 angulos e i2
7 - 3 angulos e i3
0 - Sair
    """)
    op = int(input("Digite a opção: "))
    if op == 1:
        ang1 = float(input("Digite o angulo 1: "))
        ang2 = float(input("Digite o angulo 2: "))
        i0 = float(input("Digite a intensidade: "))
        i1, i2 = ang_i0(ang1, ang2, i0)
        print("i1 = {}\ni2 = {}".format(i1, i2))
    elif op == 2:
        ang1 = float(input("Digite o angulo 1: "))
        ang2 = float(input("Digite o angulo 2: "))
        i1 = float(input("Digite a intensidade: "))
        i0, i2 = ang_i1(ang1, ang2, i1)
        print("i0 = {}\ni2 = {}".format(i0, i2))
    elif op == 3:
        ang1 = float(input("Digite o angulo 1: "))
        ang2 = float(input("Digite o angulo 2: "))
        i2 = float(input("Digite a intensidade: "))
        i0, i1 = ang_i2(ang1, ang2, i2)
        print("i0 = {}\ni1 = {}".format(i0, i1))
    elif op == 4:
        ang1 = float(input("Digite o angulo 1: "))
        ang2 = float(input("Digite o angulo 2: "))
        ang3 = float(input("Digite o angulo 3: "))
        i0 = float(input("Digite a intensidade: "))
        i1, i2, i3 = ang3_i0(ang1, ang2, ang3, i0)
        print("i1 = {}\ni2 = {}\ni3 = {}".format(i1, i2, i3))
    elif op == 5:
        ang1 = float(input("Digite o angulo 1: "))
        ang2 = float(input("Digite o angulo 2: "))
        ang3 = float(input("Digite o angulo 3: "))
        i1 = float(input("Digite a intensidade: "))
        i0, i2, i3 = ang3_i1(ang1, ang2, ang3, i1)
        print("i0 = {}\ni2 = {}\ni3 = {}".format(i0, i2, i3))
    elif op == 6:
        ang1 = float(input("Digite o angulo 1: "))
        ang2 = float(input("Digite o angulo 2: "))
        ang3 = float(input("Digite o angulo 3: "))
        i2 = float(input("Digite a intensidade: "))
        i0, i1, i3 = ang3_i2(ang1, ang2, ang3, i2)
        print("i0 = {}\ni1 = {}\ni3 = {}".format(i0, i1, i3))
    elif op == 7:
        ang1 = float(input("Digite o angulo 1: "))
        ang2 = float(input("Digite o angulo 2: "))
        ang3 = float(input("Digite o angulo 3: "))
        i3 = float(input("Digite a intensidade: "))
        i0, i1, i2 = ang3_i3(ang1, ang2, ang3, i3)
        print("i0 = {}\ni1 = {}\ni2 = {}".format(i0, i1, i2))
    elif op == 0:
        break

