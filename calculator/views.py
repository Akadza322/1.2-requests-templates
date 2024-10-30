from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet_view(request):
    servings = int(request.GET.get('number', 1))
    if servings > 1:
        omlet = {}
        omlet.update((key, value * servings) for key, value in DATA['omlet'].items())
        context = {
            'recipe': omlet,
        }
    else:
        context = {
            'recipe': DATA['omlet'],
        }
    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    servings = int(request.GET.get('number', 1))
    if servings > 1:
        pasta = {}
        pasta.update((key, value * servings) for key, value in DATA['pasta'].items())
        context = {
            'recipe': pasta,
        }
    else:
        context = {
            'recipe': DATA['pasta'],
        }
    return render(request, 'calculator/index.html', context)

def buter_view(request):
    servings = int(request.GET.get('number', 1))
    if servings > 1:
        buter = {}
        buter.update((key, value * servings) for key, value in DATA['buter'].items())
        context = {
            'recipe': buter,
        }
    else:
        context = {
            'recipe': DATA['buter'],
        }
    return render(request, 'calculator/index.html', context)