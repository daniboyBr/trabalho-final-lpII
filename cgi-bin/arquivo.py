#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import cgi
import cgitb
import csv
cgitb.enable()

def escrever(linha):
    arquivo = open("cgi-bin/inscricoes.csv", "a")
    escrever = csv.writer(arquivo, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    escrever.writerow([nome])
    arquivo.close()

def registro_existe(registro):
    arquivo = open("cgi-bin/inscricoes.csv", "r")
    ler = csv.reader(arquivo)
    registro_existe = False
    for linha in ler:
        if (linha[0] == nome):
            registro_existe = True
            break
    arquivo.close()
    return registro_existe

input_data = cgi.FieldStorage()

print('Content-Type:text/html; charset=UTF-8')
print()
print('<h1>Resultado</h1>')
try:
    nome = input_data["nome"].value
    if (registro_existe(nome)):
        print('<p>O registro que está tentando inserir já existe</p>')
    else:
        escrever(nome)
        print('<p>Registro salvo com sucesso</p>')

except:
    print("Não foi possivel buscar a infomação solicitada")