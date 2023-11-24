from django.shortcuts import render
import os

# Create your views here.

def index(request):
    text = ''
    numbers = 0
    if request.method == "GET":
        name = request.GET.get('filename')
        if request.GET.get('load') == "1":
            if name:
                with open(name, 'r') as f:
                    text = f.read()
            with open("E:/temp/log.txt", 'a') as f1:
                f1.write(f'{str(text)} ')

        if request.GET.get('erase') == "2":
            with open("E:/temp/log.txt", 'w') as f1:
                f1.truncate(0)

        fo_find = str(request.GET.get('search'))
        if request.GET.get('find') == "3":
            with open("E:/temp/log.txt", 'r') as f:
                take_text = str(f.read()).split(" ")
                numbers = take_text.count(fo_find)

        with open("E:/temp/log.txt", 'r') as f:
            take_text = f.read()

    return render(request, 'index.html', {'word_list': take_text,
                                          'number': numbers, })
