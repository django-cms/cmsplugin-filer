from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from filer.models import Image
try:
    import json
except:
    import simplejson as json


@login_required
def fetch_image_metadata(request):
    if not request.is_ajax():
        return HttpResponseForbidden()
    file_id = request.GET.get('id')
    try:
        file = Image.objects.get(pk=file_id)
    except File.DoesNotExist:
        file = None

    result = {'alt': file.default_alt_text,
              'caption': file.default_caption,
              'credit': file.default_credit,
              'width': file.width,
              'height': file.height} if file else {}

    return HttpResponse(json.dumps(result), mimetype="application/json")
