## Описание приложения
Инструмент для поиска домена под регистрацию для комерческих компаний и индивидуальных предпринимателей.

## Установка
```shell
pip -r requirements.txt
```

## Buld Production
```shell
pyinstaller -F --icon=icon.ico --add-data 'public_suffix_list.dat;whois/data/' main.py
pyarmor gen --pack dist/main.exe main.py 

```
