from django.shortcuts import render, get_object_or_404

from debates.models import Ticket
from users.models import Region, District


def index(request):
    regions = Region.objects.all()
    return render(request, "index.html", {"regions": regions})


def region_view(request, region_id):
    region = get_object_or_404(Region, id=region_id)
    tickets = Ticket.objects.filter(debate__region=region)
    return render(request, "region.html", {"region": region, "tickets": tickets})


def district_view(request, district_id):
    district = get_object_or_404(District, id=district_id)
    tickets = Ticket.objects.filter(debate__district=district)
    return render(request, "district.html", {"district": district, "tickets": tickets})
