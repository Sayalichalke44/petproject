 
from django.urls import path
from petapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.home),
     path('register',views.register),
     path('login',views.userLogin),
     path('aboutus',views.aboutUs),
     path('contactus',views.contactUs),
     path('details/<int:petid>',views.petDetails),
     path('logout',views.userLogout),
     path('search/<str:searchBy>',views.searchByCategory),
     path('searchbyrange',views.searchByRange),
     path('sort/<int:dir>',views.sortPetsByPrice),
     path('addtocart/<int:petid>',views.addToCart),
     path('mycart',views.showMyCart),
     path('removecart/<int:cartid>',views.removeCart),
     path('updatecount/<int:cartid>/<str:oprn>',views.updateQuantity),
     path('confirmorder',views.confirmOrder),
     path('profile',views.addProfile),
     path('makepayment',views.makePayment),
     path('placeorder/<str:ordid>',views.placeOrder),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)