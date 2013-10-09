from django.test import TestCase
from filer.tests.helpers import create_superuser, create_image
import os
from django.core.files import File as DjangoFile
from filer.models.imagemodels import Image
from filer.models.filemodels import File
from cmsplugin_filer_image.models import ThumbnailOption


class ThumbnailOptionsTest(TestCase):

    def setUp(self):
        self.superuser = create_superuser()
        self.img = create_image()
        self.filename = os.path.join(os.path.dirname(__file__),
                                 'test.jpg')
        self.img.save(self.filename, 'JPEG')

        self.image = self.create_filer_image()
        self.image.save()

    def tearDown(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass
        for f in File.objects.all():
            f.delete()

    def create_filer_image(self):
        file_obj = DjangoFile(open(self.filename), name='test.jpg')
        image = Image.objects.create(owner=self.superuser,
                                     original_filename='test.jpg',
                                     file=file_obj)
        return image

    def test_20x20_image(self):
        self.image._width = 20
        self.image._height = 20

        qs = ThumbnailOption.objects.get_default_options_queryset(self.image)
        self.assertQuerysetEqual(qs,
                                 ['Original -- 20 x 20'],
                                 lambda o: str(o))

    def test_500x500_image(self):
        self.image._width = 500
        self.image._height = 500

        qs = ThumbnailOption.objects.get_default_options_queryset(self.image)
        self.assertQuerysetEqual(qs,
                                 ['Original -- 500 x 500',
                                  'Medium -- 320 x XXX',
                                  'Small -- 180 x XXX'],
                                 lambda o: str(o))

    def test_720x405_image(self):
        self.image._width = 720
        self.image._height = 405

        qs = ThumbnailOption.objects.get_default_options_queryset(self.image)
        self.assertQuerysetEqual(qs,
                                 ['Original -- 720 x 405', 'Large -- 640 x XXX',
                                  'Medium -- 320 x XXX', 'Small -- 180 x XXX'],
                                 lambda o: str(o))

    def test_1920x1080_image(self):
        self.image._width = 1920
        self.image._height = 1080

        qs = ThumbnailOption.objects.get_default_options_queryset(self.image)
        self.assertQuerysetEqual(qs,
                                 ['Original -- 1024 x 576', 'Large -- 640 x XXX',
                                  'Medium -- 320 x XXX', 'Small -- 180 x XXX'],
                                 lambda o: str(o))
