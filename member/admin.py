from django.contrib import admin
from .models import Exituser, Prod_Categ_big, Prod_Categ_mid, Prod_Categ_sma, User,Term

class Termconfig(admin.ModelAdmin):
    readonly_fields=('registerday',)

admin.site.register(User)
admin.site.register(Term,Termconfig)
admin.site.register(Exituser)
admin.site.register(Prod_Categ_big)
admin.site.register(Prod_Categ_mid)
admin.site.register(Prod_Categ_sma)
# Register your models here.