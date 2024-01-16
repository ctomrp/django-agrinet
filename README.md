# AGRINET

## cómo descargar el proyecto

### 1 - clona el repositorio
Posicionate en el directorio donde quieres guardar el proyecto y ejecuta:
```bash
git clone https://github.com/ctomrp/django-agrinet.git
```
Una vez hecho eso muevete a la carpeta del repositorio y ejecuta:
```bash
git checkout develNombre
```
para moverte a tu rama (Nombre tuyo).
### 2 - configura tu entorno virtual y poetry
Muevete a la carpeta back y estando en la raíz del proyecto django ejecuta:
```bash
py -m venv venv
```
Luego ejecuta 
```bash
venv\Scripts\Activate.ps1
```
para activar el entorno virtual.
Una vez ahí instala poetry con:
```bash
pip install poetry
```
Y ejecuta 
```bash
poetry install
```

### BUENAS PRÁCTICAS PYTHON

[Buenas prácticas python pep8](https://ellibrodepython.com/python-pep8)