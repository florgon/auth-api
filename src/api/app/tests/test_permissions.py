import unittest

from app.services.permissions import parse_permissions_from_scope, normalize_scope, Permission


class TestPermissionsUnit(unittest.TestCase):
    def test_normalization(self):
        with self.assertRaises(AssertionError):
            normalize_scope([Permission.email])
        self.assertEqual(normalize_scope(""), "")
        self.assertEqual(normalize_scope("email"), "email")
        self.assertEqual(normalize_scope("email,  email"), "email")
        self.assertEqual(normalize_scope("\nemail, \remail"), "")

    def test_parse(self):
        with self.assertRaises(AssertionError):
            parse_permissions_from_scope([Permission.email])
        self.assertIsInstance(parse_permissions_from_scope(""), list)
        self.assertEqual(parse_permissions_from_scope(""), [])
        self.assertEqual(parse_permissions_from_scope("email"), [Permission.email])
        self.assertEqual(parse_permissions_from_scope("email,  email"), [Permission.email])
        self.assertEqual(parse_permissions_from_scope("\nemail, \remail"), [])