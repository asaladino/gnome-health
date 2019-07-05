import unittest

from src.data.model.Me import Me


class TestMe(unittest.TestCase):

    def test_format_date(self):
        """
        Make sure the date time is getting converted correctly.
        :return: None
        """
        me = Me()
        date1 = "1999-09-27"
        me.set_birth(date1)

        self.assertIsNotNone(me.birth)

        print(me.birth)
