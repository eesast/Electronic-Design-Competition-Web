from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, mail_admins, BadHeaderError


def contact(request):

    success_submit = False

    if request.method == 'POST':

        subject = request.POST.get('reason')
        message = request.POST.get('message')
        email = request.POST.get('email')
        if subject and message and email:
            try:
           #     send_mail( subject,
           #               message,
           #               email,
           #               ['mildwindyu@hotmail.com'],
           #               fail_silently=False,
           #     )
                mail_admins(subject, message+'\n'+email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')




        success_submit = True


    return render(request, 'contact.html', {'success_submit' : success_submit})

# Create your views here.
