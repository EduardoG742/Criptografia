from flask import Flask, render_template, request
import base64
import hashlib
import time

app = Flask(__name__)

# Genera un hash SHA-256 en bytes
def sha256(s):
    return hashlib.sha256(s.encode()).digest()

# Devuelve el desplazamiento de cada byte
def char_a_offset(c):
    return c % 256

# Cifra o descifra los datos con la clave en bytes
def procesar_bytes(data_bytes, clave_bytes, modo='cifrar'):
    resultado = bytearray()
    offsets = [char_a_offset(b) for b in clave_bytes]

    for i, byte in enumerate(data_bytes):
        d = offsets[i % len(offsets)]
        if modo == 'cifrar':
            xor = byte ^ (d & 0b1111)
            final = (xor + d) % 256
        else:
            sub = (byte - d) % 256
            final = sub ^ (d & 0b1111)
        resultado.append(final)

    return bytes(resultado)

# Ruta de cifrado
@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = ""
    clave = ""
    cifrado = ""
    hash_clave = ""

    if request.method == 'POST':
        mensaje = request.form['mensaje']
        clave = request.form['clave']

        if mensaje and clave:
            timestamp = str(int(time.time()))
            clave_derivada = sha256(clave + timestamp)
            hash_clave = clave_derivada.hex()  # Mostrar hash en hexadecimal

            mensaje_bytes = mensaje.encode("utf-8")
            cifrado_bytes = procesar_bytes(mensaje_bytes, clave_derivada, 'cifrar')
            final_bytes = f"{timestamp}|".encode() + cifrado_bytes
            cifrado = base64.b64encode(final_bytes).decode("utf-8")

    return render_template('index.html', mensaje=mensaje, clave=clave, cifrado=cifrado, hash_clave=hash_clave)

# Ruta de descifrado
@app.route('/descifrar', methods=['GET', 'POST'])
def descifrar():
    cifrado = ""
    clave = ""
    mensaje_descifrado = ""
    hash_clave = ""

    if request.method == 'POST':
        cifrado = request.form['cifrado']
        clave = request.form['clave']

        try:
            datos = base64.b64decode(cifrado)
            partes = datos.split(b"|", 1)
            timestamp = partes[0].decode()
            datos_cifrados = partes[1]

            clave_derivada = sha256(clave + timestamp)
            hash_clave = clave_derivada.hex()  # Mostrar también el hash derivado

            descifrado_bytes = procesar_bytes(datos_cifrados, clave_derivada, 'descifrar')
            mensaje_descifrado = descifrado_bytes.decode("utf-8")
        except:
            mensaje_descifrado = "Clave incorrecta, timestamp dañado o texto alterado."

    return render_template('descifrar.html', cifrado=cifrado, clave=clave, mensaje=mensaje_descifrado, hash_clave=hash_clave)

# Ejecutar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
