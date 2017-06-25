from django.conf.urls import url
from . import views
app_name = 'todolist'
urlpatterns = [

    # Index Url
    url(r'^$', views.index, name='index'),

]