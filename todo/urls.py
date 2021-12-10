from django.urls import path,include
from . import views

app_name='todo'

urlpatterns = [
    path('', views.home,name="主页"),
    path('about/',views.about,name="关于"),
    path('edit/<i_id>',views.edit,name="编辑"),
    path('delete/<i_id>',views.delete,name="删除"),
    path('cross/<i_id>',views.cross,name="划掉"),
    path('edit_level/<i_id>',views.edit_level,name="优先级"),
    path('details/<i_id>',views.details,name="详细内容"),
]