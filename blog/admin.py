from django.contrib import admin
from .models import Blog
from .models import Portpolio
from .models import Pictures
#추가해주기
# Register your models here.
admin.site.register(Blog)
admin.site.register(Portpolio)
admin.site.register(Pictures) 
#admin 사이트에 등록해라라는뜻