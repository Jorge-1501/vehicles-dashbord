# Dashboard Tesis

Este repositorio contiene el código fuente para el análisis de datos provenientes de jets generados por quarks y jets generador por gluones en el contexto de física de altas energías, particularmente en las colisiones protón-protón.

## **Notas importantes**
Esta versión tiene como propósito sevir como proyecto entregable para el bootcamp de Data Science de TripleTen. Además, aprovechando la naturaleza de la tarea y el contexto de estar desarrollando mi tesis de licenciatura, el producto incluye un análisis de datos que forma parte de mi investigación de tesis.

En versiones futuras se planea agregar a deatalle el proceso completo de la tesis, marco teórico, metodología y resultados, además de mejorar la presentación del dashboard y agregar nuevas funcionalidades.

Como parte de los requisitos del proyecto de solicitaba un `requirements.txt`. Al usar un `uv` como administrador de dependencias, el archivo `requirements.txt` no se usó de forma predetermiada, ya que `uv` gestiona las dependencias a través de su propio sistema. Sin embargo, se generó el archivo para copatibilidad con otras herramientas también.

## Contenido del repositorio
**Directorios**
- `data/`: Contiene los archivos de datos utilizados para el análisis.
- `notebooks/`: Contiene los notebooks de Jupyter utilizados para el análisis exploratorio y la generación de visualizaciones.
- `src/`: Contiene el código fuente para el procesamiento de datos y la generación del dashboard.
- `img/`: Contiene imágenes y gráficos generados durante el análisis.

**Archivos**
- `README.md`: Este archivo, que proporciona una visión general del proyecto y su propósito.
- `main.py`: El archivo principal para ejecutar el dashboard.
- `requirements.txt`: Archivo que lista las dependencias del proyecto para su instalación.

## Requisitos
El proyecto usa uv para la gestión de dependencias. Para instalar las dependencias necesarias, ejecuta el siguiente comando en la terminal:

```bash
$ uv init
$ uv sync
```

## Autor
- **Jorge Luis Toral Gamez** - [LinkedIn](https://www.linkedin.com/in/jorge-luis-toral-gamez/)

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.