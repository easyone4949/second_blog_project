from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
#어떤 데이터가 어떻게 처리될지 함수로 정의한 후 템플릿으로 출력
from .models import Blog
from .models import Portpolio
from .forms import BlogPost
def home(request):
    blogs = Blog.objects
    #모델로부터 객체 목록을 전달받을수 있음(.object)
    #그 객체 목록을 Query set이라함.
    #기능들을 표시해주는 방법을 method라고함. 

    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개을 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해 준다. 
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

    #쿼리셋과 메소드의 형식
    #모델이름.쿼리셋(objects).메소드


def detail(request, blog_id):
    blog_detail =  get_object_or_404(Blog, pk= blog_id)
    #첫번째 인자는 클래스
    #get_object_or_404는 object를 갖고와 주기도 하고(get_object) 예외처리(or_404)도 해주는 역할
    
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))
    #URL은 문자열 형식이기 때문에 문자열로 형변환시킨거임
    #여기 있는거 다 처리한 다음에 이 URL로 넘기세요~

def portpolio(request):
    portpolios = Portpolio.objects
    return render(request, 'portpolio.html', {'portpolios': portpolios})


def blogpost(request):
         
    # 1.입력도니 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.title
            post.body
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form': form})