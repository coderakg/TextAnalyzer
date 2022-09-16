#Created-Akshat

import re
from string import punctuation
from django.http import HttpResponse 
from django.shortcuts import render

def index(request): #we have to give request as an arguement in the function to make this appear on the website
    return render(request,'index.html')
    
def analyze(request): # this is another path's function
    djtext = request.POST.get('text','default') #gets the text from the input field
    print(djtext)
    removepunc = request.POST.get('removepunc','off') #gets the text from the input field
    print(removepunc)
    fullcaps = request.POST.get('fullcaps','off') #gets the text from the input field
    print(fullcaps)
    newline_remover = request.POST.get('newline_remover','off') #gets the text from the input field
    print(newline_remover)
    space_remover = request.POST.get('space_remover','off') #gets the text from the input field
    print(space_remover)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext :
            if char not in punctuations:
                analyzed = analyzed + char
        
        dict = {
            'purpose' : 'Removed Punctuations',
            'analyzed_text' : analyzed
        }
        djtext=analyzed
        # return render(request,'analyze.html',dict)

    if(fullcaps != "off"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        dict = {
            'purpose' : 'CONVERT UPPERCASE',
            'analyzed_text' : analyzed
        }
        djtext=analyzed
        # return render(request,'analyze.html',dict_upper)

    if(newline_remover == "on"):
        analyzed= ""
        
        for char in djtext:
            if char != "\n" and char != "\r": #this will remove the new line character i.e will remove the new line and will put the words together.
                analyzed = analyzed + char
        
        dict = {
            'purpose' : 'Remove new line Character',
            'analyzed_text' : analyzed
        }
        djtext=analyzed
        # return render(request,'analyze.html',dict_upper)

    if(space_remover == "on"):
        analyzed= ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "): #this will remove the new line character i.e will remove the new line and will put the words together.
                analyzed = analyzed + char
        
        dict = {
            'purpose' : 'Remove extra spaces between lines',
            'analyzed_text' : analyzed
        }
        djtext=analyzed

    if (removepunc != "on" and fullcaps != "on" and newline_remover != "on" and space_remover !="on" ):
        return HttpResponse("error")

    return render(request,'analyze.html',dict)
# def capitalize_first(request): # this is another path's function
#     return HttpResponse('''Capitalize First letter of word 
#     <button> <a href = "/"> BACK <a/> </button>''') 

# def space_remover(request): # this is another path's function
#     return HttpResponse('''Removes the space in between 
#     <button> <a href = "/"> BACK <a/> </button>''') 

# def newline_remover(request): # this is another path's function
#     return HttpResponse('''Removes the new lines 
#     <button> <a href = "/"> BACK <a/> </button>''') 

# def char_count(request): # this is another path's function
#     return HttpResponse('''Counts the number of characters 
#      <button> <a href = "/"> BACK <a/> </button>''') 


