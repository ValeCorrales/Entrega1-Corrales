# Entrega1-Corrales/Renzi

Blog de Viajes - Descubriendo el Mundo

La idea del blog es que los visitantes puedan aconsejar sobre Ciudades, Restaurantes y Alojamiento

Ejecución

1. Para clonar el proyecto y poder ejecutarlo es necesario:
 - Copiar la url del mismo : https://github.com/ValeCorrales/Entrega1-Corrales.git
 - Abrir Git y clonarlo en la ubicación deseada. Ubicarse en la consola en la carpeta deseada y tipear el comando git clone https://github.com/ValeCorrales/Entrega1-Corrales.git
 
2. Una vez clonado, abrir la carpeta en un editor de código y ejecutar en la Terminal (en la carpeta correspondiente) el comando python manage.py runserver

3. En el exploarador de internet  abrir http://127.0.0.1:8000/App/inicio/

- Modelamos ciudades, restaurantes y alojamientos, se puede navegar hacia ellos desde cualquier pagina.

- Dentro de cada una de las paginas de los modelos se encuentra un formulario para agregar instancias a la base de datos. 

- Modelamos tambien la entidad comentarios a la cual se le agregan registros desde el formulario de contacto.