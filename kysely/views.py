from django.shortcuts import render



def index(request):
    return HttpResponse("Heippa! Olet kysely-appin index-sivulla.")
