from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup 
import json

def obtenerCondicion(departamento, tipoProducto, producto):

    # Acceso a la página de retasas
    driver = webdriver.Firefox()
    driver.get("http://www.sbs.gob.pe/app/retasas/paginas/retasasinicio.aspx")

    # Llenado del formulario, dando tiempo a que se refresquen los items
    select = Select(driver.find_element_by_name('ddlDepartamento'))
    select.select_by_value(departamento)
    time.sleep(1) 
    select = Select(driver.find_element_by_name('ddlTipoProducto'))
    select.select_by_value(tipoProducto)
    time.sleep(1) 
    select = Select(driver.find_element_by_name('ddlProducto'))
    select.select_by_value(producto)
    time.sleep(1) 
    
    soup=BeautifulSoup(driver.page_source, 'html.parser') 

    # Se cierra el driver de Selenium
    driver.close()

    # Se obtiene las lista de condiciones
    listaCondicion = soup.find('select',{"name":"ddlCondicion"})

    # Se obtiene las condiciones y se retira el elemento vacío de la lista
    condiciones = listaCondicion.find_all('option')
    del condiciones[0] 

    resultadoCondiciones = []
    
    # Se convierte la lista de item a una lista de diccionarios
    for fila in condiciones:
        item = {
            "Valor":fila['value'],
            "Texto":fila.text,
        }
        resultadoCondiciones.append(item) 

    # Se retorna el JSON del resultado
    return (json.dumps(resultadoCondiciones, separators=(',', ':')))
 