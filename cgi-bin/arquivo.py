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

def campos_em_branco(registro):
    campos = ['nome','idade','email','telefone','matricula','curso','turno','campus']
    branco = False
    for campo in campos:
        input = registro[campo].value
        input = input.strip()
        if (len(input) == 0):
            branco = True
            break
    return branco

input_data = cgi.FieldStorage()

print('Content-Type:text/html; charset=utf-8')
print()
try:
    if (len(input_data) == 8):
        if(campos_em_branco(input_data)):
            print("Campos obrigatorios nao preenchidos.")     
        else:
            print("Não possui campos em branco")
    else:
        print("Alguns campos não foram enviados ou nao preenchidos")





    '''
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
        
        print('<h1>Resultado</h1>')
        print(usuario)
        escrever(usuario)
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
