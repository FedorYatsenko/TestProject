from django.db import models
from django.urls import reverse

class User(models.Model):

    name = models.CharField(max_length=200, help_text="Enter your name")
    email = models.EmailField()

    def display_buys(self):
        count = 0
        for buy in Buys.objects.all():
            if buy.user.id == self.id:
                count += 1

        return str(count)

    display_buys.short_description = 'Buys count'

    def display_totalamount(self):
        ta = 0
        for buy in Buys.objects.all():
            if buy.user.id == self.id:
                ta += buy.amount

        return str(ta)

    display_totalamount.short_description = 'Total amount'

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    class Meta:
        ordering = ['name']

class Buys(models.Model):

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.name + " " + str(self.amount)

    class Meta:
        ordering = ['id']