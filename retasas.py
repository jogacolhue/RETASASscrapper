from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import json

def obtenerRetasas(departamento, tipoProducto, producto, condicion):

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
    select = Select(driver.find_element_by_name('ddlCondicion'))
    select.select_by_value(condicion) 

    # Se acciona el botón "Consultar"
    driver.find_element_by_id("btnConsultar").click()
    time.sleep(1) 

    # Se apunta al iframe generado con la tabla de retasas
    driver.switch_to.frame("ifrmContendedor")

    # Se obtiene el contenido del iframe
    soup=BeautifulSoup(driver.page_source, 'html.parser')

    # Se cierra el driver de Selenium
    driver.close()

    # Se obtiene la tabla con las retasas
    one_a_tag = soup.find("table", {"id": "myTable"})

    table_body = one_a_tag.find_all('tr')

    # Se pasa la información a una lista
    table_headers = [[cell.text for cell in row("th")]
                            for row in table_body]

    table_data = [[cell.text for cell in row("td")]
                            for row in table_body]

    # Se retira el encabezado vacío
    del table_data[0]

    resultado = []

    # Se convierte la lista de item a una lista de diccionarios
    for fila in table_data:
        item = {
            table_headers[0][0]: fila[0],
            table_headers[0][1]: fila[1],
            table_headers[0][2]: fila[2]
        }
        resultado.append(item)

    # Se retorna el json con los datos de retasas
    return json.dumps(resultado, separators=(',', ':'))

