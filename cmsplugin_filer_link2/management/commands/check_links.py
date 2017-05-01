import requests

from django.core.management.base import BaseCommand
from django.core.urlresolvers import NoReverseMatch

from django.utils.translation import activate
from requests.exceptions import ConnectionError, MissingSchema

from cmsplugin_filer_link2.models import FilerLink2Plugin, LinkHealthState


class Command(BaseCommand):
    help = 'Check all links for the availability of their destination'

    def check_with_request(self, url):
        try:
            r = requests.get(url)
        except ConnectionError:
            return LinkHealthState.SERVER_ERROR
        except MissingSchema:
            return LinkHealthState.BAD_CONFIGURED

        return {
            # we are only interested in bad status codes
            '3': LinkHealthState.REDIRECT,
            '4': LinkHealthState.NOT_REACHABLE,
            '5': LinkHealthState.SERVER_ERROR
        }.get(str(r.status_code)[0])

    def handle(self, *args, **options):
        all_links = FilerLink2Plugin.objects.all()
        self.stdout.write('Checking {num} link-instances'.format(num=all_links.count()))

        for link in all_links:
            status = None
            if link.file:
                status = self.check_with_request(link.file.url)
            elif link.url:
                status = self.check_with_request(link.url)
            elif link.page_link:
                try:
                    # see if we can resolve the page this link points to
                    activate(link.language)
                    link.page_link.get_absolute_url()
                except NoReverseMatch:
                    status = LinkHealthState.NOT_REACHABLE
            link.set_linkstate(status)
