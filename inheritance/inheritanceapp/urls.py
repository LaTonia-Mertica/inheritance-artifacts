from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# url patterns for the inheritance app
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('ourstory/', views.ourstory, name='ourstory'),
    path('gallery/',views.imagedisplay, name='gallery'), 
    path('gallery/<str:category>',views.imagecategorydisplay, name='gallery-category'), 
    path('addartifact/', views.image_upload_view, name='addartifact'),  
    path('editartifact/<int:id>', views.editartifact, name="editartifact"), 
    path('deleteartifact/<int:id>', views.deleteartifact, name="deleteartifact"),

]

urlpatterns += staticfiles_urlpatterns()


