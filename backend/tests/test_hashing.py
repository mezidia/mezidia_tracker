from unittest import TestCase

from ..hashing import Hash


class TestHash(TestCase):
    def setUp(self):
        self.password = 'password'

    def test_bcrypt(self):
        hashed_password = Hash.bcrypt(self.password)
        self.assertIsNotNone(hashed_password)
        self.assertNotEqual(self.password, hashed_password)

    def test_verify(self):
        hashed_password = Hash.bcrypt(self.password)
        self.assertTrue(Hash.verify(hashed_password, self.password))
