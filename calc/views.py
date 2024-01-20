from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'I am Navin'})

# def add(request):
#     val1=request.GET['num1']
#     val2 = request.GET['num2']
#     res= val1 +  val2
#     return render(request,'result.html', {'resullt':res})


# from django.shortcuts import render
#
# def add(request):
#     num1 = request.GET.get('num1', 0)
#     num2 = request.GET.get('num2', 0)
#
#     # Perform any processing or calculations here if needed
#
#     context = {'num1': num1, 'num2': num2}
#     return render(request, 'add_template.html', context)


def home(request):
    return render(request, 'home.html', {'name': 'I am Navin'})

def add(request):
    try:
        val1 = int(request.GET['num1'])
        val2 = int(request.GET['num2'])
        result = val1 + val2
    except (KeyError, ValueError):
        # Handle cases where 'num1' or 'num2' are not provided or not valid numbers
        result = "Invalid input"

    return render(request, 'result.html', {'result': result})
