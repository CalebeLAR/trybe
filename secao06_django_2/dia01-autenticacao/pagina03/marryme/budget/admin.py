from django.contrib import admin
from .models import Vendor, Marriage, Budget

admin.site.site_header = "s2_MARRYME_s2"


class BudgetInline(admin.StackedInline):
    model = Budget


class MarriageAdmin(admin.ModelAdmin):
    inlines = [BudgetInline]


admin.site.register(Vendor)
admin.site.register(Marriage, MarriageAdmin)
