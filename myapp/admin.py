from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
from django.utils.html import format_html
# Register your models here.


class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(ClassifyModel, ClassifyAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'actor', 'detail', 'duration', 'show_image', 'publish_time', 'classify', 'create_time')
    search_fields = ('name', 'actor')
    list_filter = ('classify', 'create_time')
    list_per_page = 20
    ordering = ('-create_time',)
    list_editable = ('name', 'actor')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 30})},
    }

    def show_image(self, obj):
        return format_html("<a href='/{0}'><img src='/{0}' style='width:50px;height:50px;'></img> </a>".format(obj.pic.url))
    show_image.short_description = 'Poster'


admin.site.site_header = 'iCine'
admin.site.site_title = 'iCine'
admin.site.register(MovieModel, MovieAdmin)
