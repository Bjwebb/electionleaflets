from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

admin.autodiscover()

from leaflets.feeds import *

from core.views import home

urlpatterns = patterns(
    '',

    url(r'^$',          home, name='home'),
    url(r'^leaflets',   include('leaflets.urls')),
    url(r'^parties',    include('parties.urls')),
    url(r'^constituencies',    include('constituencies.urls')),
    url(r'^analysis',   include('analysis.urls')),
    url(r'^tags',       include('tags.urls')),
    url(r'^categories', include('categories.urls')),
    url(r'^map/', include('boundaries.urls')),
    url(r'^api', include('api.urls')),

    # Feeds
    url(r'^feeds/latest/$', LatestLeafletsFeed(), name='latest_feed'),
    url(r'^feeds/party/(?P<party_slug>[\w_\-\.]+)/$', PartyFeed(), name='party_feed'),
    url(r'^feeds/attacking/(?P<party_slug>[\w_\-\.]+)/$', AttackingPartyFeed(), name='attacking_party_feed'),
    url(r'^feeds/constituency/(?P<cons_slug>[\w_\-\.]+)/$', ConstituencyFeed(), name='constituency_feed'),
    url(r'^feeds/category/(?P<cat_slug>[\w_\-\.]+)/$', CategoryFeed(), name='category_feed'),
    url(r'^feeds/tag/(?P<tag_slug>[\w_\-\.]+)/$', TagFeed(), name='tag_feed'),

    # Individual urls
    url(r'^about/$', direct_to_template, {'template': 'core/about.html'}, name='about'),
    url(r'^report/(?P<id>\d+)/sent/$', TemplateView.as_view(tempalte='core/report_sent.html'), name='report_abuse_sent'),
    url(r'^report/(?P<id>\d+)/$', 'core.views.report_abuse', name='report_abuse'),

    # Administration URLS
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
