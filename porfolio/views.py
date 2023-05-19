from django.core.checks import messages

from porfolio import form
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from porfolio.models import Slider,Service,Project_Plans,Offer_Ditails,Portfolio_Section,Featureplans,Video,Websitesettings


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['sliders']=Slider.objects.all()
        context['services']=Service.objects.all()
        context['projectplan']=Project_Plans.objects.all()
        context['featureplan']=Featureplans.objects.all()
        context['offerditails']=Offer_Ditails.objects.all()
        context['portfolio']=Portfolio_Section.objects.all()
        context['videos'] = Video.objects.all()
        context['website'] = Websitesettings.objects.first()
        return context


class ContactView(View):
    def post(self,request):
        forms=form.ContactForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Your data has been saved successfull")
        else:
            messages.error(request, "Invalid please try again")

class SubscriberView(View):
    def post(self,request):
        forms=form.SubscriberForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            # messages.Success(request,"Your data has been saved successfull")
        # else:
        #     # messages.error(request,"Invalid please try again")
        return redirect('/')