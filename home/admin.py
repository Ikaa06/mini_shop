from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from home.models import products, ProductImage, Reservation
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    property = forms.CharField(label='Характеристики', widget=CKEditorUploadingWidget())

    class Meta:
        model = products
        fields = '__all__'


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


@admin.register(products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('name',)}
    form = ProductAdminForm


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['product_url',
                    'name', 'email', 'phone', 'created', 'updated',
                    'available']
    list_display_links = ['name']
    readonly_fields = ['product_url', ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    fields = [('product',), ('name', 'email', 'phone'), ('available')]

    def product_url(self, obj):
        return mark_safe(
            u'<a href="{0}" target="_blank">{1}</a>'.format(obj.product.get_absolute_url(), obj.product.name))

    product_url.short_description = 'Ссылка на товар'
