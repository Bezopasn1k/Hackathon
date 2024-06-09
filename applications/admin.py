from django.contrib import admin
from .models import Application, ApplicationTransfer


class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id_z', 'id_pas', 'datetime', 'in_p', 'out_p', 'tpz',
        'insp_sex_m', 'insp_sex_f', 'time_over', 'id_st1', 'id_st2',
        'status', 'vokzal', 'dop_inf', 'bag_s', 'pass_count', 'method_p'
    )
    list_display_links = ('id_z', 'id_pas')
    list_filter = ('datetime', 'status', 'id_st1', 'id_st2')
    search_fields = ('id_pas__fio_p', 'status')

class ApplicationTransferAdmin(admin.ModelAdmin):
    list_display = ('id_adit', 'id_bid', 'time_edit', 'get_in_p', 'time_f')
    list_display_links = ('id_adit', 'id_bid')
    list_filter = ('time_edit',)
    search_fields = ('id_bid__id_z',)

    def get_in_p(self, obj):
        return obj.time_s.in_p
    get_in_p.short_description = 'Изначальное время заявки'

admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationTransfer, ApplicationTransferAdmin)






# Register your models here.
