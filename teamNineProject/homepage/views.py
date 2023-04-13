# from http.client import HTTPResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'index.html', {})

# def coffee_view(request):
#     coffee_all = Coffee.objects.all() # .get(), .filter(), ...
#     # if request="POST"
#     # Form 완성
#     # Form이 유효하면 저장
    
#     if request.method == "POST":
#         form = CoffeeForm(request.POST) # 완성된 Form
#         if form.is_valid(): # 채워진 Form이 유효하다면
#             form.save() # Form을 저장
    
#     form = CoffeeForm()
    
#     return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form": form})