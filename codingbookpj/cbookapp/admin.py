from django.contrib import admin
from .models import CodeShare, CodeAsk, ShareComment, ShareRe
# Register your models here.
admin.site.register(CodeShare)
admin.site.register(CodeAsk)

admin.site.register(ShareComment)
admin.site.register(ShareRe)