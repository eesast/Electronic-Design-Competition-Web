from django.shortcuts import render_to_response

def contact(request):

    if request.method == 'POST':

        print(request.POST['txtBody'])
        print(request.POST['txtform'])

    return render_to_response('contact.html')

# Create your views here.
