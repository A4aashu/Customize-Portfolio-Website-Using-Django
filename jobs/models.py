from django.db import models


# Create your models here.
class Job(models.Model):
    skill = models.CharField(max_length=20,default='abc')
    percent=models.IntegerField(default=50)

    def __str__(self):
        return self.skill

class Profile (models.Model):
    name = models.CharField(max_length=20,default='Aashu Yadav')
    profilephoto=models.ImageField(upload_to='images/' , blank=True)
    facebook=models.URLField(max_length=200,default='https://www.facebook.com/aashu.yadav.589/' , blank=True)
    insta=models.URLField(max_length=200,default='https://www.instagram.com/a4_aashu/' , blank=True)
    skype=models.URLField(max_length=200,default='https://join.skype.com/invite/UJB1tZr05vWv' , blank=True)
    linkedin=models.URLField(max_length=200,default='https://www.linkedin.com/in/aashu-yadav-9000a1b4/' ,blank=True)
    github=models.URLField(max_length=200,default='https://github.com/A4aashu' ,blank=True)
    hero=models.CharField(max_length=20,default='Aashu Yadav')
    skill1=models.CharField(max_length=20,default='Designer')
    skill2=models.CharField(max_length=20,default='Data scientist',blank=True)
    skill3=models.CharField(max_length=20,default='Free lancer',blank=True)
    skill4=models.CharField(max_length=20,default='Full stack developer',blank=True)
    skill5=models.CharField(max_length=20,default='Cool😎',blank=True)
    backgroundimage = models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.name

class About(models.Model):
    shortintro = models.CharField(max_length=200,default='I am a curious B.tech Computer science undergraduate from KIIT UNIVERSITY, Bhubaneswar. Data Science and Web Development Enthusiast.')
    quality1=models.CharField(max_length=20,default='Web developer')
    quality2=models.CharField(max_length=20,default='Data scientist',blank=True)
    aboutquality=models.CharField(max_length=400,blank=True,default='Data Science is the process of analyzing data using specialized skills and technology whereas Web Development is the creation of a website for the internet or intranet using company details, client requirement, and technical skills.')
    birthday=models.DateField(default='1999-01-21')
    phone=models.CharField(max_length=13,default=('+919996143731'))
    city=models.CharField(max_length=20,default='Narnaul')
    age=models.IntegerField(default='21')
    degree=models.CharField(max_length=20,default='B.Tech')
    email= models.EmailField(max_length=200,default='kdsastm@gmail.com')
    intro=models.CharField(max_length=500,blank=True,default=' I’ve gained some practical knowledge in the field of Computer Programming. Therefore, I am looking for an opportunity where I can utilize my skills, put my learning into practice and make a contribution in the field of Computing and Technology. ')
    aboutphoto=models.ImageField(upload_to='images/',blank=True)
    
    def __str__(self):
        return self.email


class Summary(models.Model):
    resumeintro = models.CharField(max_length=500,default='Optimizing problems by thinking out of the box. A learning enthusiast grasping and observing patterns in day-to-day activities. I am comfortable with a lot of tech languages & frameworks and would love to work in a very dynamic & aspirational environment. Passionate about Competitive programming, Algorithms, Data Science and Web Development. Playing badminton and Cooking being the favorite pastime.',blank=True)
    resumename=models.CharField(max_length=20,default='Aashu Yadav')
    resumeaddress=models.CharField(max_length=50,default='Narnaul,Haryana,India',blank=True)
    resumephone=models.CharField(max_length=13,default=('+919996143731'),blank=True)
    resumeemail= models.EmailField(max_length=200,default='kdsastm@gmail.com',blank=True)
    
    def __str__(self):
        return self.resumename

class Education(models.Model):
    degree = models.CharField(max_length=100,default='Bachelor of Technology')
    field=models.CharField(max_length=100,default='Computer science')
    date=models.CharField(max_length=10,default='2017-2021')
    nameoforg=models.CharField(max_length=100,default=('Kiit University ,Bhubaneswar'))
   
    def __str__(self):
        return self.degree

class Experience(models.Model):
    workas = models.CharField(max_length=100,default='Full stack developer',blank=True)
    date=models.CharField(max_length=100,default='May(2019)-July(2019)',blank=True)
    nameoforg=models.CharField(max_length=100,default=('Tekserve ,Egypt'),blank=True)
    expintro = models.CharField(max_length=500,default='Made an english learning website front end and made app similar to uber eats with help of React Native,Html,Css and Javascript.',blank=True)
   
    def __str__(self):
        return self.workas


class Portfolio(models.Model):
    title = models.CharField(max_length=20,default='Educational website')
    projectphoto=models.ImageField(upload_to='images/' , blank=True)
    projectlink=models.URLField(max_length=200,default='https://a4aashu.github.io/educational-website/' , blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model): 
    phone=models.CharField(max_length=13,default=('+919996143731'))
    location=models.CharField(max_length=100,default='Narnaul,Haryana,India ')
    email= models.EmailField(max_length=100,default='kdsastm@gmail.com')
    maplink=models.URLField(max_length=1000,default='https://maps.google.com/maps?q=narnaul%20haryana&t=&z=13&ie=UTF8&iwloc=&output=embed' , blank=True)
    
    def __str__(self):
        return self.email