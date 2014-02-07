from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from filer.models import Image
from django.forms.widgets import Select
from cmsplugin_filer_image.models import ThumbnailOption
from django.utils.safestring import mark_safe


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
    except Image.DoesNotExist:
        file = None

    widget = Select()
    th_options = ThumbnailOption.objects.get_default_options(file)
    widget.choices = zip([th_opt.id for th_opt in th_options], th_options)
    widget.choices.insert(0, ('', '--------'))

    options = [widget.render_options((), [])]

    options = mark_safe(u''.join(options))

    result = {'alt': file.default_alt_text,
              'caption': file.default_caption,
              'credit': file.default_credit,
              'width': file._width,
              'height': file._height,
              'options': options} if file else {}

    return HttpResponse(json.dumps(result), mimetype="application/json")
