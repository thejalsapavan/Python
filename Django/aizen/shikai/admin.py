from django.contrib import admin
from .models import Employee
# Register your models here.
#admin.site.register(Employee)
@admin.register(Employee)
class filt(admin.ModelAdmin):
    list_display=('eid','nam','sal','ad')
    list_filter=('sal',)
    ordering=('nam',)
    search_fields=('nam',)

