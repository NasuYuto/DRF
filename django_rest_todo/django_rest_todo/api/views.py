from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer

#ModelViewSetとはデータベースモデルに基づいて自動的にCRUD操作を処理するための便利なビューセット
class TodoViewSet(ModelViewSet):
    #データベースから取得するデータのクリアセット
    queryset = Todo.objects.all()
    #Todoモデルのシリアライザを指定
    serializer_class = TodoSerializer