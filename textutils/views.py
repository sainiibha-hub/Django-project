
# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))


def analyze(request):
    def get_input(name, default='off'):
        return request.POST.get(name, request.GET.get(name, default))

    djtext = request.POST.get('text', request.GET.get('text', '')) or ''

    # Check checkbox values
    removepunc = get_input('removepunc')
    fullcaps = get_input('fullcaps')
    newlineremover = get_input('newlineremover')
    extraspaceremover = get_input('extraspaceremover')
    charcount = get_input('charcount')

    # Check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        analyzed = ''.join(char for char in djtext if char not in punctuations)
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == 'on':
        analyzed = ''
        for char in djtext:
            if not (char == ' ' and analyzed.endswith(' ')):
                analyzed += char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ''.join(char for char in djtext if char not in '\n\r')
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcount == 'on':
        analyzed = str(len(djtext))
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error: no operation selected or text provided.')

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")

