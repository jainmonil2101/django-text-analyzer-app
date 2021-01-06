# I have created this file - Monil

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # Analyze the text
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,/?@#$%^&*_~.<>='''
        analyzed = ""
        for monil in djtext:
            if monil not in punctuations:
                analyzed = analyzed + monil
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = f"Characters in {djtext} is {len(djtext)}"
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != "on") and (fullcaps != "on") and (newlineremover != "on") and (extraspaceremover != "on") and (charcount != "on"):
        return HttpResponse("Error")

    return render(request, "analyze.html", params)
