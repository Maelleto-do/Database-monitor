#!/usr/bin/env python3.7

import unittest


class SGBDTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du projet 'SGBD'."""

    def test_example(self):
        """Un simple test d'exemple"""
        always_one = 1
        self.assertTrue(always_one == 1, "True n'est pas vrai !")


if __name__ == "__main__":
    unittest.main()
