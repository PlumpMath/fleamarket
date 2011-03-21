from django.conf.urls.defaults import *
#from django.views.generic import list_detail, create_update
from listings.models import Item
import views

info_dict = {
    'queryset': Item.objects.all(),
}

my_listings_dict = {
        # TODO: How to feed in the proper seller id to this query
    'queryset': Item.objects.filter(seller__exact=4),
}

item_info = {
    'model': Item,
}

urlpatterns = patterns('',
    #(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    #(r'^$', 'django.views.generic.list_detail.object_list', my_listings_dict),
    (r'^$', views.list),
    #(r'^new/$', 'django.views.generic.create_update.create_object', item_info),
    #(r'^create/$', views.create),
    (r'^new/$', views.new),

    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),

    # We're naming this 'item_results'
    url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='items/results.html'), 'item_results'),
)
