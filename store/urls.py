from django.urls import path
from . import views
from . import product_utils
from . import contact_us
urlpatterns=[
    path('',views.home_page,name = "home_page"),
    path('store/',views.store,name = "store"),

    path('brands/',views.brands,name = "brands"),
    path('brand-omega/',views.view_omega_brand,name = "omega_brand"),
    path('gucci-omega/',views.view_gucci_brand,name = "gucci_brand"),


    path('cart/',views.cart,name = "cart"),
    path('contact/',views.contactUs,name = "contact"),
    path('checkout/',views.checkout,name = "checkout"),
    path('process_order/',views.processOrder,name = "process_order"),

    path('search_product/',views.searchProduct,name = "searchProduct"),
    path('recommend_product/',product_utils.recommend_product,name = "recommend_product"),

    path('contact_us/',contact_us.contact_us,name = "contact_us"),


]