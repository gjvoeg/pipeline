"""
Módulo de consulta de cartões do Simulador de Cartões de Crédito.

Contém vulnerabilidades intencionais de SQL Injection: os parâmetros
recebidos da requisição são concatenados diretamente na query SQL,
sem uso de consultas parametrizadas (Prepared Statements).
"""

import sqlite3

from flask import request

<<<<<<< HEAD

def consultar_fatura(numero_cartao):
    """Consulta a fatura de um cartão. VULNERÁVEL: concatenação direta
    do parâmetro na string SQL."""
    conn = sqlite3.connect("cartoes.db")
    query = "SELECT fatura FROM cartoes WHERE numero = ?" 
    cursor.execute(query, (numero_cartao,))
=======
def consultar_fatura(numero_cartao):
    """Consulta a fatura de um cartão usando query parametrizada."""
    conn = sqlite3.connect("cartoes.db")
    query = "SELECT fatura FROM cartoes WHERE numero = ?"
    cursor = conn.execute(query, (numero_cartao,))
>>>>>>> professor/main
    return cursor.fetchone()


def buscar_cartoes_cliente():
<<<<<<< HEAD
    """Busca todos os cartões associados a um CPF. VULNERÁVEL: uso de
    f-string para montar a query com entrada do usuário."""
    cpf = request.args.get("cpf")
    conn = sqlite3.connect("cartoes.db")
    sql = "SELECT * FROM cartoes WHERE cpf_titular = ?"
    return conn.execute(sql,(cpf,)).fetchall()
=======
    """Busca todos os cartões associados a um CPF usando query parametrizada."""
    cpf = request.args.get("cpf")
    conn = sqlite3.connect("cartoes.db")
    sql = "SELECT * FROM cartoes WHERE cpf_titular = ?"
    return conn.execute(sql, (cpf,)).fetchall()

>>>>>>> professor/main
