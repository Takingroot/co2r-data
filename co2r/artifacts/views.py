from dynamicresponse.response import SerializeOrRender

from django.http import Http404

from co2r.artifacts.models import Artifact, Footprint


def artifacts(request):
    """
    Returns a list of all artifacts
    """
    artifacts = Artifact.objects.all()

    return SerializeOrRender('artifacts/list.html', {'artifacts': artifacts})


def artifact(request, internal_name):
    """
    Returns a list of all artifacts
    """
    artifact = Artifact.objects.get(internal_name=internal_name)

    return SerializeOrRender('artifacts/artifact.html', {'artifact': artifact})


def footprints(request):
    footprints = Footprint.objects.all()
    return SerializeOrRender('artifacts/footprints.html', {'footprints': footprints})


def footprint(request, internal_name, year):
    try:
        footprint = Footprint.objects.get(artifact__internal_name=internal_name,
            year=year)
    except Footprint.DoesNotExist:
        raise Http404

    return SerializeOrRender('artifacts/footprint.html', {'footprint': footprint})

# Create your views here.
