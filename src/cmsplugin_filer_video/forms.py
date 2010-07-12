from django import forms
from cmsplugin_filer_video.models import Video

class VideoForm(forms.ModelForm):
    
    class Meta:
        model = Video
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')