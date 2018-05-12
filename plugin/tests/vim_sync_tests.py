import unittest
import vim_sync as sut


@unittest.skip("Don't forget to test!")
class VimSyncTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_sync_example()
        self.assertEqual("Happy Hacking", result)
