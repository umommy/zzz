rem создать ручками github ветку zzz или:
rem curl -u umommy:113355mw7799 https://api.github.com/user/repos -d'{"name":"test3", "private":"true"}'
rem git remote add test3 git@github.com:umommy/test3.git


git init
git add .
git commit -m "first commit"
git branch -M main
git remote add zzz https://github.com/umommy/zzz.git
git push -u zzz main
