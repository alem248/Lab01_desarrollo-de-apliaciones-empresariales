# Lab01 — Desarrollo de Aplicaciones Empresariales (Django)

Base: https://github.com/alem248/Lab01_desarrollo-de-apliaciones-empresariales.git
(reordenado: proyecto ahora en la **raíz**, antes colgaba de `lab01_quispe/todoproject/`).

## Estructura (raíz)
```
manage.py
todoproject/      # settings, urls, wsgi/asgi
tasks/            # app tareas (lista en /)
calculadora/      # app operaciones (en /app/)
requirements.txt
.gitignore
README.md
OBSERVACIONES.md
```

## Requisitos
- Python 3.13 + Django 6.1 (ver `requirements.txt`)

## Instalación
```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

## Rutas
- `/` → `tasks:task_list`
- `/app/sumar/<a>/<b>/`, `/app/restar/<a>/<b>/`, `/app/multiplicar/<a>/<b>/`
- `/admin/`

## Verificación
```bash
py manage.py check
py manage.py test
```

## Notas
- No se versiona `db.sqlite3` (ver `.gitignore` y `OBSERVACIONES.md`). Se genera local con `migrate`.
