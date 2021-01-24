from django.test import TestCase
from dojo.tools.fortify.parser import FortifyXMLParser
from dojo.models import Test
from datetime import datetime


class TestFortifyParser(TestCase):

    def test_fortify_many_findings(self):
        testfile = "dojo/unittests/scans/fortify/fortify_many_findings.xml"
        parser = FortifyXMLParser(testfile, Test())
        self.assertEqual(324, len(parser.items))
        self.assertEqual(parser.items[0].date, datetime(2019, 12, 17))

    def test_fortify_few_findings(self):
        testfile = "dojo/unittests/scans/fortify/fortify_few_findings.xml"
        parser = FortifyXMLParser(testfile, Test())
        self.assertEqual(2, len(parser.items))
        self.assertEqual(parser.items[0].date, datetime(2019, 5, 7))

    def test_fortify_few_findings_count_chart(self):
        testfile = "dojo/unittests/scans/fortify/fortify_few_findings_count_chart.xml"
        parser = FortifyXMLParser(testfile, Test())
        self.assertEqual(3, len(parser.items))
        self.assertEqual(parser.items[0].date, datetime(2019, 5, 7))
