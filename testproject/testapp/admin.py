from django.contrib import admin
from testapp.models import *
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(User)