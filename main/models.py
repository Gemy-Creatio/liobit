from django.db import models


class ContactRequests(models.Model):
    personName = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, )
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.personName


class CategoryOfBusiness(models.Model):
    Name_ar = models.CharField(max_length=255, null=True, blank=True)
    description_ar = models.TextField(null=True, blank=True)
    Name_en = models.CharField(max_length=255, null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name_ar


class Projects(models.Model):
    Name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True , blank=True)
    category = models.ForeignKey(CategoryOfBusiness, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name
