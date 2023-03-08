apt install python3.10-venv

linux vs code
    python3 -m venv ve

windows vs code
    py -m venv ve

linux vs code
source ve/bin/activate
    source /home/kirill/Python/va_ecom/ve/bin/activate

windows vs code
    ve\Scripts\Activate.ps1


C:\Python\dj_very_academy\ve\Scripts\python.exe -m pip install --upgrade pip

pip install django black

django-admin startproject drfecommerce 

cd drfecommerce

black "--line-length=79" ./

linux
    ./manage.py runserver

windows
    python manage.py runserver
    
Started lesson:
    https://www.youtube.com/@veryacademy
    Django DRF Project | Modularizing Django Settings | 2 
    https://youtu.be/0WXVAMGisWs



python manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    m0zl&+r%jyb0$6l+7@v)qaclmgq2awf^4_cj1b5=qm&uwvk5$c

    Use quit() or Ctrl-Z plus Return to exit


pip freeze > requirements.txt

pip install -r requirements.txt

https://pypi.org/project/python-dotenv/

pip install python-dotenv

pip install djangorestframework

https://pypi.org/

https://www.django-rest-framework.org/

https://pypi.org/project/pytest/

pip install pytest==7.2.2

(ve) (base) PS C:\Python\dj_very_academy> pytest

pytest -h

pip instal pytest-django==4.5.2

https://pytest-django.readthedocs.io/en/latest/

# -- FILE: pytest.ini (or tox.ini)
[pytest]
DJANGO_SETTINGS_MODULE = test.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py