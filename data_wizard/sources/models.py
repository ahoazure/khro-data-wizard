from django.db import models
from khro_app.authentication.models import CustomUser

class FileSource(models.Model): #added location lookup for location here but may need to chnage
    user = models.ForeignKey(CustomUser, models.PROTECT,blank=False,
		verbose_name = 'User Name (Email)',default=4)
    name = models.CharField(max_length=255, null=True,
		blank=True,verbose_name = 'File Name',)
    file = models.FileField(upload_to='datawizard/',
		verbose_name = 'Source File',)
    date = models.DateTimeField(auto_now_add=True,verbose_name='Import Date',)

    def __str__(self):
        return self.name or self.file.name


class URLSource(models.Model):
    user = models.ForeignKey(CustomUser, models.PROTECT,blank=False,
		verbose_name = 'User Name (Email)',default=4)
    name = models.CharField(max_length=255, null=True,blank=True,
        verbose_name = 'URL Name',)
    url = models.URLField(null=False,blank=False,verbose_name='Source Address',)
    date = models.DateTimeField(auto_now_add=True,verbose_name='Import Date',)

    def __str__(self):
        return self.name or self.url

