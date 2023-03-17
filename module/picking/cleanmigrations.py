import os

# Lista de las aplicaciones del proyecto Django
apps = ['box', 'boxitem', 'company', 'picking', 'reference', 'registration', 'saleorder', 'saleorderitem']

# Eliminar archivos de migración y la carpeta __pycache__ de la carpeta migrations de cada aplicación
for app in apps:
    migration_path = os.path.join(app, 'migrations')
    pycache_path = os.path.join(migration_path, '__pycache__')

    if os.path.exists(migration_path):
        # Eliminar archivos de migración
        for file in os.listdir(migration_path):
            if file != '__init__.py' and (file.endswith('.py') or file.endswith('.pyc')):
                os.remove(os.path.join(migration_path, file))
        print(f'Archivos de migración eliminados en la aplicación {app}')

    if os.path.exists(pycache_path):
        # Eliminar carpeta __pycache__ de migrations
        for file in os.listdir(pycache_path):
            os.remove(os.path.join(pycache_path, file))
        os.rmdir(pycache_path)
        print(f'Carpeta __pycache__ eliminada en la carpeta migrations de la aplicación {app}')