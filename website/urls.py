
from django.contrib import admin
from django.conf.urls import include,url


from django.conf import settings
from django.conf.urls.static import static
#app_name='AiHiring'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^AiHiring/', include('AiHiring.urls')),
    url(r'^AiHiring/index.html/', include('AiHiring.urls')),
    url(r'^AiHiring/examples.html/', include('AiHiring.urls')),
    url(r'^AiHiring/page.html/', include('AiHiring.urls')),
    url(r'^AiHiring/another_page.html/', include('AiHiring.urls')),
    url(r'^AiHiring/contact.html/', include('AiHiring.urls')),
    url(r'^AiHiring/selected.html/', include('AiHiring.urls')),
    url(r'^AiHiring/finalLIST.html/', include('AiHiring.urls')),
    url(r'^AiHiring/PRS1w.pdf/', include('AiHiring.urls')),
    url(r'^AiHiring/firstPage.html/', include('AiHiring.urls')),
    url(r'^AiHiring/signupin.html/', include('AiHiring.urls')),
    url(r'^AiHiring/authenticate.html/', include('AiHiring.urls')),
    url(r'^AiHiring/forget.html/', include('AiHiring.urls')),
    url(r'^AiHiring/otp.html/', include('AiHiring.urls')),
    url(r'^AiHiring/changePSWD.html/', include('AiHiring.urls')),
    url(r'^AiHiring/activate.html', include('AiHiring.urls')),
    url(r'^AiHiring/excel.html', include('AiHiring.urls')),
    
    
    #url(r'^examples/', include('examples.urls')),
    #url(r'^AiHiring/index.html/', include('AiHiring.urls')),
    #url(r'^AiHiring/examples.html/', include('AiHiring.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)