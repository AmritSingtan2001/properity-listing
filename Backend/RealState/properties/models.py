from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class AutoSlugField(models.SlugField):
    """
    Custom SlugField that generates a slug based on a specific field.
    """
    def __init__(self, *args, source_field='', **kwargs):
        self.source_field = source_field  # field to use for slug generation
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        """
        This method is called before the model is saved.
        It will generate a slug from the specified source_field.
        """
        value = getattr(model_instance, self.source_field, None)
        if value:
            return slugify(value)
        return super().pre_save(model_instance, add)


class Category(models.Model):
    category_name = models.CharField(_("Enter Category Name"), max_length=150)
    slug = AutoSlugField(unique=True, blank=True, editable=False, source_field='category_name')  
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
        

RENT = 'Rent'
BUY = 'Buy'
STATUS_CHOICES = [
    (RENT, _('Rent')),
    (BUY, _('Buy')),
]


SOUTH = 'South'
EAST = 'East'
WEST = 'West'
NORTH = 'North'

DIRECTION_CHOICES = [
    (SOUTH, _('South')),
    (EAST, _('East')),
    (WEST, _('West')),
    (NORTH, _('North')),
]

class Property(models.Model):
    title = models.CharField(_("Enter property title"), max_length=150)
    category = models.ForeignKey('Category', verbose_name=_("Choose Category"), on_delete=models.DO_NOTHING)
    address = models.CharField(_("Enter Address"), max_length=50)
    old_price = models.DecimalField(_("Enter old price"), null=True, blank=True, decimal_places=2, max_digits=20)
    new_price = models.DecimalField(_("Current price"), decimal_places=2, max_digits=20)
    description = RichTextField(_("Enter Descriptions"))
    yt_link = models.URLField(_("Youtube link"),null=True, blank=True, max_length=200)
    per_aana_price = models.DecimalField(_("Per aana price"), null=True, blank=True, decimal_places=2, max_digits=20)
    plot_size = models.CharField(_("Plot size"),null=True, blank=True, max_length=50)
    total_aana = models.CharField(_("Total aana"), max_length=150, null=True, blank=True)
    road_size = models.CharField(_("Road size"), max_length=150, null=True, blank=True)
    road_type = models.CharField(_("Road Type"), max_length=150, null=True, blank=True)
    land_area = models.CharField(_("Land Area"), max_length=150, null=True, blank=True)
    property_face_direction = models.CharField(_("Choose Property Face Direction"), choices=DIRECTION_CHOICES,  max_length=150, null=True, blank=True)
    google_map_url = models.URLField(_("Enter Google map url"),null=True, blank=True, max_length=200)
    status = models.CharField(
        _("Choose Property status"),
        choices=STATUS_CHOICES,
        default=BUY,
        max_length=50
    )
    slug = AutoSlugField(unique=True, blank=True, editable=False, source_field='title')  
    is_highlight = models.BooleanField(_("Is Highlight"), default=False)
    is_featured = models.BooleanField(_("Is Featured"), default=False)
    
    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Property_detail", kwargs={"slug": self.slug})

class PropertyImages(models.Model):
    property = models.ForeignKey("Property", verbose_name=_("Choose Property"), related_name='property_images' ,on_delete=models.CASCADE)
    image = models.ImageField(_("Choose Image"), upload_to='property/images', max_length=255) 
    class Meta:
        verbose_name = _("PropertiesImages")
        verbose_name_plural = _("PropertiesImagess")

    def __str__(self):
        return self.property.title

    def get_absolute_url(self):
        return reverse("PropertyImages_detail", kwargs={"pk": self.pk})
