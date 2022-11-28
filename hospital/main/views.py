from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Specialization, Disease, Patient, Doctor, Diagnosis
from .forms import SpecForm, DisForm, PatForm, DocForm, DiagForm
from django.contrib import messages



def index(request):
    dis = Disease.objects.all()
    spec = Specialization.objects.all()
    pat = Patient.objects.all()
    doc = Doctor.objects.all()
    diag = Diagnosis.objects.all()

    search_query= request.GET.get('q')
    groups ={dis, spec, pat, doc, diag}



    return render(request, 'main/index.html', {'title': 'Main page', 'specs': spec, 'diseases': dis,
                                               'patients': pat, 'doctors': doc,'diagnosis': diag} )


def about(request):
    return render(request, "main/about.html")

def create(request):
    return render(request, "main/create.html")



def createSpec(request):
    error = ''
    if request.method =='POST':
        form = SpecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Введені некоректні дані'

    form = SpecForm()
    context = {
    'form': form,
    'error': error
    }
    return render(request, "main/createSpecialization.html", context)

def deleteSpec(request, id):
    try:
        person = Specialization.objects.get(spec_id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Specialization.DoesNotExist:
        return HttpResponseNotFound("<h2>Помилка</h2>")

def createDis(request):
    error = ''
    if request.method =='POST':
        form = DisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Введені некоректні дані'

    form = DisForm()
    context = {
    'form': form,
    'error': error
    }
    return render(request, "main/createDis.html", context)

def deleteDis(request, id):
    try:
        person = Disease.objects.get(dis_id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Specialization.DoesNotExist:
        return HttpResponseNotFound("<h2>Помилка</h2>")

def createPat(request):
    error = ''
    if request.method =='POST':
        form = PatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Введені некоректні дані'

    form = PatForm()
    context = {
    'form': form,
    'error': error
    }
    return render(request, "main/createPat.html", context)


def deletePat(request, id):
    try:
        person = Patient.objects.get(pat_id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Specialization.DoesNotExist:
        return HttpResponseNotFound("<h2>Помилка</h2>")

def createDoc(request):
    error = ''
    if request.method =='POST':
        form = DocForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Введені некоректні дані'

    form = DocForm()
    context = {
    'form': form,
    'error': error
    }
    return render(request, "main/createDoc.html", context)

def deleteDoc(request, id):
    try:
        person = Doctor.objects.get(doc_id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Specialization.DoesNotExist:
        return HttpResponseNotFound("<h2>Помилка</h2>")

def createDiag(request):
    error = ''
    if request.method =='POST':
        form = DiagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Введені некоректні дані'

    form = DiagForm()
    context = {
    'form': form,
    'error': error
    }
    return render(request, "main/createDiag.html", context)


def deleteDiag(request, id):
    try:
        person = Diagnosis.objects.get(diag_id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Specialization.DoesNotExist:
        return HttpResponseNotFound("<h2>Помилка</h2>")