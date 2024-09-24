from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # 단일 게시글 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return (request, 'articles/new.html')

# 과거 catch
def create(request):
    # 1. 사용자 요청으로부터 입력 데이터를 추출
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 저장 1
    # article = Article()       인스턴스 생성
    # article.title = title     인스턴스 변수에 지정
    # article.content = content
    # article.save()            인스턴스 저장
    
    # 저장 2, 인스턴스 생성할때 변수에 값을 넣어줌
    article = Article(title=title, content=content)
    article.save()
    # 유효성 검사 --> 저장 전에 진행함

    # 저장 3
    # Article.objects.create(title=title, content=content)

    # 2. 추출한 입력 데이터를 활용해 DB에 저장 요청
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    # 삭제 후 이동할 페이지로
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 어떤 게시글 수정할지
    article = Article.objects.get(pk=pk)
    # 사용자로부터 받은 새로운 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 기존 게시글의 데이터를 사용자로부터 받은 데이터로 새로 저장
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article.pk)