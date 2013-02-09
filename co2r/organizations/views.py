from dynamicresponse.response import Serialize
from co2r.organizations.models import Organization


def organizations(request):
    """
    Returns a list of all artifacts
    """
    organizations = Organization.objects.all()

    language_code = request.GET.get('language', None)
    if language_code != None:
        for organization in organizations:
            organization.set_language(language_code)

    return Serialize('organizations/list.html', {'organizations': organizations})

# Create your views here.
