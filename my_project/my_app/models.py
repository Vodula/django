from django.db import models

class CarMake(models.Model):
     name=models.CharField(max_length=100)

     def __str__(self):
         return self.name

class Car(models.Model):
    model_name=models.CharField(max_length=100)
    year=models.IntegerField(max)
    make_name=models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return f"model - {self.model_name} year - {self.year} make_name - {self.make_name}"
