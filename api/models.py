from django.db import models

# Create your models here.


class MessBill(models.Model):

    newBillAmount = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    uniqueId = models.TextField(blank=False, null=False)

    def __str__(self):
        return str(self.created_on)


class RoomType(models.Model):

    spaceFor = models.TextField(null=True, blank=True)
    occupiedBy = models.TextField(null=True, blank=True)
    rentCost = models.TextField(null=True, blank=True)

    def __str__(self):
        return "size=" + str(self.spaceFor) + "Occupied By" + str(self.occupiedBy)


class Hosteler(models.Model):
    hosteler = models.CharField(max_length=100)
    fee = models.BooleanField(null=True, blank=True)
    room_number = models.CharField(max_length=5)
    uniqueId = models.TextField(null=False, blank=False)
    mess_bill = models.ForeignKey(MessBill, on_delete=models.CASCADE)
    messBillPaid = models.BooleanField(null=True, blank=True)
    roomType = models.ForeignKey(RoomType, null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uniqueId']

    def __str__(self):
        return str(self.hosteler) + str(self.uniqueId)
