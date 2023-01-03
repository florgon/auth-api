"""
    Tests password unit (hashing).
"""

import unittest

from app.services.passwords import check_password, get_hashed_password


class TestPasswordsUnit(unittest.TestCase):
    """Check password unit (hashes)"""

    def test_passwords(self):
        """Check that password hashed correcly and does not allow to pass non-strings."""
        test_password = "mypassword"
        with self.assertRaises(TypeError):
            check_password(32, 64, hash_method=0)  # noqa
        self.assertTrue(
            check_password(
                test_password, get_hashed_password(test_password, hash_method=0)
            )
        )
        self.assertEqual(
            get_hashed_password(test_password, hash_method=0),
            get_hashed_password(test_password, hash_method=0),
        )

        # Hash method 1 (second).
        self.assertTrue(
            check_password(
                test_password, get_hashed_password(test_password, hash_method=1)
            )
        )
        self.assertEqual(
            get_hashed_password(test_password, hash_method=1),
            get_hashed_password(test_password, hash_method=1),
        )
        with self.assertRaises(TypeError):
            check_password(32, 64, hash_method=1)  # noqa
