from django.db import models


class Car(models.Model):
    Make_Name = models.CharField(max_length=100)
    Model_Name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Make_Name} {self.Model_Name}'


class Rating(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    car_id = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'Rating for {self.car} is: {self.rating}'
