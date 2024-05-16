# control de versiones desde github

# crear una carpeta y conectar a github
# se crea normal el repositorio
# se conecta mediante code y se copia alguna direccion, http u otra

# la carpeta del equipo local y el repositorio con el mismo nombre

# desde la terminal 
git remote -v
# cambiar la rama de master a env (que lleva github)
git branch -m main

# se hace la conexion
git remote add pruebas link_copiado

# comprobacion del remoto
git remote -v

# fetch de la carpeta pruebas que se crea en el equipo local
git fetch pruebas main

# se agrega la carpeta al repositorio de github
git pull pruebas main

git add .
git status
git commit -am "inicio git"

# mandar un archivo recien creado
git push pruebas main
