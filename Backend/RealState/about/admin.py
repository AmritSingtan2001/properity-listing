from django.contrib import admin
from about.models import setting, AboutUs
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

from urllib.parse import urlparse, parse_qs

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'about_media', 'yt_video_url')
    search_fields = ('title',)
    list_filter = ('title',)

    def about_media(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        elif obj.yt_video_url:
            video_id = self.extract_youtube_id(obj.yt_video_url)
            if video_id:
                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
                return format_html('<img src="{}" width="100" height="100" />', thumbnail_url)
            return "Invalid YouTube URL"
        return "No Media"

    def extract_youtube_id(self, yt_url):
        try:
            parsed_url = urlparse(yt_url)
            if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
                return parse_qs(parsed_url.query).get("v", [None])[0]
            elif parsed_url.hostname in ("youtu.be",):
                return parsed_url.path.lstrip("/")
        except Exception:
            return None

    about_media.short_description = "Media"

# Register the model admin
admin.site.register(AboutUs, AboutUsAdmin)