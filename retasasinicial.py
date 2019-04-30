import requests
import urllib.request 
from bs4 import BeautifulSoup 
import json

def informacionInicial():

    # Acceso a la página de retasas
    url = 'http://www.sbs.gob.pe/app/retasas/paginas/retasasinicio.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser") 

    # Se obtiene las lista de departamentos y tipos de productos
    listaDepartamento = soup.find('select',{"name":"ddlDepartamento"})
    listaTipoProducto = soup.find('select',{"name":"ddlTipoProducto"})

    # Se obtiene las opciones y se retira el primer elemento vacío de las listas
    departamentos = listaDepartamento.find_all('option')
    del departamentos[0]

    tipoProductos = listaTipoProducto.find_all('option')
    del tipoProductos[0]

    resultadoDepartamentos = []

    # Se convierte la lista de item a una lista de diccionarios
    for fila in departamentos:
        item = {
            "Valor":fila['value'],
            "Texto":fila.text,
        }
        resultadoDepartamentos.append(item)

    resultadoTipoProductos = []

    for fila in tipoProductos:
        item = {
            "Valor":fila['value'],
            "Texto":fila.text,
        }
        resultadoTipoProductos.append(item)

    # Se retorna el JSON del resultado
    return (json.dumps({"Departamentos":resultadoDepartamentos,"TipoProductos":resultadoTipoProductos}, separators=(',', ':')))
 