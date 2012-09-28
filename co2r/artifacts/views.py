from dynamicresponse.response import SerializeOrRender

from django.http import Http404

from co2r.artifacts.models import Artifact, Footprint


def artifacts(request):
    """
    Returns a list of all artifacts
    """
    artifacts = Artifact.objects.all()

    language_code = request.GET.get('language', None)
    if language_code != None:
        for artifact in artifacts:
            artifact.set_language(language_code)

    return SerializeOrRender('artifacts/list.html', {'artifacts': artifacts})


def artifact(request, slug):
    """
    Returns a list of all artifacts
    """
    artifact = Artifact.objects.get(slug=slug)

    language_code = request.GET.get('language', None)
    if language_code != None:
        artifact.set_language(language_code)

    return SerializeOrRender('artifacts/artifact.html', {'artifact': artifact})


def footprints(request):
    footprints = Footprint.objects.all()
    return SerializeOrRender('artifacts/footprints.html', {'footprints': footprints})


def footprint(request, slug, year):
    try:
        footprint = Footprint.objects.get(artifact__slug=slug,
            year=year)
    except Footprint.DoesNotExist:
        raise Http404

    return SerializeOrRender('artifacts/footprint.html', {'footprint': footprint})

# Create your views here.
