# Proyecto Gestión de Hoteles 

**Asignatura**: Base datos no estructuradas (TI3V32_140-3-Flex_V Puente Alto)

**Profesor**: Michael Arjel

**Integrantes**: 
- Araceli Alvarado
- Jorge Moreno
- Benjamín Tobar

--

## Descripción

Este es un proyecto de sistema de gestión de hoteles desarrollado en Python, utilizando MongoDB como base de datos NoSQL. 

### Permite:

- Conectarse a una BD en MongoDB
- Crear hoteles con sus datos básicos (nombre, dirección, comuna, ciudad)
- Agregar habitaciones con asus respectivos atributos (numero de habitacion, tipo, precio, disponibilidad)
- Editar nombre y dirección del hotel
- Editar o eliminar habitaciones existentes
- Buscar hoteles:
  - Listar todos los hoteles
  - Buscar por mombre
  - Buscar por ID
  - Buscar por ciudad
  - Buscar por comuna
  - Hoteles con habitaciones disponibles
  - Nombre o ciudad *solo si tienen habitaciones disponibles*
- Eliminar hoteles

--

## Para ejecutarlo:
- Instalar librería pymongo (pip install pymongo)
- Configurar conexión a MongoDB (Database -> mongo.py, agregar usuario y contraseña)
- Ejecutar el programa desde el archivo principal (main.py)
## Clonar este repositorio:
   ```bash
   git clone https://github.com/JamonaRamona/Evaluacion3_noSQL.git
