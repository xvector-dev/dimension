from django.urls import path
from .views import conversational, code_generation, seo_generation, sales

urlpatterns = [
    path('conversation/', conversational, name='conversation'),
    path('code-generation/', code_generation, name='code-generation'),
    path('seo-generation/', seo_generation, name='seo-generation'),
    path('sales/', sales, name='sales')
]
