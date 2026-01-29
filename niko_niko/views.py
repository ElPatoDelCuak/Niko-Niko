from django.shortcuts import render
import random

# Recipe data
RECIPES = [
    {
        'id': 1,
        'title': 'Ramen Tonkotsu Clásico',
        'category': 'Fideos',
        'description': 'Caldo cremoso y rico de huesos de cerdo con chashu tierno, huevo cocido y fideos frescos.',
        'image': 'img/recipe-ramen.jpg',
        'time': '4 horas',
        'servings': '4 raciones'
    },
    {
        'id': 2,
        'title': 'Gyoza Crujiente',
        'category': 'Aperitivos',
        'description': 'Empanadillas a la plancha con jugoso relleno de cerdo y una base perfectamente crujiente.',
        'image': 'img/recipe-gyoza.jpg',
        'time': '45 min',
        'servings': '6 raciones'
    },
    {
        'id': 3,
        'title': 'Brazo de Gitano de Matcha',
        'category': 'Postres',
        'description': 'Bizcocho ligero y esponjoso de té verde relleno de delicada nata montada.',
        'image': 'img/recipe-matcha.jpg',
        'time': '1 hora',
        'servings': '8 raciones'
    },
    {
        'id': 4,
        'title': 'Pollo Teriyaki',
        'category': 'Plato Principal',
        'description': 'Pollo jugoso glaseado con un equilibrio perfecto entre sabores dulces y salados.',
        'image': 'img/recipe-teriyaki.jpg',
        'time': '30 min',
        'servings': '4 raciones'
    },
    {
        'id': 5,
        'title': 'Bolitas de Pulpo Takoyaki',
        'category': 'Aperitivos',
        'description': 'Doradas y crujientes por fuera, cremosas por dentro con tiernos trozos de pulpo.',
        'image': 'img/recipe-takoyaki.jpg',
        'time': '40 min',
        'servings': '24 piezas'
    },
    {
        'id': 6,
        'title': 'Sopa de Miso',
        'category': 'Sopas',
        'description': 'Sopa japonesa tradicional con tofu, alga wakame y un caldo de miso rico en umami.',
        'image': 'img/recipe-miso.jpg',
        'time': '15 min',
        'servings': '4 raciones'
    },
]

VALORATIONS = [
    {
        'text': 'Las recetas son increíbles, fáciles de seguir y el resultado siempre queda delicioso. ¡Muy recomendado!',
        'author': 'Juan Pérez',
        'occupation': 'Chef',
        'stars': 5
    },
    {
        'text': 'Me gusta la web, pero algunas recetas tienen pasos confusos y tardan mucho en explicarse.',
        'author': 'Pedro Sanchez',
        'occupation': 'Blogger',
        'stars': 3
    },
    {
        'text': 'Probé el ramen y me salió espectacular, como en un restaurante japonés. Definitivamente repetiré.',
        'author': 'Lucía Fernández',
        'occupation': 'Entusiasta de la Cocina',
        'stars': 5
    },
    {
        'text': 'Las instrucciones son claras, pero algunos ingredientes son difíciles de conseguir. Aún así merece la pena.',
        'author': 'Carlos Ruiz',
        'occupation': 'Cocinero Casero',
        'stars': 4
    },
    {
        'text': 'No me gustó mucho, los sabores no eran lo que esperaba y algunas recetas estaban incompletas.',
        'author': 'Sofía Martínez',
        'occupation': 'Crítica Gastronómica',
        'stars': 2
    },
    {
        'text': 'Me encantó la sección de postres, hice el rollo de matcha y fue un éxito total con mi familia.',
        'author': 'María López',
        'occupation': 'Amante de la Comida',
        'stars': 5
    },
    {
        'text': 'Está bien para principiantes, pero esperaba más variedad en los platos principales.',
        'author': 'Pablo Sánchez',
        'occupation': 'Estudiante de Cocina',
        'stars': 3
    },
    {
        'text': 'Algunas recetas requieren ingredientes caros o difíciles de encontrar, lo que hace que no sean tan prácticas.',
        'author': 'Elena Torres',
        'occupation': 'Cocinera Aficionada',
        'stars': 3
    },
    {
        'text': 'Excelente página, todo muy bien explicado y las fotos ayudan mucho a entender el resultado final.',
        'author': 'Miguel Ramírez',
        'occupation': 'Chef Profesional',
        'stars': 5
    },
    {
        'text': 'La sección de sopas es fantástica, pero los postres podrían tener más opciones sin azúcar.',
        'author': 'Isabel Navarro',
        'occupation': 'Nutricionista',
        'stars': 4
    }
]


FAQS = [
    {
        'question': '¿Qué tipo de recetas puedo encontrar en Niko-Niko?',
        'answer': 'En Niko-Niko, ofrecemos una amplia variedad de recetas japonesas tradicionales y modernas, desde platos principales hasta aperitivos y postres.'
    },
    {
        'question': '¿Las recetas son aptas para principiantes?',
        'answer': 'Sí, nuestras recetas están diseñadas para ser fáciles de seguir, con instrucciones claras y detalladas, ideales tanto para principiantes como para cocineros experimentados.'
    },
    {
        'question': '¿Puedo encontrar opciones vegetarianas o veganas?',
        'answer': 'Absolutamente. Contamos con una selección de recetas vegetarianas y veganas para satisfacer diferentes preferencias dietéticas.'
    },
    {
        'question': '¿Necesito ingredientes especiales para cocinar las recetas?',
        'answer': 'La mayoría de nuestras recetas utilizan ingredientes que se pueden encontrar en supermercados comunes. Sin embargo, algunas recetas pueden requerir ingredientes específicos de la cocina japonesa, que también son fáciles de conseguir en tiendas especializadas o en línea.'
    },
    {
        'question': '¿Puedo compartir mis propias recetas en Niko-Niko?',
        'answer': 'Actualmente, Niko-Niko no permite a los usuarios compartir sus propias recetas, pero estamos considerando esta función para el futuro.'
    },
    {
        'question': '¿Cómo puedo contactar con el equipo de Niko-Niko?',
        'answer': 'Puedes contactarnos a través de la página de contacto en nuestro sitio web, donde encontrarás un formulario para enviarnos tus preguntas o comentarios.'
    },
    {
        'question': '¿Ofrecen contenido adicional como videos o tutoriales?',
        'answer': 'Sí, además de las recetas escritas, ofrecemos videos y tutoriales para ayudarte a mejorar tus habilidades culinarias y aprender técnicas específicas de la cocina japonesa.'
    }
]

# Create your views here.
def home(request):
    # Get 3 random recipes
    featured_recipes = random.sample(RECIPES, min(3, len(RECIPES)))
    context = {'recipes': featured_recipes}
    # Get 3 random valorations
    featured_valorations = random.sample(VALORATIONS, min(3, len(VALORATIONS)))
    context['valorations'] = featured_valorations
    # Get 4 faqs randomly
    featured_faqs = random.sample(FAQS, min(4, len(FAQS)))
    context['faqs'] = featured_faqs
    return render(request, 'niko_niko/home.html', context)

def recipe(request):
    return render(request, 'niko_niko/recipe.html')

def about(request):
    return render(request, 'niko_niko/about.html')

def contact(request):
    return render(request, 'niko_niko/contact.html')