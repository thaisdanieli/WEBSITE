from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('cadastro/', views.register, name="cadastro"),
    path('sac/', views.complaint, name='sac'),
    path('sugestao/', views.suggestion, name='sugestao'),
    path('reclamacao/', views.homepage, name='registrar_reclamacao'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
