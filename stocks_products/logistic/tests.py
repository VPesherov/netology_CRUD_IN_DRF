from django.test import TestCase


class Test1(TestCase):
    def test_test(self):
        assert 2 + 2 == 4

    def test_test1(self):
        assert 2 + 2 != 5