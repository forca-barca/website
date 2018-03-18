from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#app_name="AiHiring"
urlpatterns = [
    url(r'^$', views.hi, name='hi'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^examples.html$', views.examples, name='examples'),
    url(r'^page.html$', views.page, name='page'),
    url(r'^another_page.html$', views.another_page, name='another_page'),
    url(r'^contact.html$', views.contact, name='contact'),
    url(r'^selected.html$', views.selected, name='selected'),
    url(r'^finalLIST.html$', views.fL, name='fLs'),
    url(r'^firstPage.html$', views.firstPage, name='firstPage'),
    url(r'^signupin.html$', views.signupin, name='signupin'),
    url(r'^authenticate.html$', views.auth, name='auth'),
    url(r'^forget.html$', views.forget, name='forget'),
    url(r'^otp.html$', views.otp, name='otp'),
    url(r'^changePSWD.html$', views.changePSWD, name='changePSWD'),
    url(r'^excel.html', views.excel, name='excel'),
    
    #url(r'^', include('AiHiring.urls')),
    #url(r'^account/', include('social_django.urls', namespace='social')),
    #url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),
    #url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^examples.html/examples.html', views.examples, name='examlpes'),
    #url(r'^examples.html/index.html', views.index, name='index'),
]