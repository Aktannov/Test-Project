# Test Project


### Описание установки проекта:


# Запуск с окружением:
'''
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt

./manage.py runserver

'''



# Запуск без окружения:
'''
chmod +x manage.py
pip install -r requirements.txt
./manage.py runserver
'''


# Создание админа:
'''
./manage.py createsuperuser
'''


# Команда для создании миграции после изменения моделей:
'''
./manage.py makemigrations
./manage.py migrate
'''