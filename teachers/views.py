from django.shortcuts import render, get_object_or_404
from .models import Teacher

# Create your views here.


def all_teachers(request):
    """ A view to show all teachers, or a particular teacher """

    teachers = Teacher.objects.all()
    teacher = None

    if request.GET:
        if 'name' in request.GET:
            name = request.GET['name']
            teachers = Teacher.objects.filter(name=name)

    context = {
        'teachers': teachers,
    }

    return render(request, 'teachers/teachers.html', context)


