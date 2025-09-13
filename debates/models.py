from django.db import models
from io import BytesIO
from django.core.files.base import ContentFile
import qrcode

from ibratdebate.base_model import BaseModel
from users.models import User, Region, District, get_random_id


def create_qr_code(ticket_id: str) -> ContentFile:
    image = qrcode.make(ticket_id)

    buffer = BytesIO()
    image.save(buffer)
    buffer.seek(0)

    return ContentFile(buffer.read(), name=f"{ticket_id}.png")


class Debate(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name="debates")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name="debates")
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.region} - {self.district} ({self.date} {self.time})"


class Ticket(BaseModel):
    id = models.CharField(max_length=40, primary_key=True, default=get_random_id)
    debate = models.ForeignKey(Debate, on_delete=models.SET_NULL, null=True, related_name="tickets")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="tickets")
    qr_code = models.ImageField(upload_to="qr_codes", null=True, blank=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.debate} - {self.user}"

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.qr_code = create_qr_code(str(self.id))
        super(Ticket, self).save(*args, **kwargs)
