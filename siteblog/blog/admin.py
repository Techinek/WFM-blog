from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    """CKEDITOR model connected with Post model"""
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    """Post model representation in the admin area
     with a form field for CKEditor model"""
    form = PostAdminForm
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('category', 'tags')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    """Category model representation in the admin area"""
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    """Tag model representation in the admin area"""
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
