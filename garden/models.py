from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Content(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.plant.name} - {self.category.name}"
