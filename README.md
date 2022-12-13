cd Desenvolvimento/
source plataforma_env/bin/activate
cd PLATAFORMA_PROJETO/PLATAFORMA_prj/
python3 manage.py runserver


git config --global user.email "tiagopena@yahoo.com.br"
git config --global user.name "tiagopena"

git add .
git commit -m ""
git remote add origin https://github.com/tiagopena/CUSTO_prj.git
git push -u origin master