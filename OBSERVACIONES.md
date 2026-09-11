# Observaciones — respuesta al feedback

## 1. Proyecto en la raíz
- Antes: `lab01_quispe/todoproject/` (mencionado por el docente).
- Ahora: `manage.py`, `todoproject/`, `tasks/`, `calculadora/` en la **raíz**.
- Se eliminó la carpeta intermedia `lab01_quispe/` y no se versiona `db.sqlite3`.

## 2. `.gitignore`
- Incluye `*.sqlite3`, `*.db`, `__pycache__/`, `*.pyc`, `.venv/`, `.env`, `*.log`, `.idea/`, `.vscode/`.
- Verificado: `git status` no muestra `db.sqlite3` ni `__pycache__`.

## 3. `requirements.txt`
- Generado desde el entorno verificado (`py -m pip freeze`): `Django==6.1`, `asgiref`, `sqlparse`, `tzdata`.
- Se excluyeron paquetes no usados por el proyecto (`djangorestframework`, `django-cors-headers` estaban instalados globalmente pero no están en `INSTALLED_APPS`).

## 4. README
- Con estructura, instalación, rutas y verificación.

## 5. Commits progresivos
- `feat: base Django en raiz (config todoproject + manage.py)`
- `feat(tasks): app lista de tareas`
- `feat(calculadora): operaciones suma/resta/multiplicacion`
- `chore: agrega .gitignore, requirements.txt, README y OBSERVACIONES`
