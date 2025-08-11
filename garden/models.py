from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    """
    Representa um grupo ao qual as plantas pertencem.
    """
    name = models.CharField(max_length=100, verbose_name="Group Name")

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    Categoria para classificar o conteúdo das plantas.
    """
    name = models.CharField(max_length=100, verbose_name="Category Name")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Plant(models.Model):
    """
    Representa uma planta, que pode pertencer a um grupo e ter vários donos.
    """
    name = models.CharField(max_length=200, verbose_name="Plant Name")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='plants')
    image = models.ImageField(upload_to='plants/', blank=True, null=True)
    owners = models.ManyToManyField(User, related_name='plants')  # vários usuários podem ter a mesma planta

    class Meta:
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

    def __str__(self):
        return self.name

class Content(models.Model):
    """
    Conteúdo associado a uma planta, categorizado e com texto/imagem.
    """
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='contents')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='contents')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='contents/', blank=True, null=True)

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return f"{self.plant.name} - {self.category.name}"
