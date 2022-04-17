from django.shortcuts import render, redirect
from django.http import HttpResponse
from categories.models import Category, SubCategory
from . models import UserPost, PostLike, PostComment
from django.views import View
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.decorators import login_required
from . forms import PostModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from django.utils.timesince import timesince
from collections import defaultdict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count
from .serializers import PostSerializer


class AddPost(View):
    
    def get_alertnum(user):
        return Alert.objects.filter(read=False, for_user=user).count()

    #@login_required
    def get(self, request):

        form = PostModelForm()
        category_objs = Category.objects.all()
        context = {'category_objs':category_objs, 'form' : form}
        return render(request, 'post/add_post.html', context)
    
    
    #@login_required(login_url='/accounts/login/')
    def post(self, request):
        #import pdb;pdb.set_trace()
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            # my_image = new.cleaned_data['image']
            category = request.POST.get('category_id')
            category_obj = Category.objects.get(id=category)
            # title = new.cleaned_data['title']
            # description = new.cleaned_data['description']
            # location = new.cleaned_data['location']
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.category = category_obj
            new_post.save()
            return redirect('users:index')
        
        category_objs = Category.objects.all()
        context = {'category_objs':category_objs, 'form' : form}
        return render(request, 'post/add_post.html', context)
        
            #new_post = UserPost.objects.create(user=request.user, category = category_obj, image=my_image, title=title,description=description, location=location)
        
         

       
class ViewPost(View):
    def get(self, request):
        if request.user.is_authenticated:
            post_objs = UserPost.objects.all().annotate(likes_count=Count('postlike')).prefetch_related('postcomment_set').order_by('-created')
            #import pdb;pdb.set_trace()
            #comment_objs = PostComment.objects.select_related('post').all().order_by()
            #now = datetime.now()
            #post_objs.postlike_set.all().count()
            # context = defaultdict(list)
            # for obj in post_objs:
            #     difference = now - post_objs.created
            #     context['since_time'].append(difference)

            

            # since_time =  '%(time)s ago' % {'time': timesince(value).split(', ')[0]}
            context = {'post_objs':post_objs}
            return render(request, 'post/view_post.html', context)
        else:
            return redirect('post:view_post')

class LikePost(View):
    def get(self, request,*args,**kwargs):
        #import pdb;pdb.set_trace()
        if request.user.is_authenticated:
            #import pdb;pdb.set_trace()
            
            #obj = PostLike.objects.filter(user=request.user)
            #if obj.user_id == True:
            #obj.delete()
            user = request.user
            p_id = kwargs['post_id']
            post = UserPost.objects.get(id=p_id)
            like = PostLike.objects.create(user=user,post=post)
            
        return redirect('post:view_post')
      
class CommentPost(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CommentPost, self).dispatch(request, *args, **kwargs)

    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            p_id = kwargs['post_id']
            obj = UserPost.objects.get(id=p_id)
            return render(request, 'post/comment_post.html', {'obj':obj})
    
    def post(self, request, *args,**kwargs):
        #import pdb;pdb.set_trace()
        if request.user.is_authenticated:
            user = request.user
            p_id = kwargs['post_id']
            post = UserPost.objects.get(id=p_id)
            text = request.POST.get('comment')
            comment = PostComment.objects.create(user=user, post=post, text=text)
            
        return redirect('post:view_post')
    
    