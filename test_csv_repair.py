import unittest

from csv_repair import legacy_parse_rows, parse_rows


class CsvRepairTests(unittest.TestCase):
    def test_legacy_behavior_reproduces_blank_row_crash(self) -> None:
        with self.assertRaises(ValueError):
            legacy_parse_rows("10\n\n20\n30\n")

    def test_fixed_behavior_skips_blank_and_whitespace_rows(self) -> None:
        self.assertEqual(parse_rows("10\n\n  \n20\n30\n"), [10, 20, 30])

    def test_fixed_behavior_preserves_visible_invalid_input(self) -> None:
        with self.assertRaises(ValueError):
            parse_rows("10\nnope\n30\n")


if __name__ == "__main__":
    unittest.main()
