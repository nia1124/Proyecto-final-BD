from django.shortcuts import render

# Create your views here.

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from proyectoauxiliares.models import *

def main(request):
    estudiante = Estudiante.objects.all().order_by("-edad")
    paginator = Paginator(estudiante,3)

    try: pagina = int(request.GET.get("page",'1'))
    except ValueError: pagina=1

    try: estudiante = paginator.page(pagina)
    except (InvalidPage,EmptyPage):
        estudiante = paginator.page(paginator.num_pages)

    return render_to_response("listado.html",dict(estudiante = estudiante, usuario=request.user))
