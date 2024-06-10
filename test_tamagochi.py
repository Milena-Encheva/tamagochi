import unittest

from tamagochi import Cat, Dog


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Liza')

    # Test the sound functionally with cat.

    def test_sound(self):
        self.assertEqual(self.cat.make_sound(), 'Meow, Meow')

    # Test the feed functionally with cat.

    def test_feed_successful(self):
        self.cat._hungry_level = 9
        self.cat._mood = 9
        self.assertEqual(self.cat.feed(), "You have fed you Liza - it less less hungry "
                                          "(hungry level increased to 10) and more happy - mood increased "
                                          "to 10 points.Meow, Meow!")

    def test_feed_not_hungry(self):
        self.cat._hungry_level = 10
        self.assertEqual(self.cat.feed(), "Liza is not hungry!")

    def test_feed_too_exited(self):
        self.cat._mood = 10
        self.assertEqual(self.cat.feed(), "Liza is too excited!")

    # Test the sleep functionally with cat.

    def test_put_to_sleep_successful(self):
        self.cat._energy_level = 9
        self.cat._hungry_level = 10
        self.assertEqual(self.cat.put_to_sleep(), "You put your Liza to sleep -"
                                                  " its energy increased to 10 but will get up hungrier - "
                                                  "its hungry lever decreased to 9.")

    def test_not_tired_to_sleep(self):
        self.cat._energy_level = 10
        self.assertEqual(self.cat.put_to_sleep(), 'Liza is not tired!')

    def test_too_hungry_to_sleep(self):
        self.cat._hungry_level = 1
        self.assertEqual(self.cat.put_to_sleep(), 'Liza is too hungry to sleep!')

    # Test the play functionally with cat.

    def test_play_successful(self):
        self.cat._mood = 9
        self.cat._energy_level = 10
        self.assertEqual(self.cat.play(), 'You have played with your Liza - it got a little tired energy level'
                                          ' decreased to 9) but is happy now - mood increased to 10 points. '
                                          'Meow, Meow!')

    def test_do_not_want_to_play(self):
        self.cat._mood = 10
        self.assertEqual(self.cat.play(), 'Liza does not want to play!')

    def test_too_tired_to_play(self):
        self.cat._energy_level = 1
        self.assertEqual(self.cat.play(), 'Liza is too tired')


class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog('Rio')

    # Test the sound functionally with cat.

    def test_sound(self):
        self.assertEqual(self.dog.make_sound(), 'Woof, woof')

    # Test the feed functionally with cat.

    def test_feed_successful(self):
        self.dog._hungry_level = 7
        self.dog._mood = 3
        self.assertEqual(self.dog.feed(), "You have fed you Rio - it less less hungry "
                                          "(hungry level increased to 8) and more happy - mood increased "
                                          "to 4 points.Woof, woof!")

    def test_feed_not_hungry(self):
        self.dog._hungry_level = 10
        self.assertEqual(self.dog.feed(), "Rio is not hungry!")

    def test_feed_too_exited(self):
        self.dog._mood = 10
        self.assertEqual(self.dog.feed(), "Rio is too excited!")

    # Test the sleep functionally with cat.

    def test_put_to_sleep_successful(self):
        self.dog._energy_level = 3
        self.dog._hungry_level = 3
        self.assertEqual(self.dog.put_to_sleep(), "You put your Rio to sleep -"
                                                  " its energy increased to 4 but will get up hungrier - "
                                                  "its hungry lever decreased to 2.")

    def test_not_tired_to_sleep(self):
        self.dog._energy_level = 10
        self.assertEqual(self.dog.put_to_sleep(), 'Rio is not tired!')

    def test_too_hungry_to_sleep(self):
        self.dog._hungry_level = 1
        self.assertEqual(self.dog.put_to_sleep(), 'Rio is too hungry to sleep!')

    # Test the play functionally with cat.

    def test_play_successful(self):
        self.dog._mood = 6
        self.dog._energy_level = 8
        self.assertEqual(self.dog.play(), 'You have played with your Rio - it got a little tired energy level'
                                          ' decreased to 7) but is happy now - mood increased to 7 points. '
                                          'Woof, woof!')

    def test_do_not_want_to_play(self):
        self.dog._mood = 10
        self.assertEqual(self.dog.play(), 'Rio does not want to play!')

    def test_too_tired_to_play(self):
        self.dog._energy_level = 1
        self.assertEqual(self.dog.play(), 'Rio is too tired')


if __name__ == "__main__":
    unittest.main()