from django.contrib import admin
from django.urls import path
import cbookapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cbookapp.views.index, name="index"),

    # share crud
    path('share', cbookapp.views.share, name="share"),
    path('share', cbookapp.views.search, name='search'),
    path('sharenew', cbookapp.views.sharenew, name="sharenew"),
    path('share/<int:codeshare_id>', cbookapp.views.sharedetail, name="sharedetail"),
    path('share/delete/<int:codeshare_id>', cbookapp.views.sharedelete, name="sharedelete"),
    path('share/edit/<int:codeshare_id>', cbookapp.views.shareedit, name="shareedit"),
    
    # share comments
    path('share/<int:codeshare_id>/create', cbookapp.views.sharecomment_create, name="sharecomment_create"),
    path('share/<int:codeshare_id>/comment/<int:sharecomment_id>/delete', cbookapp.views.sharecomment_delete, name="sharecomment_delete"),
    #path('<int:codeshare_id>/comment/<int:sharecomment_id>/sharereply_create', cbookapp.views.sharereply_create, name="sharereply_create"),
    #path('<int:codeshare_id>/comment/<int:sharecomment_id>/delete/<int:sharere_id>/sharereply_delete', cbookapp.views.sharereply_delete, name="sharereply_delete"),

    # ask crud
    path('ask', cbookapp.views.ask, name="ask"),
    path('ask', cbookapp.views.searchAsk, name='searchAsk'),
    path('asknew', cbookapp.views.asknew, name="asknew"),
    path('ask/<int:codeask_id>', cbookapp.views.askdetail, name="askdetail"),
    path('ask/delete/<int:codeask_id>', cbookapp.views.askdelete, name="askdelete"),
    path('ask/edit/<int:codeask_id>', cbookapp.views.askedit, name="askedit"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
