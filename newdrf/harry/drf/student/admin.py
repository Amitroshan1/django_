from django.contrib import admin
from .models import children
# Register your models here.

@admin.register(children)
class childrenadmin(admin.ModelAdmin):
    list_display = ['name','roll','city']
