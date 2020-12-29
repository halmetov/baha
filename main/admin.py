from django.contrib import admin
from main.models import *
# Register your models here.


class CaruselAdmin(admin.ModelAdmin):
    pass

admin.site.register(Carusel, CaruselAdmin)




####################################################
class BestServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(BestService, BestServiceAdmin)




####################################################
class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)



####################################################
class RecoveryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recovery, RecoveryAdmin)




####################################################
class ServiceProcessAdmin(admin.ModelAdmin):
    pass

admin.site.register(ServiceProcess, ServiceProcessAdmin)



####################################################
class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(Staff, StaffAdmin)



####################################################
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)




####################################################
class FeedbackAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feedback, FeedbackAdmin)



####################################################
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)



####################################################
class BlogcommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blogcomment, BlogcommentAdmin)


####################################################
class ClientSaysAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClientSays, ClientSaysAdmin)


####################################################
class BrandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Brand, BrandAdmin)



####################################################
class InformationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Information, InformationAdmin)



####################################################
class AboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(About, AboutAdmin)




####################################################
class About_actionAdmin(admin.ModelAdmin):
    pass

admin.site.register(About_action, About_actionAdmin)



####################################################
class About_serviceAdmin(admin.ModelAdmin):
    pass

admin.site.register(About_service, About_serviceAdmin)



####################################################
class BlogQouteAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogQoute, BlogQouteAdmin)



###################################################
class PriceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Price, PriceAdmin)




###################################################
class FaqAdmin(admin.ModelAdmin):
    pass

admin.site.register(Faq, FaqAdmin)



###################################################
class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)


###################################################
class ContactPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(ContactPost, ContactPostAdmin)



###################################################
class ProductcommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Productcomment, ProductcommentAdmin)