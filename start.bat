@echo off
call bw_env\Scripts\activate
python manage.py runserver 5000
pause