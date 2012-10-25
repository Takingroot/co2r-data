from dynamicresponse.response import SerializeOrRender

from django.core.mail import send_mail
from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from co2r.main.models import Faq, Co2Equivalents, DefinedTerms, Locale
from co2r.main.forms import EmailForm
from co2r.artifacts.models import OffsetVariables

@csrf_exempt
def email(request):
    """
    Allow the Co2r frontend to send emails
    """

    results = {
        'status': {
            'success': False,
            'errors': []
        }
    }

    if request.method == 'POST':
        json_data = simplejson.loads(request.POST)
        form = EmailForm(json_data)
        
        if form.is_valid():
            sender = settings.EMAIL_SENDER
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = [recipient[1] for recipient in settings.TAKINGROOT_STAFF]

            send_mail(subject, message, sender, recipients, fail_silently=False)
            results['status']['success'] = True
        else:
            results['errors'] = form.errors

    json = simplejson.dumps(results)

    return HttpResponse(json, mimetype='application/json')


def faqs(request):
    """
    Display FAQs
    """

    faqs = Faq.objects.all()

    language_code = request.GET.get('language', None)
    if language_code != None:
        for faq in faqs:
            faq.set_language(language_code)

    return SerializeOrRender('main/faqs.html', {'faqs': faqs})


def app_content(request):
    """
    Return general app contents
    """

    context = {}

    equivalents = Co2Equivalents.objects.filter(active=True)

    language_code = request.GET.get('language', 'en')

    for equivalent in equivalents:
        equivalent.set_language(language_code)

    defined_terms = DefinedTerms.objects.filter(language=language_code)

    offset_variables = OffsetVariables.objects.all()

    context['offset_variables'] = offset_variables
    context['co2_artifact_comparisons'] = equivalents
    context['defined_terms'] = defined_terms

    return SerializeOrRender('main/app_content.html', context)

def locale(request, language):
    context = {}

    locale = Locale.objects.get(language=language)
    context['locale'] = locale

    return SerializeOrRender('main/app_content.html', context)
