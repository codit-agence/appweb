from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Article, Category, Picture, Service, Action
from contact.forms import ContactForms, ContactInscriptionForms
from contact.models import Contact
from django.contrib import messages

def gestion_index(request):

    articles=Article.objects.all()
    images = Picture.objects.filter(title__startswith='about')
    services = Service.objects.all()

    return render(request, 'index.html',  {
                                            'articles':articles,
                                            'images':images,
                                            'services':services
                                           })


def gestion_service(request):
    actions = Action.objects.all()
    services = Service.objects.all()

    return render(request, 'services.html', {
                                            'actions':actions,
                                            'services':services
                                             })


def gestion_blog(request):
    return render(request, 'blogs.html', {})


def gestion_partner(request):
    return render(request, 'partners.html', {})


def gestion_contact(request):
    form = ContactForms()

    if request.method=="POST":
        form = ContactForms(request.POST or None)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            message=form.cleaned_data.get('message')
            title=form.cleaned_data.get('title')
            tel=form.cleaned_data.get('tel')
            ville=form.cleaned_data.get('ville')
            form.save()
            return redirect('gestion:contact')

    return render(request, 'contacts.html', {
                                             'form':form,
                                             })


def gestion_inscription(request):
    form = ContactInscriptionForms()

    if request.method=="POST":
        form = ContactInscriptionForms(request.POST or None)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            message=form.cleaned_data.get('message')
            tel=form.cleaned_data.get('tel')
            ville=form.cleaned_data.get('ville')
            form.save()
            return redirect('gestion:inscription')

    return render(request, 'inscription.html', {
                                             'form':form,
                                             })


def gestion_project(request):
    return render(request, 'projects.html', {})
