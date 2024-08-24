from django.db import models
class categoria(models.Model):

    nombre=models.CharField(max_length=60)
    codigo=models.CharField(max_length=60, null=True, blank=True)
    estado=models.BooleanField(default=True)
    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categoria"
    def _str_(self):
        return self.nombre
# Create your models here.