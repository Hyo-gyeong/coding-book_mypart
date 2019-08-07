from django.shortcuts import render, redirect, get_object_or_404
from .models import CodeShare, CodeAsk, ShareComment
from .forms import ShareNew, AskNew, ShareCommentForm
from django.utils import timezone
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'index.html')

# share관련 함수

def share(request):

    sharecodes = CodeShare.objects.all()
    if request.method == 'POST':
            search = request.POST.get('search')
            sharecodes = sharecodes.filter(title__contains=search)
    
    return render(request, 'share.html', {'sharecodes':sharecodes})

def search(request):     
    if request.method == 'POST':     
        bds = CodeShare.objects.all()
        b = request.POST.get('search')
        bds = CodeShare.objects.filter(title__contains=b)
        return render(request, 'share.html', {'bds' : bds})
    else:
        return render(request, 'share.html', {})

def sharedetail(request, codeshare_id):

    sharedetail = get_object_or_404(CodeShare, pk = codeshare_id)

    return render(request, 'sharedetail.html', {'sharedetail':sharedetail})

def sharedelete(reqeust, codeshare_id):
    
    sharedetail = get_object_or_404(CodeShare, pk = codeshare_id)
    sharedetail.delete()

    return redirect('share')

def sharenew(request):

    if request.method == 'POST':
    
        share_form = ShareNew(request.POST, request.FILES)
        if share_form.is_valid(): 
            share_post = share_form.save(commit=False)
            share_post.pub_date = timezone.now()
            share_post.save()
        return redirect('share')
            
    else:

        share_form = ShareNew()

        return render(request, 'sharenew.html', {'share_form': share_form})

def shareedit(request, codeshare_id):

    shareedit = get_object_or_404(CodeShare, pk = codeshare_id)

    if request.method == 'POST':
        shareedit.title = request.POST['title']
        shareedit.body = request.POST['body']
        shareedit.codes = request.POST['codes']
        shareedit.subject = request.POST['subject']
        shareedit.university = request.POST['university']
        shareedit.score = request.POST['score']
        shareedit.writer = request.POST['writer']
        shareedit.save()

        return redirect('/share/'+str(shareedit.id))

    else:

        return render(request, 'shareedit.html', {'shareedit':shareedit})


def sharecomment_create(request, codeshare_id):
    
    if request.method == 'POST':
            codeshare = get_object_or_404(CodeShare, pk=codeshare_id)
            shareform = ShareCommentForm(request.POST)

            if shareform.is_valid():
                sharecomment = shareform.save(commit = False)
                sharecomment.codeshare = codeshare
                sharecomment.save()
            return redirect('/share/'+str(codeshare.id))
    else:
            shareform = ShareCommentForm()
            return render(request, 'sharedetail.html', {'shareform' : shareform})

def sharecomment_delete(request, codeshare_id, sharecomment_id):

    codeshare = get_object_or_404(CodeShare, pk=codeshare_id)
    sharecomment = get_object_or_404(ShareComment, pk=sharecomment_id)
    sharecomment.delete()
    
    return redirect('/share/'+str(codeshare.id))





# ask관련 함수

def ask(request):

    askcodes = CodeAsk.objects.all()
    if request.method == 'POST':
            search = request.POST.get('searchAsk')
            askcodes = askcodes.filter(title__contains=search)
    
    return render(request,'ask.html', {'askcodes':askcodes})



def searchAsk(request):     
    if request.method == 'POST':     
        bds = CodeAsk.objects.all()
        b = request.POST.get('searchAsk')
        bds = CodeAsk.objects.filter(title__contains=b)
        return render(request, 'ask.html', {'bds' : bds})
    else:
        return render(request, 'ask.html')



def askdetail(request, codeask_id):
    
    askdetail = get_object_or_404(CodeAsk, pk = codeask_id)

    return render(request, 'askdetail.html', {'askdetail':askdetail})

def askdelete(reqeust, codeask_id):

    askdetail = get_object_or_404(CodeAsk, pk = codeask_id)
    askdetail.delete()

    return redirect('ask')

def asknew(request):

    if request.method == 'POST':
    
        ask_form = AskNew(request.POST, request.FILES)
        if ask_form.is_valid(): 
            ask_post = ask_form.save(commit=False)
            ask_post.pub_date = timezone.now()
            ask_post.save()
        return redirect('ask')
            
    else:

        ask_form = AskNew()

        return render(request, 'asknew.html', {'ask_form': ask_form})

def askedit(request, codeask_id):
    
    askedit = get_object_or_404(CodeAsk, pk = codeask_id)

    if request.method == 'POST':
        askedit.title = request.POST['title']
        askedit.body = request.POST['body']
        askedit.codes = request.POST['codes']
        askedit.subject = request.POST['subject']
        askedit.writer = request.POST['writer']
        askedit.save()

        return redirect('/ask/'+str(askedit.id))

    else:

        return render(request, 'askedit.html', {'askedit':askedit})
