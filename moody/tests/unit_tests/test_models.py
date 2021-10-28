# tests/test_models.py
from django.test import TestCase

from ..models import User


class UserTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        company = CompanyFactory()
        self.assertEqual(str(company), company.name)


class MoodTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        company = CompanyFactory()
        self.assertEqual(str(company), company.name)
