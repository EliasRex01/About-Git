// Agregar control de versiones desde terminal git
// crear un repositorio vacio
  git init
git init .
// añadir todos los archivos en la carpeta al control de versiones
  git add .

// ver los archivos añadidos sin conmitear
  git status

// hacer el conmiteo (ejemplo)
  git commit -am "Inicial"

// para ver los commit hechos
  git log


// ver configuraciones
git config --list --global    // puede ser local tambien

// para ver las opciones con config
git config

// para cambiar el usuario
git condig --global user.name "Elias Oviedo"
// para 


Crear usuario en git
git --global user.name "Elias Oviedo"

Crear email del usuario
git config --local user.email "elias@ggamil.com"
git config --list --global


Eqtiquetas
git commint -a -m "segundo cambio"
Poniendo etiqueta
git tag -a "v2.0" identificador
Copiar el identificador a la izquierda de donde dice head-master
Después al usar git log se puede ver las etiquetas o las versiones del archivo (puesto que se hizo cambios en un archivo y después se hizo el nuevo commint).

Moverse entre versiones
git branch -1
git checkout v1.0
git checkout v2.0

Cómo desastre un commint y volver al anterior
git revert (número de comint, el que está alado de head-master)
 
Remover un fichero de las versiones
git rm nom_archivo
git -a -m "fichero eliminado 01.txt"


Desaser todo
git reset --hard

Crear fichero texto desde consola
copy con fichero.txt
echo mensaje > archivo01.txt
git log --oneline

Ver texto del archivo
type archivo01.txt

Ir hacia atrás o a la versión anterior
git reset --soft HEAD~1


Ver si hay diferencias
git diff

Como volver a una versión anterior de un archivo
git reset --hard
git log --oneline

Como crear ramas en git
( No sé borra una rama sino que se hace es copiar una rama y trabajar sobre esa)
git status (muestra si hay algo que commintear)
git branch desarrollo
git checkout -b desarrollo02

La dif entre el branch y el checkout es que el segundo ya te lleva a la rama para trabajar y en el primero debes cambiar de rama.
git status

git add .
git commit -am "añadido el fichero"
git log --oneline

Cambiar de rama
git checkout master (llendo a la rama master)
git checkout desarrollo (a la rama desarrollo)
git status
git add .
git status

git commit -am "archivo creado y modificado en la rama desarrollo"
