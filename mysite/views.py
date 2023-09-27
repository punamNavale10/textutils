# I have created this file - punam

from django.http import HttpResponse
from django.shortcuts import render

def index(request):   
    return render(request,'index.html')
    
def analyze(request):
    # get the text
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    
    if removepunc == 'on':
        punctuatuions = '''!{}-()[];:'"\?/<>,@#$%^&*_~-'''
        analyze = ""
        for char in djtext:
            if char not in punctuatuions:
                analyze = analyze+char
                
        params = {'purpose':'Removed Punctuations','analyzed_text':analyze}
        djtext = analyze
       
    if fullcaps=='on':
        analyze = ""
        for char in djtext :
            analyze = analyze+char.upper()
        params ={'purpose':'Changed to uppercase','analyzed_text':analyze}
        djtext = analyze
       
    if newlineremover=='on':
        analyze=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyze = analyze + char
        params ={'purpose':'Removed new line','analyzed_text':analyze}
        djtext = analyze
        
    if extraspaceremover=='on':
        analyze=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyze = analyze + char
        params ={'purpose':'Removed extra spaces','analyzed_text':analyze}
        djtext = analyze
         
    if charcount=='on':
        i=0
        for char in djtext:
            i = i+1
        params ={'purpose':'Character count','analyzed_text':i}
        
    if(removepunc!='on' and fullcaps!='on' and newlineremover !='on' and extraspaceremover !='on' and charcount !='on'):
        return HttpResponse('You have not selected anything! \n Please select some analyzing operation')
    
    return render(request,'analyze.html',params)

