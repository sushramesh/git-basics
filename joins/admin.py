from django.contrib import admin

# Register your models here.

from .models import Join

class JoinAdmin(admin.ModelAdmin):
    #code
    class Meta:
        model = Join


admin.site.register(Join)
