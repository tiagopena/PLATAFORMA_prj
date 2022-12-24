cd Desenvolvimento/
source plataforma_env/bin/activate
cd PLATAFORMA_PROJETO/PLATAFORMA_prj/
sudo git pull origin
python3 manage.py runserver

WINDOWS
cd \Users\tiago\OneDrive\Documentos\Desenvolvimento\
.\smartweb_env\Scripts\activate
cd PLATAFORMA_prj
python manage.py runserver


git config --global user.email "tiagopena@yahoo.com.br"
git config --global user.name "tiagopena"

git add .
git commit -m ""
git remote add origin https://github.com/tiagopena/PLATAFORMA_prj.git
git push -u origin main