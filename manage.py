#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario_simba.settings')
    
    # Handle custom port from environment variable
    port = os.getenv('PORT', '8000')  # Default to 8000 if PORT is not set

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Adjust arguments to bind to 0.0.0.0 and the port from the environment variable
    if 'runserver' in sys.argv:
        sys.argv.append(f'0.0.0.0:{port}')
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()





#!/usr/bin/env python
# import os
# import sys

# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario_simba.settings')

#     port = os.getenv('PORT', '8000')

#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc

#     if 'runserver' in sys.argv:
#         sys.argv.append(f'0.0.0.0:{port}')
#         sys.argv.append('--noreload') 

#     execute_from_command_line(sys.argv)

# if __name__ == '__main__':
#     main()
