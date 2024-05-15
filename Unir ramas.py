-- como unificar ramas

-- se crea una rama
git checkout -b prueba2

git status
git add .
git commit -am "cambio desde prueba2"
git log --oneline

git checkout master
git log --oneline

-- Unificando las ramas 1 y 2

-- ver listado de ramas
git branch

-- unificando 2 ramas
git merge prueba1
git log --oneline

git merge prueba2
git log --oneline

-- se unieron a la rama principal
