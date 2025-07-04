from django.contrib import admin

# Register your models here.

from .models import Barang, Jenis, About, Feature
from django.utils.html import format_html

class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg','nama','stok','harga','link_gbr','tgl_input','id_jenis')
    search_fields = ('kdbrg','nama', 'id_jenis__nama')
    list_per_page = 3
    list_filter = ('id_jenis__nama',)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('pengantar','fet1', 'isi_fet1', 'fet2', 'isi_fet2', 'img_thumb' )

    def img_thumb(self,obj):
        if obj.img_fet:
            return format_html('<img src="{}" width="150" />'.format(obj.img_fet.url))
        else:
            return 'No Image'

    img_thumb.short_description = 'Gambar'

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About)
admin.site.register(Feature, FeatureAdmin)
