from cms.models import CMSPlugin
from cmsplugin_filer_link.models import FilerLinkPlugin
from django.core.management.base import BaseCommand
from django.db import transaction

from cmsplugin_filer_link2.models import FilerLink2Plugin


class Command(BaseCommand):
    help = 'Migrate all FilerLinkPlugin to FilerLink2Plugins'

    def handle(self, *args, **options):
        old_links = FilerLinkPlugin.objects.all()
        self.stdout.write('Migrating {num} FilerLinkPlugin objects to FilerLink2Plugins'.format(num=old_links.count()))

        with transaction.atomic():
            for old_link in old_links:
                cmsplugin = CMSPlugin.objects.get(id=old_link.cmsplugin_ptr_id)
                FilerLinkPlugin.objects.filter(id=old_link.id).delete()

                link = FilerLink2Plugin(cmsplugin_ptr=cmsplugin)
                link.__dict__.update(old_link.__dict__)
                link.plugin_type = 'FilerLink2Plugin'
                link.save()
                link.parent.numchild += 1
                link.parent.save()
