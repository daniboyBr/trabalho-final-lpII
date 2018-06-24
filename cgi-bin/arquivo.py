#!d:/Daniel/python/python.exe
# -*- coding: utf-8 -*-

import cgi
import cgitb
import csv
cgitb.enable()

def escrever(registro):
    arquivo = open("cgi-bin/inscricoes.csv", "a", newline="")
    escrever = csv.writer(arquivo, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    escrever.writerow(registro)
    arquivo.close()

def registro_existe(registro):
    arquivo = open("cgi-bin/inscricoes.csv", "r")
    ler = csv.reader(arquivo)
    registro_existe = False
    for linha in ler:
        if (linha[0] == registro):
            registro_existe = True
            break
    arquivo.close()
    return registro_existe

input_data = cgi.FieldStorage()

print('Content-Type:text/html; charset=utf-8')
print()
print('<h1>Resultado</h1>')
try:
    usuario = [
        input_data["nome"].value,
        int(input_data["idade"].value),
        input_data["email"].value,
        input_data["telefone"].value,
        input_data["matricula"].value,
        input_data["curso"].value,
        input_data["turno"].value,
        input_data["campus"].value
    ]
    print(usuario)
    escrever(usuario)

    '''
        msg = ''
        if (registro_existe(nome)):
            msg = {'msg': 'O registro que está tentando inserir já existe'}
        else:
            escrever(nome)
            msg = {'msg':'Registro salvo com sucesso'}
        print(msg['msg']) 
    '''
except:
    print("Não foi possivel buscar a infomação solicitada")
