import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
names = [
    "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
    "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
    "Diana", "Radu", "Laura", "Cristian", "Raluca",
    "Bianca",
]

numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32]

def ordered_names_view(request):
    ordered_names = sorted(names)
    return HttpResponse(", ".join(ordered_names))

def ordered_numbers_view(request):
    ordered_numbers = sorted(numbers, reverse=True)
    return HttpResponse(", ".join(map(str, ordered_numbers)))
