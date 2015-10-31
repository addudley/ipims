@ECHO off
CLS
ECHO Preparing Virtualenv...
virtualenv env >nil
set VIRTUAL_ENV_DISABLE_PROMPT = 1 >nil
cmd /k "env\scripts\activate.bat & cd /d src & ECHO Fixing dependencies... & pip uninstall -y pillow > nil & pip install pillow >nil & start "" /min ..\env\elasticsearch\bin\elasticsearch.bat & ECHO Starting ElasticSearch... & timeout 6 >nul & ECHO Rebuilding index... & manage.py rebuild_index --noinput >nil & CLS & ECHO --------------------------------------- & ECHO. & ECHO Django Development Server: Running & ECHO. & ECHO ElasticSearch server: Running & ECHO. & ECHO --------------------------------------- & ECHO. & ECHO Access the IPIMS at http://127.0.0.1:8000. & ECHO. & ECHO Press Ctrl+C on this window to turn off servers before using 'git commit'. & manage.py runserver --verbosity 0 >nul & cd ../ & env\scripts\deactivate.bat"

