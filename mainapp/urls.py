from  django.conf.urls import url

import mainapp.views as mainapp

app_name='maimapp'

urlpatterns=[
    url('^$', mainapp.products, name='index'),
    url(r'^(?P<pk>\d+)/$', mainapp.products, name='product'),
]