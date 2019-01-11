from django.db import models

from datetime import datetime

# Create your models here
# TODO create a model for the gateway
# parameters
#   model
#   serial_number
#   sim_card_id
#   isp_carrier (select from list)
#   ethernet_ip_address
#   wifi_ip_address
#   vpn_ip_address

class Gateway(models.Model):
    # standard fields
    title = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.PositiveIntegerField()
    sim_id = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)

    # complex model field types
    website = models.URLField(blank=True, null=True)
    date_deployed = models.DateField(default=datetime.now, null=True)

    # complex model field types Requiring other models
    # example point to one other object 
    # publisher = models.ForeignKey("Publisher", blank=True, null=True)
    # example select several
    # genre = models.ManyToManyField("Genre", blank=True)

    def __str__(self):
        return self.title


