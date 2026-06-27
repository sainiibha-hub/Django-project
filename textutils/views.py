
from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#    return HttpResponse("<h1>Hello Ibha</h1> " '''<a href=\"https://app.netlify.com/teams/ibha/projects\"> \
#    "Projects on Netlify</a>" ''')

# def about(request):
# return HttpResponse("About Ibha.")



def index(request):
    return render(request, 'index.html')
#     return HttpResponse("<h1>Home</h1>" '''<a href = \"removepunc\">Remove Punctuation</a><br>''' \
#     '''<a href = \"capitalizefirst\">Capitalize First</a><br>''' \
#     '''<a href = \"newlineremove\">New Line Remove</a><br>''' \
#     '''<a href = \"spaceremover\">Space Remover</a><br>''' \
#     '''<a href = \"charcount\">Character Count</a><br>''' 
# )
# def removepunctuation(request):
#     return HttpResponse("Remove Punctuation")

def ex1(request):
    s = '''<h1>Navigation Bar</h1>
    <a href = \"removepunctuation\">Remove Punctuation</a><br>
    <a href = \"capitalizefirst\">Capitalize First</a><br>
    <a href = \"newlineremove\">New Line Remove</a><br>
    <a href = \"spaceremover\">Space Remover</a><br>
    <a href = \"charcount\">Character Count</a><br>'''
    return HttpResponse(s)

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)


    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    print(removepunc)
    fullcaps = request.POST.get('fullcaps', 'off')
    print(fullcaps)
    newlineremove = request.POST.get('newlineremove', 'off')
    print(newlineremove)
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(extraspaceremover)
    charcount = request.POST.get('charcount', 'off')
    print(charcount)

# check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        # analyzed = djtext
       
        return render(request, 'analyze.html', params)
    

    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # analyzed = djtext
        return render(request, 'analyze.html', params)
    

    elif(newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params={'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        # analyzed = djtext
        return render(request, 'analyze.html', params)
    

    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params={'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        # analyzed = djtext
        return render(request, 'analyze.html', params)
    
    elif(charcount == "on"):
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1

        params={'purpose': 'Character Count', 'analyzed_text': analyzed}
        # analyzed = djtext
        return render(request, 'analyze.html', params)

    else :
        return HttpResponse("Error")

    # return HttpResponse("<h1>Text Processed</h1>" )

# def capitalizefirst(request):
#     return HttpResponse("Capitalize First")

# def newlineremove(request):
#     return HttpResponse("New Line Remove")

# def spaceremover(request):
#     return HttpResponse("Space Remover <a href = '/'>Back</a>")

# def charcount(request):
#     return HttpResponse("Character Count")  