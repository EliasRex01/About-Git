-- abrir terminal de git en la carpeta donde se desea crear la rama

-- dentro de la terminal
git status

-- crear una rama 
-- forma 1
git branch nombre_rama

-- forma 2
git checkout -b nombre_rama

-- Como crear ramas en git
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
