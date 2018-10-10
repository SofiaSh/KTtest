from login.views import register, index, login, form, edit_form, logout
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'register/$', register, name='register'),
    url(r'login/$', login, name='login'),
    url(r'form/$',form, name='form'),
    url(r'edit/$',edit_form, name='edit'),
    url(r'logout/$',logout, name='logout'),
    url(r'^$', index, name='index'),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
