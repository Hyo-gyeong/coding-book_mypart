from django.db import models
from datetime import datetime

# Create your models here.

class CodeShare(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'shareimage/', blank = True, null = True)
    body = models.TextField()
    codes = models.TextField(default='코드 없음')
    pub_date = models.DateTimeField(default=datetime.now,blank=True)    
    subject = models.CharField(max_length=50) 
    university = models.CharField(max_length=50,default='없음') #대학교는 옵션이기때문에
    score = models.CharField(max_length=50,default='없음')
    writer = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def sum(self):
        return self.body[:100]

    def codesum(self):
        return self.codes[:50]

class ShareComment(models.Model):
    post = models.ForeignKey(CodeShare, on_delete = models.CASCADE, null=True, related_name='sharecomments')
    sharecontents = models.CharField(max_length = 200)

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.sharecontents

class ShareRe(models.Model):
    comment = models.ForeignKey(ShareComment, on_delete = models.CASCADE, null=True, related_name='sharereplies')
    resharecontents = models.CharField(max_length = 200)

    def __str__(self):
        return self.resharecontents



class CodeAsk(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'askimage/', blank = True, null = True)
    body = models.TextField()
    codes = models.TextField(default='코드 없음')
    pub_date = models.DateTimeField(default=datetime.now,blank=True)    
    subject = models.CharField(max_length=50)
    #질문게시판은 학교에 상관없이 누구나 글을 쓸 수 있는 열린공간이기때문에 학교를 없앰.
    writer = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def sum(self):
        return self.body[:100]

    def codesum(self):
        return self.codes[:50]
