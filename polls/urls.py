from django.conf.urls import url
from . import views
app_name = 'polls'
urlpatterns = [

    # Index Url
    url(r'^$', views.index, name='index'),

    # Details of question
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # results of question
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # vote for question
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    #testUrl
    url(r'^test/(?P<testId>[0-9]+)/$', views.testView, name='test'),
]