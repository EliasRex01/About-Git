-- indica los commit, ramas, de forma visual
git log --oneline --graph --all

-- craer rama
git checkout -b modificaciones
git commit -am "fichero 02 cambiado"
-- se modifica el archivo 01
git log --oneline
git status
git commit -am

git checkout master
git log --oneline

-- agregar el cambio de la rama modificaciones
git cherry-pick id_linea fichero02 cambiado  (linea con el mensaje)
git log --oneline

-- usar para que incluya los del rango pero sin incluir
git cherry-pick id1..id7

-- incluyendo inicio a final
git cherry-pick id1^..id7
