from django.shortcuts import render

def home(request):
    """Vista para la página principal del portfolio"""
    return render(request, 'portfolio/home.html', {
        'title': 'Inicio'
    })

def about(request):
    """Vista para la página sobre mí"""
    context = {
        'title': 'Sobre Mí',
        'skills': [
            {'name': 'Python', 'level': 90, 'icon': 'fab fa-python', 'color': 'warning'},
            {'name': 'Django', 'level': 80, 'icon': 'fas fa-globe', 'color': 'success'},
            {'name': 'JavaScript', 'level': 70, 'icon': 'fab fa-js-square', 'color': 'warning'},
            {'name': 'HTML/CSS', 'level': 85, 'icon': 'fab fa-html5', 'color': 'danger'},
            {'name': 'Git', 'level': 75, 'icon': 'fab fa-git-alt', 'color': 'dark'},
            {'name': 'Bases de Datos', 'level': 70, 'icon': 'fas fa-database', 'color': 'info'},
        ],
        'education': [
            {
                'institution': 'Instituto Técnico Huergo',
                'degree': 'Técnico en Informática',
                'year': '2021 - 2025',
                'description': 'Especialización en programación y sistemas computacionales'
            }
        ]
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    """Vista para la página de proyectos"""
    projects_list = [
        {
            'title': 'Sistema de Gestión Escolar',
            'description': 'Aplicación web desarrollada en Django para gestionar estudiantes, profesores y calificaciones.',
            'technologies': ['Python', 'Django', 'SQLite', 'Bootstrap'],
            'image': 'default.jpg',  # Cambiar por imagen real
            'github': '#',
            'demo': '#',
            'status': 'Completado'
        },
        {
            'title': 'Bot de Discord',
            'description': 'Bot multifuncional para Discord con comandos de moderación y entretenimiento.',
            'technologies': ['Python', 'Discord.py', 'APIs'],
            'image': 'default.jpg',
            'github': '#',
            'demo': '#',
            'status': 'En desarrollo'
        },
        {
            'title': 'Calculadora Científica',
            'description': 'Calculadora con interfaz gráfica desarrollada en tkinter con funciones avanzadas.',
            'technologies': ['Python', 'Tkinter', 'Math'],
            'image': 'default.jpg',
            'github': '#',
            'demo': '#',
            'status': 'Completado'
        }
    ]
    
    context = {
        'title': 'Proyectos',
        'projects': projects_list
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    """Vista para la página de contacto"""
    context = {
        'title': 'Contacto',
        'contact_info': {
            'email': 'thomas.rossel@ejemplo.com',  # Cambiar por email real
            'github': 'https://github.com/thomas-rossel',
            'linkedin': '#',  # Agregar LinkedIn si lo tiene
            'location': 'Buenos Aires, Argentina'
        }
    }
    return render(request, 'portfolio/contact.html', context)