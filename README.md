# meat_shop

Для запуска проекта создайте виртуально окружение, активируйте его,

python(your_version) -m venv venv

source venv/bin/activate (на unit оs), venv\Scripts\activate.bat (на windows)

pip install - r requirements.txt

создайте базу данных с названием meat_shop

создайте и примините миграции 

python manage.py makemigrations
python mange.py migrate

перейдите к файлу csu.py по пути  .users/management/commands/csu.py
и заполните в нем данные для создания пользователя-администратора

Создайте супер-пользователя командой python manage.py csu

после этого можно запускать проект командой pythone manage.py runserver

перейдите по адресу 'домен/admin' войдите под тем пользователем
которого создали с помощью команды csu  

Заполните необходимые данные продукты, объеявления и тд.

