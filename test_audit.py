import unittest
from audit import summarize


class GapTests(unittest.TestCase):
    def test_unpaired_subtask_is_skipped(self):
        rows = [{"task": "t", "subtask": "s", "domain": "sim",
                 "success": "1", "contact_error": "0"}]
        self.assertEqual(summarize(rows)["paired_subtasks"], 0)

    def test_gap_is_computed(self):
        rows = [
            {"task": "t", "subtask": "s", "domain": "sim", "success": "1", "contact_error": "0"},
            {"task": "t", "subtask": "s", "domain": "real", "success": "0", "contact_error": "1"},
        ]
        self.assertEqual(summarize(rows)["gaps"][0]["absolute_gap"], 1.0)

    def test_largest_gap_ranks_first(self):
        rows = [
            {"task": "t", "subtask": "small", "domain": "sim", "success": "1", "contact_error": "0"},
            {"task": "t", "subtask": "small", "domain": "real", "success": "1", "contact_error": "0"},
            {"task": "t", "subtask": "large", "domain": "sim", "success": "1", "contact_error": "0"},
            {"task": "t", "subtask": "large", "domain": "real", "success": "0", "contact_error": "1"},
        ]
        self.assertEqual(summarize(rows)["gaps"][0]["subtask"], "large")


if __name__ == "__main__":
    unittest.main()
