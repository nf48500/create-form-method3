from django.db import models

# Create your models here.
class Product(models.Model):
    x=(
        ('clothes','clothes'),
        ('books','books'),
        ('electronics','electronics')
    )
    name=models.CharField(max_length=100,blank=True,verbose_name='title')
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    active=models.BooleanField(default= True)
    image=models.ImageField(upload_to='products/',null=True,blank=True)
    category=models.CharField(max_length=100,blank=True,null=True,choices=x,help_text='select category')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='nour'
        verbose_name_plural='nourhan'
        ordering=['name']

class test(models.Model) :
    date=models.DateField()
    time=models.TimeField(null=True,blank=True)
    cteated=models.DateTimeField(null=True)

    def __str__(self):
        return str(self.date)
