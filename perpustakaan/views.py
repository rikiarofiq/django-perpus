from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku



def index(request):
    return render(request,'penerbit.html')

def buku(request):
    page_title = 'Buku'
    books = Buku.objects.filter(kategori__nama='PHP')[:1]
    context = {
        'page_title':page_title,
        'books':books,
    }
    return render(request,'buku.html',context)

def penerbit(request):
    return render(request,'penerbit.html')

def tambah_buku(request):
    page_title = 'Tambah Buku'

    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            message = 'Data Berhasil Disimpan'
            context = {
                'page_title': page_title,
                'form': form,
                'message': message,
            }
            return render(request, 'tambah-buku.html', context)

    else:
        form = FormBuku()
        context = {
            'page_title':page_title,
            'form':form,
        }
    return render(request,'tambah-buku.html',context)


