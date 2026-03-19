#!/usr/bin/env python
import os
import sys

def main():
    # Isso força o Python a incluir a pasta atual na busca de módulos
    current_path = os.path.dirname(os.path.abspath(__file__))
    if current_path not in sys.path:
        sys.path.append(current_path)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Verifique se a venv está ativa."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()