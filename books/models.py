from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category , on_delete=models.PROTECT, null=True)
    name = models.CharField(verbose_name= "Kitob oti", editable=True,
                             help_text="Kitob nomini yozing",  max_length=55)
    author = models.CharField(max_length=55)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    add_date = models.DateField(auto_now_add=True)
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)
    # views = models.BigIntegerField(default=0)
    
    # status = models.BooleanField()
    # models.EmailField()
    # models.PositiveBigIntegerField()
    # models.OneToOneField(Category)
    # models.ManyToManyField(Category)
    # models.DateTimeField()
    # models.URLField()
    # models.FileField(upload_to="files")

   

    def __str__(self) -> str:
        return self.name


class TgAdmin(models.Model):
    tg_id = models.BigIntegerField()
    name = models.CharField(max_length=15)

    