from cms.models import CMSPlugin
from cmsplugin_filer_link.models import FilerLinkPlugin
from django.core.management.base import BaseCommand
from django.db import transaction

from link2.cmsplugin_filer_link2.models import FilerLink2Plugin


class Command(BaseCommand):
    help = "Migrate all FilerLinkPlugin to FilerLink2Plugins"


    def handle(self, *args, **options):
        old_links = FilerLinkPlugin.objects.all()
        self.stdout.write('Migrating {num} FilerLinkPlugin objects to FilerLink2Plugins'.format(num=len(old_links)))

        with transaction.atomic():
            for old_link in old_links:
                cmsplugin = CMSPlugin.objects.get(id=old_link.cmsplugin_ptr_id)
                FilerLinkPlugin.objects.filter(id=old_link.id).delete()

                link = FilerLink2Plugin(cmsplugin_ptr=cmsplugin)
                # link.pk = old_link.pk
                # link.name = old_link.name
                # link.url = old_link.url
                # link.page_link = old_link.page_link
                # link.mailto = old_link.mailto
                # link.link_style = old_link.mailto

                link.__dict__.update(old_link.__dict__)

                # link.new_window = old_link.new_window
                # link.file = old_link.file

                # new_cmsplugin_ptr.pk = None
                print cmsplugin.pk

                # new_cmsplugin_ptr.pk = None



                # new_cmsplugin_ptr.save()
                # cmsplugin.save()
                # cmsplugin.save()
                # link.cmsplugin_ptr = cmsplugin
                # link.cmsplugin_ptr.refresh_from_db()
                print cmsplugin.pk
                print link.cmsplugin_ptr_id
                link.plugin_type = 'FilerLink2Plugin'
                link.save()
                link.parent.numchild += 1
                link.parent.save()


