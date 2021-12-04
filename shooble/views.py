from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Following, Post, LikedPost, ProfilePic
from .forms import UserForm, ProfilePicForm


@login_required(login_url='login')
def index(request):
    users_being_followed = Following.objects.filter(userFollower=request.user)
    text_posts = []
    list_of_like_data = []
    ordered_text_posts = Post.objects.order_by('created_at')
    counter = 0
    for i in ordered_text_posts:
        for j in users_being_followed:
            if i.author.id == j.userID_following:
                list_of_like_data.append(
                    i.likedpost_set.filter(user_liking=request.user, post=i).get().is_liked_by_user)
                text_posts.append(i)
                counter += 1
    text_posts.reverse()
    list_of_like_data.reverse()
    print(list_of_like_data)
    context = {
        'text_posts': text_posts,
        'list_of_like_data': list_of_like_data
    }
    return render(request, "shooble/index.html", context)


@login_required(login_url='login')
def create_text_post(request):
    if request.method == 'POST':
        text_post = request.POST.get('textPost')
        new_post = Post.objects.create(textBody=text_post, author=request.user)
        list_of_users = User.objects.all()
        for i in list_of_users:
            print(i)
            liked_post_object = LikedPost.objects.create(user_liking=i, post=new_post, is_liked_by_user=False)
            print(liked_post_object)
    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'shooble/login.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form_name_email = UserForm(request.POST)
        if form.is_valid() and form_name_email.is_valid():
            form.save()
            user = User.objects.get(username=request.POST.get('username'))
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
            ProfilePic.objects.create(user=user, profile_pic='/images/defaultProfilePic.jpeg')
            list_of_text_posts = Post.objects.all()
            for i in list_of_text_posts:
                LikedPost.objects.create(user_liking=user, post=i, is_liked_by_user=False)
            return redirect('index')
    else:
        form = UserCreationForm()
        form_name_email = UserForm()
    context = {
        'form': form,
        'form_name_email': form_name_email
    }
    return render(request, 'shooble/register.html', context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def search_shooble(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        users_searched = User.objects.filter(username__contains=search_query).exclude(username=request.user.username)
        users_being_followed = Following.objects.filter(userFollower=request.user)
        list_of_ids_being_followed = []
        for i in list(users_being_followed):
            list_of_ids_being_followed.append(int(i.userID_following))
        print(list_of_ids_being_followed)
        if users_searched:
            context = {
                'user_searched': users_searched,
                'list_of_ids_being_followed': list_of_ids_being_followed,
                'search_query': search_query
            }
        else:
            context = {
                'no_users': "There are no users for search query \"" + search_query + "\"",
                'search_query': search_query
            }
        return render(request, 'shooble/search.html', context)
    return render(request, 'shooble/search.html')


@login_required(login_url='login')
def profile_view(request, username):
    searched_user = User.objects.get(username=username)
    list_of_following = Following.objects.filter(userFollower=searched_user)  # Who the profile user follows
    list_of_followers = Following.objects.filter(userID_following=searched_user.id)  # Who is following the profile
    print(list_of_following)
    print(list_of_followers)
    ordered_text_posts = Post.objects.filter(author=searched_user).order_by('created_at')
    ordered_like_data = LikedPost.objects.order_by('post__created_at').filter(user_liking=request.user,
                                                                              post__author=searched_user)
    profile_pic = ProfilePic.objects.get(user=searched_user)
    users_being_followed = Following.objects.filter(userFollower=request.user)
    list_of_ids_being_followed = []
    for i in list(users_being_followed):
        list_of_ids_being_followed.append(int(i.userID_following))
    text_posts = []
    list_of_like_data = []
    counter = 0
    for i in ordered_text_posts:
        text_posts.append(i)
        list_of_like_data.append(i.likedpost_set.filter(user_liking=request.user, post=i).get().is_liked_by_user)
        counter += 1
    text_posts.reverse()
    list_of_like_data.reverse()
    context = {
        'user_profile': searched_user,
        'text_posts': text_posts,
        'followers': list_of_followers,
        'following': list_of_following,
        'list_of_like_data': list_of_like_data,
        'list_of_ids_being_followed': list_of_ids_being_followed,
        'profile_pic_url': profile_pic.profile_pic.url
    }
    print(text_posts)
    print(list_of_like_data)
    print(ordered_like_data)
    return render(request, 'shooble/profile.html', context)


@login_required(login_url='login')
def follow_user(request, username):
    user_to_follow = User.objects.get(username=username)
    userID_to_follow = user_to_follow.id
    if not Following.objects.filter(userFollower=request.user, userID_following=userID_to_follow):
        print("New follow")
        Following.objects.create(userFollower=request.user, userID_following=userID_to_follow)
    context = {
        'user_profile': user_to_follow
    }
    return redirect(request.META.get('HTTP_REFERER'), context)


@login_required(login_url='login')
def unfollow_user(request, username):
    user_to_unfollow = User.objects.get(username=username)
    userID_to_unfollow = user_to_unfollow.id
    unfollow = Following.objects.get(userFollower=request.user, userID_following=userID_to_unfollow)
    if unfollow:
        unfollow.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def settings_view(request):
    print("reached the settings view")
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
            return redirect('settings')
    form = UserForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'shooble/settings.html', context)


@login_required(login_url='login')
def like_post(request, postID):
    if request.is_ajax():
        print("ajax request received")
        post_being_liked = Post.objects.get(id=postID)
        liked_post_object = LikedPost.objects.get(user_liking=request.user, post=post_being_liked)
        if not liked_post_object.is_liked_by_user:
            post_being_liked.numberOfLikes += 1
            liked_post_object.is_liked_by_user = True
            post_being_liked.save()
            liked_post_object.save()
            print(post_being_liked)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            post_being_liked.numberOfLikes -= 1
            liked_post_object.is_liked_by_user = False
            post_being_liked.save()
            liked_post_object.save()
            print(post_being_liked)
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def upload_profile_pic(request):
    """Process images uploaded by users"""

    if request.method == 'POST':
        image_form = ProfilePicForm(request.POST, request.FILES)
        form = UserForm(instance=request.user)
        print("made it past the image form")
        if image_form.is_valid():
            image_form.save()
            old_image = ProfilePic.objects.get(user=request.user)
            old_image.delete()
            img_obj = image_form.instance
            img_obj.user = request.user
            img_obj.save()
            print(img_obj)
            context = {
                'image_form': image_form,
                'form': form,
                'img_obj': img_obj
            }
            return render(request, 'shooble/settings.html', context)
    else:
        image_form = ProfilePicForm()
        form = UserForm(instance=request.user)
    return render(request, 'shooble/settings.html', {'image_form': image_form, 'form:': form})


@login_required(login_url='login')
def delete_post(request, postID):
    post_to_delete = Post.objects.get(id=postID)
    if post_to_delete.author_id == request.user.id:
        if request.method == "POST":
            post_to_delete.delete()
            return redirect('/profile/' + request.user.username)
        context = {
            'text_post': post_to_delete,
            'user_profile': request.user
        }
        return render(request, 'shooble/delete.html', context)


def create_bio(request):
    # if request.method == 'POST':
    #     bio = request.POST.get('textPost')
    #     new_post = Post.objects.create(textBody=text_post, author=request.user)
    #     list_of_users = User.objects.all()
    #     for i in list_of_users:
    #         print(i)
    #         liked_post_object = LikedPost.objects.create(user_liking=i, post=new_post, is_liked_by_user=False)
    #         print(liked_post_object)
    return None
