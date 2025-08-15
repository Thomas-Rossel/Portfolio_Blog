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
            'title': 'Gymtrack',
            'description': 'Aplicación web para registrar entrenamientos en el gimnasio y hacer una optima sobrecarga progresiva',
            'technologies': ['Next.js', 'Javascript', 'SQL'],
            'image': 'Gymtrack.jpg',
            'github': '#',
            'demo': '#',
            'status': 'Completado'
        },
        {
            'title': 'Remake Space Invaders',
            'description': 'Remake del famoso juego de naves espaciales "Space Invaders", lo hice como un proyecto en la secundaria',
            'technologies': ['Python', 'Pygame', 'Json'],
            'image': 'Space-Invaders.jpg',
            'github': '#',
            'demo': '#',
            'status': 'Completado'
        },
        {
            'title': 'BookReader',
            'description': 'Una aplicacion donde alguien interesado en los libros puede ingresar y buscar distintas recomendaciones segun sus generos favoritos',
            'technologies': ['Django', 'HTML', 'Javascript'],
            'image': 'libro.jpg',
            'github': '#',
            'demo': '#',
            'status': 'En desarrollo'
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
            'email': 'thomy17fr@gmail.com',
            'github': 'https://github.com/thomas-rossel',
            'location': 'Buenos Aires, Argentina'
        }
    }
    return render(request, 'portfolio/contact.html', context)