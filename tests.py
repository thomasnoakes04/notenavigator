import unittest
from notenavigator import get_scale


class TestScales(unittest.TestCase):
    def test_major_scales(self):
        self.assertEqual(get_scale('C', 'major'),
                         ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'])
        self.assertEqual(get_scale('F', 'major'),
                         ['F', 'G', 'A', 'A#', 'C', 'D', 'E', 'F'])
        self.assertEqual(get_scale('G', 'major'),
                         ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G'])
        self.assertEqual(get_scale('A#', 'major'),
                         ['A#', 'C', 'D', 'D#', 'F', 'G', 'A', 'A#'])

    def test_harmonic_minor_scales(self):
        self.assertEqual(get_scale('A', 'harmonic minor'),
                         ['A', 'B', 'C', 'D', 'E', 'F', 'G#', 'A'])
        self.assertEqual(get_scale('C', 'harmonic minor'),
                         ['C', 'D', 'D#', 'F', 'G', 'G#', 'B', 'C'])
        self.assertEqual(get_scale('G#', 'harmonic minor'),
                         ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'G', 'G#'])
        self.assertEqual(get_scale('B', 'harmonic minor'),
                         ['B', 'C#', 'D', 'E', 'F#', 'G', 'A#', 'B'])

    def test_invalid_root_note(self):
        with self.assertRaises(ValueError):
            get_scale('H', 'major')

    def test_invalid_scale_type(self):
        with self.assertRaises(KeyError):
            get_scale('C', 'magor')

    def test_flats_handling(self):
        self.assertEqual(get_scale('Bb', 'major'),
                         ['A#', 'C', 'D', 'D#', 'F', 'G', 'A', 'A#'])
        self.assertEqual(get_scale('Eb', 'major'),
                         ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D', 'D#'])

    def test_enharmonic_equivalent_handling(self):
        self.assertEqual(get_scale('Cb', 'major'),
                         get_scale('B', 'major'))
        self.assertEqual(get_scale('E#', 'harmonic minor'),
                         get_scale('F', 'harmonic minor'))


if __name__ == "__main__":
    unittest.main()
