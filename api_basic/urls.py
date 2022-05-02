
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
router.register('article', views.GenericArticleViewSet, basename='article')
router.register('modalarticle', views.ModalArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),   
    # path('article/', views.article_list),
    # path('article/', views.ArticleAPIView.as_view()),
    path('article/', views.GenericArticleView.as_view()),
    # path('article/<int:pk>', views.article_detail),
    path('article/<int:id>', views.GenericArticleView.as_view()),

]
