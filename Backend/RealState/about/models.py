from django.db import models
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

nepali_phone_regex = r"^(\+977|977|9)\d{8,9}$"

def validate_nepali_phone_number(value):
    if not re.match(nepali_phone_regex, value):
        raise ValidationError(
            _("Invalid Nepali phone number. It should start with +977, 977, or 9 followed by 8 to 9 digits."),
            code='invalid_phone_number'
        )

class setting(models.Model):
    site_name = models.CharField(_("site name"), max_length=150)
    phone_no= models.CharField(_("Phone Number(contact no)"), validators=[validate_nepali_phone_number], max_length=50)
    logo = models.ImageField(_("Upload logo"), upload_to='logo/', height_field=None, width_field=None, max_length=None)
    fb_link = models.URLField(_("Facebook Link"), max_length=200, null= True, blank =True) 
    insta_link = models.URLField(_("Instagram Link"), max_length=200, null =True, blank =True)
    linkedIn_link =models.URLField(_("LinkedIn Link"), max_length=200,null =True, blank =True)
    whatsapp_link = models.URLField(_("whatsapp"), max_length=200, null =True, blank =True)

    class Meta:
        verbose_name = _("setting")
        verbose_name_plural = _("settings")

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse("setting_detail", kwargs={"pk": self.pk})


class AboutUs(models.Model):
    title = models.CharField(_("Enter Title"), max_length=150)
    descriptions = RichTextField(_("Enter Descriptions"))
    yt_video_url = models.URLField(_("Enter Youtube video URL"), null=True, blank=True)
    image = models.ImageField(_("Select Image"),upload_to='AboutUs/', null=True, blank=True)

    def clean(self):
        super().clean()
        if not self.yt_video_url and not self.image:
            raise ValidationError(
                _("You must provide at least one of 'Youtube video URL' or 'Image'.")
            )