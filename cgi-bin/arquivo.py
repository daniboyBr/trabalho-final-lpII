#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import cgi
import cgitb
import csv
cgitb.enable()

"""
    Metodo recebe um registro e abre o arquivo para escrita escrevendo o registro nele
"""
def escrever(registro):
    arquivo = open("cgi-bin/inscricoes.csv", "a", newline="") #abre o arquivo para escrita para atualizacao com a proxima linha em branco
    escrever = csv.writer(arquivo, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) #prepara o arquivo para ser escrito
    escrever.writerow(registro) #escreve registro na ultima linha do arquivo
    arquivo.close() #fecha o arquivo

"""
    Metodo verifica se o registro existe, abrindo o arquivo para leitura e comparando com o registro enviado
"""
def registro_existe(registro):
    arquivo = open("cgi-bin/inscricoes.csv", "r") #abre o arquvivo em modo de leitura
    ler = csv.reader(arquivo) #ler o arquivo e salva na variavel
    registro_existe = False
    for linha in ler: #percorre cada linha do arquvivo
        if (linha[4] == registro[4]): #verifica se o registro recebido é igual ao registro existente no arquivo
            registro_existe = True
            break
    arquivo.close()#fecha o arquivo
    return registro_existe

"""
    Metodo de teste para ler o arquivo.
"""
def ler_arquivo():
    arquivo = open("cgi-bin/inscricoes.csv", "r")
    ler = csv.reader(arquivo)
    for linha in ler:
        print(linha)
    arquivo.close()

"""
    Verifica se os campos recebidos do formulario estao em branco.
"""
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

"""
    retorna os cursos
"""
def retorna_curso(num_curso):
    curso = {
        1 : "Curso I",
        2 : "Curso II",
        3 : "Curso III"
    }
    return curso[num_curso]

"""
    retorna os turno
"""
def retorna_turno(num_turno):
    turno = {
        1 : "Matutino",
        2 : "Vespertino",
        3 : "Noturno"
    }
    return turno[num_turno]

"""
    Verifica se os campos numericos relmente são numeros
"""
def campo_numerico(registro):
    campos = ['idade', 'telefone','curso','turno','matricula']
    isNumero = True
    for campo in campos:
        input = registro[campo].value
        if(not input.isdigit()):
            isNumero = False
            break
    return isNumero

"""
    Verifica se os campos de texto são apenas texto
"""
def campo_apenas_texto(registro):
    campos = ['nome', 'campus']
    isLetras = True
    for campo in campos:
        input = registro[campo].value
        input = input.replace(" ","")
        if(not input.isalpha()):
            isLetras = False
            break
    return isLetras

input_data = cgi.FieldStorage()

print('Content-Type:text/html; charset=utf-8')
print()
print('<h1>Resultado</h1>')
try:
    if (len(input_data) == 8):
        if(campos_em_branco(input_data)):
            print("Campos obrigatorios nao preenchidos.")     
        else:
            if(campo_apenas_texto(input_data) and campo_numerico(input_data)):

                usuario = [
                    input_data["nome"].value,
                    int(input_data["idade"].value),
                    input_data["email"].value,
                    input_data["telefone"].value,
                    input_data["matricula"].value,
                    retorna_curso(int(input_data["curso"].value)),
                    retorna_turno(int(input_data["turno"].value)),
                    input_data["campus"].value
                ]

                if(registro_existe(usuario)):
                    print("Usuário já inscrito.")
                else:
                    escrever(usuario)
                    print("Registro salvo com sucesso.")
            else:
                print("Campos obrigatorios não preenchidos corretamente.")
    else:
        print("Alguns campos não foram enviados ou nao preenchidos")
except:
    print("Não foi possivel buscar a infomação solicitada")
