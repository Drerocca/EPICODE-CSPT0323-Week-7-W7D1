import random

semplice = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
complessa = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-_./:;<=>?@{|}~'

tipo = input("Che tipo di password vuoi generare?\n1. SEMPLICE\n2. COMPLESSA\n")

if tipo == "1":
    lunghezza = 8
    password = ''.join(random.sample(semplice, lunghezza))
    print("La tua password casuale è:\n", password)
elif tipo == "2":
    lunghezza = 20
    password = ''.join(random.sample(semplice, lunghezza))
    print("La tua password casuale è:\n", password)
else:
    print("Scelta non valida!")
