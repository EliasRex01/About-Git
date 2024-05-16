# cuando no quieres que un archivo o carpeta entre en el control de versiones se usa este archivo
# registrando su nombre dentro del archivo

# .gitignore (contenido abajo)
.lib/
temp/
pass.*    # cualquiera de nombre pass no importa la extension
clave.txt
*.exe     # cualquier archivo de tipo exe
/config       (muy usado al momento de hacer proyectos compartidos)

# agregando el gitignore
git status
git add .gitignore

# intentando agregar un archivo de gitignore
git add clave.txt
# no dejaria agregarlo y si se fuerza no tendria seguimiento del control de versiones

# para ver la ayuda es con git help
git help

# web para crear estos archivos
toptal.com gitignore.io
# seleccionar las caracteristicas y luego el texto generado se copia a nuestro 
# archivo .gitignore
