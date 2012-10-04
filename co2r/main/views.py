from dynamicresponse.response import SerializeOrRender

from co2r.main.models import Faq, Co2Equivalents, DefinedTerms
from co2r.artifacts.models import OffsetVariables


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

    equivalents = Co2Equivalents.objects.all()

    language_code = request.GET.get('language', 'en')

    for equivalent in equivalents:
        equivalent.set_language(language_code)

    defined_terms = DefinedTerms.objects.filter(language=language_code)

    offset_variables = OffsetVariables.objects.all()

    context['offset_variables'] = offset_variables
    context['co2_artifact_comparisons'] = equivalents
    context['defined_terms'] = defined_terms

    return SerializeOrRender('main/app_content.html', context)
