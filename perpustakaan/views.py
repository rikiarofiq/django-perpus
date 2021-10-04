from django.shortcuts import render
import logging



def index(request):
    return render(request,'penerbit.html')

def buku(request):
    page_title = 'Buku'
    list_of_book = ["Lion King","King Of Narnia","End Of Narnia"]
    context = {
        'page_title':page_title,
        'list_of_book':list_of_book,
    }
    return render(request,'buku.html',context)

def penerbit(request):
    return render(request,'penerbit.html')
