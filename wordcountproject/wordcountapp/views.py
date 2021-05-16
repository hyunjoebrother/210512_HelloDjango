from django.shortcuts import render

# Create your views here.
def home(request) : # home.html을 띄우는 함수
    return render(request, 'home.html')

def about(request) : # about.html을 띄우는 함수
    return render(request, 'about.html')

def result(request) :
    text = request.GET['fulltext'] # 입력한 글 전체 data 받아옴
    words = text.split() # 공백 기준으로 나눠 list로 저장하는 함수

    return render(request, 'result.html', 
    {'full' : text, 'total' : len(words)}
    ) # 세 번째 인자에 딕셔너리형 객체