from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import donor
from school.models import school

def home_page(request):
	return render(request,'donor_home_page.html')


def register_donor(request):
	try:
		donor_name = request.POST["donor_name"]
		pnum = request.POST["phone_number"]
		#school_name = request.POST["school_name"]
	except donor.DoesNotExist:
		return Http404("Error occured")

	d = donor(name=donor_name,phone_number=pnum)
	d.save()

	all_donors = donor.objects.all()
	context = {
		"donors":all_donors,
	}
	return render(request,'donor_list.html',context)