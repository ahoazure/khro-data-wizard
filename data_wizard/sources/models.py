from django.db import models
from regions.models import StgLocation

class FileSource(models.Model): #added location lookup for location here but may need to chnage
    location = models.ForeignKey(StgLocation, models.PROTECT,
		verbose_name = 'Location',default=1,)
    name = models.CharField(max_length=255, null=True, 
		blank=True,verbose_name = 'File Name',)
    file = models.FileField(upload_to='datawizard/',
		verbose_name = 'Attach File',)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or self.file.name


class URLSource(models.Model):
    location = models.ForeignKey(StgLocation, models.PROTECT,
		verbose_name = 'Location',default=1,)
    name = models.CharField(max_length=255, null=True, 
		blank=True,verbose_name = 'Link Name',)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or self.url
