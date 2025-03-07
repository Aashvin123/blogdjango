from django.urls import  path
from django.http import HttpResponse
from blog import views




urlpatterns = [
    # Function Based View
    # path("", views.blog_list_view, name="home_page"),
    # path("about/", views.about_view,name="about_page"),
    # path("contact/", views.contact_view,name="contact_page"),
    # path("post/<int:pk>/", views.blog_detail_view,name="blog_detail"),

    # Class Based View 
    path("", views.BlogListView.as_view(), name="home_page"),
    path("about/", views.BlogAboutListView.as_view(),name="about_page"),
    path("contact/", views.BlogContactListView.as_view(),name="contact_page"),
    path("create/",views.BlogCreateView.as_view(),name="create_page"),
    path("post/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("post/<int:pk>/edit/", views.BlogUpdateView.as_view(), name="edit_blog"), # edit not write automatically add
    path("post/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="delete_blog"), 
    path("post/<int:pk>/comment",views.CommentCreateView.as_view(),name="create_comment"),

] 
