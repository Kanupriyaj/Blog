from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
	
	path('add_post/', views.AddPost.as_view(), name='add_post'),
	path('view_post/', views.ViewPost.as_view(), name='view_post'),
	path('like_post/<int:post_id>', views.LikePost.as_view(), name='like_post'),
	path('comment_post/<int:post_id>', views.CommentPost.as_view(), name='comment_post'),
	
	


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)