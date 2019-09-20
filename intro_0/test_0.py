#!/usr/bin/env python3

with open('texto.txt', 'r') as p_arquivo:
    t = p_arquivo.read()

print(repr(t))

t = t[:-1] + ' MUITO NOOB\n'

print(t)

with open('texto_mod.txt', 'a') as p_arquivo:
    p_arquivo.write(t)

print(t)
