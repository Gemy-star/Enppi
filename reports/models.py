from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=255, blank=True)
    employee_number = models.CharField(max_length=255)

    class Meta:
        abstract = True


class ITStaff(Info):
    phone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Rating(Info):
    RATING_VALUE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]
    itstaff = models.ForeignKey(ITStaff, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=True, null=True)
    rating = models.CharField(max_length=50, choices=RATING_VALUE)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
