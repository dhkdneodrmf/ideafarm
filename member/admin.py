from django.contrib import admin
from .models import Devlivery, Devlivery_com, Devlivery_term, Exituser, Prod_Categ_big, Prod_Categ_mid, Prod_Categ_sma, Product_review, Product_reviewimg, User,Term,Product_thumb,Product

class Termconfig(admin.ModelAdmin):
    readonly_fields=('registerday',)

# Product_thumb 클래스를 inline으로 나타낸다.
class ProdThmubInline(admin.TabularInline):
    model = Product_thumb

# Proudct 클래스는 해당하는 Product_thumb 객체를 리스트로 관리한다. 
class ProudctAdmin(admin.ModelAdmin):
    inlines = [ProdThmubInline, ]
    readonly_fields=('Userveiw','Userpurchase',)

class ProdreviewInline(admin.TabularInline):
    model = Product_reviewimg

class ProudctreviewAdmin(admin.ModelAdmin):
    inlines = [ProdreviewInline, ]

# Register your models here.
admin.site.register(User)
admin.site.register(Term,Termconfig)
admin.site.register(Exituser)
admin.site.register(Prod_Categ_big)
admin.site.register(Prod_Categ_mid)
admin.site.register(Prod_Categ_sma)
admin.site.register(Product, ProudctAdmin)
admin.site.register(Devlivery_com)
admin.site.register(Devlivery_term,Termconfig)
admin.site.register(Devlivery)
admin.site.register(Product_review, ProudctreviewAdmin)