from django.contrib import admin
from basics import models


class PMAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(responsible_group__in=request.user.groups.all())


@admin.register(models.T_1)
class T1Admin(PMAdmin):
    fields = (
        "name",
        "responsible_group",
    )
    list_display = ("name",)


@admin.register(models.T_2)
class T2Admin(PMAdmin):
    fields = (
        "name",
        "responsible_group",
    )
    list_display = ("name",)


@admin.register(models.T_3)
class T3Admin(PMAdmin):
    fields = (
        "name",
        "responsible_group",
    )
    list_display = ("name",)


admin.site.site_header = "Портал"
admin.site.site_title = "Портал"
admin.site.index_title = "Добро пожаловать"
