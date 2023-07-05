from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')

def analyse(request):
    text=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    uppercase=request.GET.get('uppercase','off')
    lowercase=request.GET.get('lowercase','off')
    nonewline=request.GET.get('nonewlines','off')
    extraspace=request.GET.get('removespace','off')
    charcount=request.GET.get('charcount','off')
    #print(removepunc)
    #print(text)

    if removepunc =='on':
        punctuations='''!(){}[];:'",.<>=-_+@#$%^&*'''
        analysed=""
        for char in text:
            if char not in punctuations:
                analysed=analysed + char
        params={'purpose':'Removed punctuations','analysed_text':analysed}
        return render(request,'analyse.html',params)

    elif (uppercase =='on'):
        analysed=""
        for char in text:
            analysed=analysed + char.upper()
 
        params={'purpose':'Text in uppercase','analysed_text':analysed}
        return render(request,'analyse.html',params)
    elif (lowercase =='on'):
        analysed=""
        for char in text:
            analysed=analysed + char.lower()

        params={'purpose':'Text in lowercase','analysed_text':analysed}
        return render(request,'analyse.html',params)
    elif (nonewline =='on'):
        analysed=""
        for char in text:
            if(char!='\n'):
                analysed=analysed + char

        params={'purpose':'Text after removing new lines','analysed_text':analysed}
        return render(request,'analyse.html',params)
    elif (extraspace =='on'):
        analysed=""
        for index,char in enumerate(text):
            if not(text[index]==' ' and text[index+1]==' '):
                analysed=analysed + char

        params={'purpose':'Text after removing extra spaces','analysed_text':analysed}
        return render(request,'analyse.html',params)
    elif (charcount =='on'):
        analysed=0
        for char in text:
            analysed=analysed + 1

        params={'purpose':'Total characters in text','analysed_text':analysed}
        return render(request,'analyse.html',params)
    else:
        return HttpResponse('error')
