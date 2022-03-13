from audioop import reverse
from django.db import models
from django.core.validators import FileExtensionValidator
from MyAccount.models import CustomUser

# Create your models here.
class Vidio(models.Model):
    name = models.CharField(max_length=115)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    vidio = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov'])])
    privew = models.FileField(upload_to='media/')
    relateed_to_chenel = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publick = models.BooleanField(default=True)
    watched = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    


