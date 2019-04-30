from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup 
import json

def obtenerProducto(departamento, tipoProducto):

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

    soup=BeautifulSoup(driver.page_source, 'html.parser') 

    # Se cierra el driver de Selenium
    driver.close()

    listaProducto = soup.find('select',{"name":"ddlProducto"})

    productos = listaProducto.find_all('option')
    del productos[0] 

    resultadoProductos = []
    
    for fila in productos:
        item = {
            "Valor":fila['value'],
            "Texto":fila.text,
        }
        resultadoProductos.append(item) 

    return (json.dumps(resultadoProductos, separators=(',', ':')))
 