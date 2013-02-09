from dynamicresponse.response import Serialize

from django.http import Http404

from co2r.artifacts.models import Artifact, Footprint


def artifacts(request):
    """
    Returns a list of all artifacts
    """
    artifacts = Artifact.objects.filter(active=True)

    language_code = request.GET.get('language', None)
    if language_code != None:
        for artifact in artifacts:
            artifact.set_language(language_code)

    return Serialize({'artifacts': artifacts})


def artifact(request, slug):
    """
    Returns a list of all artifacts
    """
    artifact = Artifact.objects.get(slug=slug)

    language_code = request.GET.get('language', None)
    if language_code != None:
        artifact.set_language(language_code)

    return Serialize({'artifact': artifact})


def footprints(request):
    footprints = Footprint.objects.all()
    return Serialize({'footprints': footprints})


def footprint(request, slug, year):
    try:
        footprint = Footprint.objects.get(artifact__slug=slug,
            year=year)
    except Footprint.DoesNotExist:
        raise Http404

    return Serialize({'footprint': footprint})

# Create your views here.
