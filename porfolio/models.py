from django.db import models


# Create your models here.
class Slider(models.Model):
    subtitle = models.CharField(max_length=60)
    title = models.CharField(max_length=100)
    bottom_subtitle = models.CharField(max_length=250)
    button_text = models.CharField(max_length=50)
    button_url = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)


class Service(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to='services/')
    desc = models.CharField(max_length=300)


class Project_Plans(models.Model):
    title = models.CharField(max_length=30)
    past_price = models.CharField(max_length=20)
    present_price = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    @property
    def get_featureplans(self):
        return self.Featureplans_set.all()


class Offer_Ditails(models.Model):
    list_item = models.CharField(max_length=20)


class Portfolio_Section(models.Model):
    image = models.ImageField(upload_to='services/')
    hovereffect_title = models.CharField(max_length=20)
    hovereffect_para = models.CharField(max_length=20)


class Feature(models.Model):
    package = models.ForeignKey(Portfolio_Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Featureplans(models.Model):
    packageList = models.ForeignKey(Project_Plans, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Video(models.Model):
    youtube = models.CharField(max_length=150)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    website=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email=models.CharField(max_length=100,unique=True)
    website=models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')

class Websitesettings(models.Model):
    logo =models.ImageField(upload_to='settings/')
    about_title=models.CharField(max_length=100)
    about_desc=models.TextField()
    project_no=models.IntegerField(default=1)
    website_no=models.IntegerField(default=1)
    client_no=models.IntegerField(default=1)
    project_no=models.CharField(max_length=100)
    website_desc=models.CharField(max_length=100)
    about_image=models.ImageField(upload_to='settings/')
    facebook=models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkdein = models.CharField(max_length=100)
    behance = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)


