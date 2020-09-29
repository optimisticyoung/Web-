from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from App.models import BlogUser


class BlogUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.query_params.get('token')
            user_id = cache.get(token)
            user = BlogUser.objects.get(pk=user_id)
            return user,user_id
        except Exception as e:
            print(e)
