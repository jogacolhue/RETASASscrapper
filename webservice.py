from flask import Flask
from flask import request
import retasasinicial
import retasasproducto
import retasascondicion
import retasas

app = Flask(__name__)

@app.route('/inicial', methods=['GET'])
def informacionInicial(): 
    return retasasinicial.informacionInicial()

@app.route('/producto/<departamento>/<tipoProducto>', methods=['GET'])
def obtenerProductos(departamento, tipoProducto): 
    return retasasproducto.obtenerProducto(departamento, tipoProducto)

@app.route('/condicion/<departamento>/<tipoProducto>/<producto>', methods=['GET'])
def obtenerCondiciones(departamento, tipoProducto, producto): 
    return retasascondicion.obtenerCondicion(departamento, tipoProducto, producto)

@app.route('/retasas/<departamento>/<tipoProducto>/<producto>/<condicion>', methods=['GET'])
def ratasas(departamento, tipoProducto, producto, condicion): 
    return retasas.obtenerRetasas(departamento, tipoProducto, producto, condicion)

# Se deja el modo de depuración activo
app.run(debug=True, use_reloader=False)#app.run(host='0.0.0.0', port=5000)