from django.db import models

#models.Modelで単なるクラスではなくモデルとして扱われる。
class Todo(models.Model):
    #CharFieldは文字列を扱うFieldのサブクラス
    title = models.CharField("タスク名",max_length=30)
    
    #現在のインスタンスのtitle属性ちを所得
    def __str__(self):
        return self.title
    