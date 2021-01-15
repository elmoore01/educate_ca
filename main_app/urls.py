from django.urls import include, path
from django.contrib import admin

from . import  views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('forum', views.forum_page, name='forum'),
    path('contact', views.contact_page, name='contact'),
    path('lifeprep', views.lifeprep_page, name='lifeprep'),
    path('partners', views.partners_page, name='partners'),
    path('board', views.board_page, name='board'),
    path('financials', views.financials_page, name='financials'),
    path('donate', views.donate_page, name='donate'),
    path('board/davidfactor/', views.dfactor_page, name='davidfactor'),
    path('board/ericmoore/', views.ericmoore_page, name="'ericmoore"),
    path('board/irwinjaeger/', views.irwinjaeger_page, name="'irwinjaeger"),
    path('board/pamelawiley/', views.pamelawiley_page, name="'pamelawiley"),
    path('board/rayroche/', views.rayroche_page, name="'rayroche"),
    path('board/samonacaldwell/', views.samonacaldwell_page, name="'samonacaldwell"),
]
