from django.contrib import admin
from .models import Post

# Register your models here.
# Registrar  el modelo 
# Forma optimizada de customizar nuestra  aplicacion de Django
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Habilitando Filtros  en la seccion de administrador
    list_display =['title','slug','author','publish','status']
    list_filter=["status","created","publish",'author']
    search_fields=["title",'body']
    prepopulated_fields ={'slug':('title',)}
    raw_id_fields=['author']
    date_hierarchy ='publish'
    ordering =['status','publish']
   