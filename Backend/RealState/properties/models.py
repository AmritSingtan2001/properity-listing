from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

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
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
