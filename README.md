# Proyecto de Criptografia
## Cifrador y Descifrador con Clave Derivada (Flask)

Este proyecto es una aplicación web desarrollada con Flask que permite **cifrar y descifrar mensajes** utilizando una clave personalizada y un sistema de cifrado híbrido basado en **XOR + César**, reforzado con **claves derivadas dinámicamente** usando **SHA-256**.

---

## 🚀 Características

- ✔️ Cifrado por clave + timestamp
- 🔑 Derivación de clave segura con SHA-256
- 📤 Exportación del mensaje cifrado en formato Base64
- 🧬 Clave única para cada cifrado (aunque se use el mismo mensaje)
- 📄 Interfaz web simple e intuitiva
- 🔓 Soporte para descifrado usando el mismo sistema

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Flask
- HTML + CSS (plantillas Jinja2)
- Base64
- SHA-256 (`hashlib`)

---

## ⚙️ Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/EduardoG742/Criptografia.git
cd Criptografia
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:

```bash
python app.py
```

4. Abre tu navegador y ve a:
```
http://localhost:5000
```

---

## 🧪 Cómo funciona el cifrado

1. El usuario ingresa un mensaje y una clave base.

2. Se obtiene la hora actual (timestamp).

3. Se deriva una clave única:
clave_derivada = SHA256(clave base + timestamp)

4. El mensaje se cifra con esa clave usando una combinación de XOR + César.

5. Se guarda el resultado:
Base64(timestamp + mensaje_cifrado)

6. La clave derivada (hash) se muestra como información técnica.

---

## 🔓 Descifrado

1. Se extrae el timestamp del texto cifrado.

2. Se deriva la misma clave usando clave base + timestamp.

3. Se aplica el descifrado inverso para recuperar el mensaje original.

---

## ⚠️ Consejo

Abrir el descifrado en una pestaña nueva para poder comparar que la clave derivada es la misma.
