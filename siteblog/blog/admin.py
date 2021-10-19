from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    form = PostAdminForm
    save_as = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')
    list_display_links =('id', 'title', 'slug',)
    search_fields = ('id', 'title')
    list_filter = ('category', 'tags')
    readonly_fields = ('created_at', 'get_photo', )
    fields = ('title', 'slug', 'content', 'category', 'created_at', 'photo','get_photo', 'views', 'tags',)

    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src = "{obj.photo.url}" widht="50">')
        return '-'
    get_photo.short_description = 'Foto'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)