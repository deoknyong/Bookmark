from django.contrib import admin

# Register your models here.
# 관리자 페이지에 모델을 등록하고 커스터마이징
from .models import Bookmark

admin.site.register(Bookmark)