from django.shortcuts import render
from rest_framework import viewsets
from .models import language
from .serializers import LanguageSerializers
# Create your views here.
class LanguageView(viewsets.ModelViewSet):
	queryset = language.objects.all()
	serializer_class = LanguageSerializers