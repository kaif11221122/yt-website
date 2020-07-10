from django.http import HttpResponse
from django.shortcuts import render
import pafy
import pytube
from pytube import YouTube

def main(request):
    #return HttpResponse('Hii')
    return render(request,'index.html')

def dwn(request):

    ado = request.GET.get('ado','off')
    vdo = request.GET.get('vdo','off')
    url = request.GET.get('text2','default')

    if ado=='off' and vdo=='off':
        return render(request,'errorpage1.html')
    if 'https://www.youtube.com/watch?v=' not in url:
        return render(request,'errorpage4.html')
    else:
        if ado=='on':
            try:
                ado_downloader(url)
                return render(request,'dwn.html')
            except:
                return render(request,'errorpage2.html')
        
        if vdo=='on':
            try:
                vd_downloader(url)
                return render(request,'dwn.html')
            except:
                return render(request,'errorpage3.html')

def ado_downloader(ip_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    result = pafy.new(ip_url,headers)
    best_quality_audio = result.getbestaudio()
    best_quality_audio.download()

def vd_downloader(ip_url):
    yt = pytube.YouTube(ip_url)
    stream = yt.streams.first()
    stream.download()
