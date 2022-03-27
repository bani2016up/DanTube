import datetime
from email.generator import Generator
from pathlib import Path
from re import A
from typing import IO, Generator
from urllib import response
from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Vidio, Chapter

# Create your views here.
def redirect_home(request):
    return redirect('vidio/')

def vidio_page(request):
    vidio = Vidio.objects.order_by('date').filter(publick=True)
    topik = Chapter.objects.all().exclude(id=7)
    if request.user.is_authenticated:
        user = request.user
        age = user.age()
        if age < 18:
            vidio = vidio.filter(content_is_only_18_plus=False)
    else:
        vidio = vidio.filter(content_is_only_18_plus=False)



    data = { 'vidio': vidio,
            'topik': topik}
    return render(request, 'main/vidio.html', data)

def vidio_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        vidio = Vidio.objects.filter(name__contains=searched)
        topik = Chapter.objects.all().exclude(id=7)
        context={
            'searched': searched,
            'vidio': vidio,
            'topik': topik
                 }
        return render(request, "main/vidio.html", context )# render
    else:
        context={}
        return render(request, "main/vidio.html", context )# render

def watch_vidio(request, pk):
    vidio = get_object_or_404(Vidio, pk=pk)
    topik = Chapter.objects.all().exclude(id=7)
    vidios = Vidio.objects.all().filter(publick=True)
    data = {
        'vidio': vidio,
        'vidios': vidios,
        'topik': topik
    }
    return render(request, 'main/watch_vidio.html', data)

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response
    
def ranged(
        file: IO[bytes],
        start: int = 0,
        end: int = None,
        block_size: int = 8192,
) -> Generator[bytes, None, None]:
    consumed = 0

    file.seek(start)
    while True:
        data_length = min(block_size, end - start - consumed) if end else block_size
        if data_length <= 0:
            break
        data = file.read(data_length)
        if not data:
            break
        consumed += data_length
        yield data

    if hasattr(file, 'close'):
        file.close()
    
def open_file(request, vidio_pk: int) -> tuple:
    _video = get_object_or_404(Vidio, pk=vidio_pk)

    path = Path(_video.vidio.path)

    file = path.open('rb')
    file_size = path.stat().st_size

    content_length = file_size
    status_code = 200
    content_range = request.headers.get('range')

    if content_range is not None:
        content_ranges = content_range.strip().lower().split('=')[-1]
        range_start, range_end, *_ = map(str.strip, (content_ranges + '-').split('-'))
        range_start = max(0, int(range_start)) if range_start else 0
        range_end = min(file_size - 1, int(range_end)) if range_end else file_size - 1
        content_length = (range_end - range_start) + 1
        file = ranged(file, start=range_start, end=range_end + 1)
        status_code = 206
        content_range = f'bytes {range_start}-{range_end}/{file_size}'

    return file, status_code, content_length, content_range
    
    
    
def chapter(request, Chapter_slug):
    chapter = get_object_or_404(Chapter, slug=Chapter_slug)
    topik = Chapter.objects.all().exclude(id=7)
    vidio = Vidio.objects.order_by('date').filter(publick=True)
    if request.user.is_authenticated:
        user = request.user
        age = user.age()
        if age < 18:
            vidio = vidio.filter(content_is_only_18_plus=False)
            if chapter.id == 4: 
                vidio =vidio.filter(content_is_only_18_plus=False)
            else:
                vidio = vidio.filter(topik=chapter.id)
        else:
            if chapter.id == 4:
                vidio = vidio
            else:
                vidio = vidio.filter(topik=chapter.id)
            
    else:
        vidio = vidio.filter(content_is_only_18_plus=False)
        if chapter.id == 4: 
            vidio = vidio
        else:
            vidio = vidio.filter(topik=chapter.id)
            
    data = {
        'chapter': chapter,
        'topik': topik,
        'vidio' : vidio
    }
    return render(request, 'main/topik.html', data)