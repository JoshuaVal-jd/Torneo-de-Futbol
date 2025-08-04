# Torneos de Bola

Proyecto de consola en Python que permite gestionar un torneo de fútbol: creación de torneos, registro de equipos, generación de calendario, registro de resultados, tablas de posiciones y goleadores, y envío de correos con calendarios y resultados.

## Descripción

Este proyecto, escrito en Python 3.12.6, emula las funcionalidades principales de una aplicación de gestión de torneos de fútbol:

- Configuración completa del torneo (nombre, número de equipos, equipos que clasifican, puntos por victoria y empate).
- Registro y administración de **equipos** (agregar, consultar, modificar, eliminar).
- Creación y consulta de **calendario de juegos**.
- Registro y edición de **resultados de partidos**, incluyendo goles, goleadores y minutos.
- Visualización y envío por correo electrónico de la **tabla de posiciones**.
- Impresión de la **tabla de goleadores**.
- Menú interactivo en consola con secciones de Ayuda y Acerca de.

## Requisitos

- Python 3.12.6
- Módulos estándar: `os`, `pickle`, `smtplib`, `ssl`, `email.message`

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/JoshuaVal-jd/torneos-de-Futbol.git
   cd torneos-de-bola
   ```
2. (Opcional) Crear y activar un entorno virtual:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. No se requieren módulos externos adicionales.

## Uso

Ejecutar el script en la consola o en IDLE:
```bash
python torneos_de_bola.py
```
Para ejemplos y capturas de cada flujo, consulta el [Manual de Usuario](manual_de_usuario_torneos_de_bola.pdf).

## Configuración inicial

**Importante:** Antes de registrar equipos o ejecutar cualquier otra opción, debes completar la **Configuración del torneo**. Si omites este paso, el programa finalizará con error.

## Menú y características principales

1. **Configuración del torneo**  
   Definir nombre, cantidad de equipos participantes, equipos que clasifican, puntos por victoria y empate; confirmar o cancelar antes de continuar.

2. **Registrar equipos**  
   Agregar, consultar, modificar o eliminar equipos antes de crear el calendario.

3. **Crear calendario de juegos**  
   Genera automáticamente las fechas y emparejamientos; bloquea la edición de la lista de equipos.

4. **Consultar calendario de juegos**  
   Imprime en pantalla el calendario completo por cada fecha.

5. **Registrar los resultados**  
   Añadir, consultar, modificar o eliminar resultados de partidos, detallando goles, goleadores y minutos.

6. **Tabla de posiciones**  
   Solicita un correo, envía por email la tabla con puntos y muestra el resultado en pantalla.

7. **Tabla de goleadores**  
   Imprime en pantalla la lista de goleadores con el total de goles.

8. **Ayuda**  
   Muestra el manual de usuario completo.

9. **Acerca de**  
   Despliega nombre del programa, versión, fecha de creación y autor.

## Autor

Joshua Valvarde Arguedas  
Versión 1.0 (13/05/2024)

## Contribuciones

¡Bienvenido! Para contribuir:

1. Abre un issue describiendo tu sugerencia o reporte.  
2. Envía un pull request con cambios claros y descritos.  

Todas las mejoras y correcciones son bienvenidas.
