from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _




class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = _('blog')





