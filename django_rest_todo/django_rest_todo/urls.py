
from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .api import views
from django.views.generic import RedirectView
from rest_framework import routers

#DefaultRouterクラスのインスタンスを作成
router = DefaultRouter()
#TodoViewSetビューセットをtodosというパスに関連付け、ルーターに登録
router.register(r'todos',views.TodoViewSet)

urlpatterns = [
    #apiで始まるURLに対してrouter.urlsのルーティングを適用する
    path(r'api/', include(router.urls)),
    path(r'',RedirectView.as_view(url='/static/index.html')),
]
