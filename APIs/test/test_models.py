from django.test import TestCase
from APIs.models import DnsRecords
from ..models import DnsRecords


class EntryModelTest(TestCase):

       def test_verbose_name_plural(self):
            self.assertEqual(str(DnsRecords._meta.verbose_name_plural), "records")