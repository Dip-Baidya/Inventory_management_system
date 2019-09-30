from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('laptop', views.display_laptop, name="Display-laptop"),
    path('desktop', views.display_desktop, name="Display-desktop"),
    path('mobile', views.display_mobile, name="Display-mobile"),

    path('add_laptop', views.add_laptop, name="Add-laptop"),
    path('add_desktop', views.add_desktop, name="Add-desktop"),
    path('add_mobile', views.add_mobile, name="Add-mobile"),

    path('edit_laptop/<int:pk>', views.edit_laptop, name="Edit-laptop"),
    path('edit_desktop/<int:pk>', views.edit_desktop, name="Edit-desktop"),
    path('edit_mobile/<int:pk>', views.edit_mobile, name="Edit-mobile"),

    path('delete_laptop/<int:pk>', views.delete_laptop, name="Delete-laptop"),
    path('delete_desktop/<int:pk>', views.delete_desktop, name="Delete-desktop"),
    path('delete_mobile/<int:pk>', views.delete_mobile, name="Delete-mobile"),

]
