from django.contrib import admin
from .models import Fcuser


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email', )


admin.site.register(Fcuser, FcuserAdmin)
