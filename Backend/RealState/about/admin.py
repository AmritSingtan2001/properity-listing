from django.contrib import admin
from about.models import setting
from django.utils.html import format_html

class settingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'phone_no', 'logo_image','fb_link', 'insta_link', 'linkedIn_link', 'whatsapp_link')
    search_fields = ('site_name', 'phone_no')
    list_filter = ('site_name',)

    def logo_image(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" height="100" />', obj.logo.url)
        return "No Logo"

    logo_image.short_description = ("Logo")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(id=1) if queryset.exists() else queryset

    def has_add_permission(self, request):
        if setting.objects.exists():
            return False  
        return True  

    def has_delete_permission(self, request, obj=None):
        if not setting.objects.exists():
            return False  
        return True

admin.site.register(setting, settingAdmin)
