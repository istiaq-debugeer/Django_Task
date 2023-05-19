from django.forms import ModelForm

from porfolio.models import Contact,Subscriber

class ContactForm(ModelForm):

    class Meta:
        model=Contact
        fields='__all__'


class SubscriberForm(ModelForm):

    class Meta:
        model=Subscriber
        fields='__all__'