from django.urls import path
from .views import *

urlpatterns = [
    # 클래스형 뷰, 함수형 뷰를 path에 사용할 때 모양이 다릅니다.
    # 함수형 뷰 : 뷰 이름만 쓴다.
    # 클래스형 뷰 : 뷰이름.as_view()
    #
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    # pk : Primary Key
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    # 필터 - Custom: int, str, slug, path,
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]