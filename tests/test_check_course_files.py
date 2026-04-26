import tempfile
import unittest
from pathlib import Path

import check_course_files


class CourseFileCheckTests(unittest.TestCase):
    def test_required_path_failure_reports_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            results = check_course_files.check_required_paths(root)

        missing = [result for result in results if result.status == "FIX"]
        self.assertTrue(missing)
        self.assertEqual(missing[0].detail, "Missing required file")

    def test_extract_markdown_links_skips_images(self):
        text = (
            "[Start](START_HERE.md)\n"
            "![Chart](chart.png)\n"
            "[External](https://example.com)\n"
        )

        links = check_course_files.extract_markdown_links(text)

        self.assertEqual(links, ["START_HERE.md", "https://example.com"])

    def test_external_and_anchor_links_are_skipped(self):
        self.assertTrue(check_course_files.should_skip_link("https://example.com"))
        self.assertTrue(check_course_files.should_skip_link("mailto:test@example.com"))
        self.assertTrue(check_course_files.should_skip_link("#local-section"))
        self.assertFalse(check_course_files.should_skip_link("README.md"))

    def test_markdown_link_check_reports_broken_local_link(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            readme = root / "README.md"
            readme.write_text("[Missing](missing.md)\n", encoding="utf-8")

            results = check_course_files.check_markdown_links(root, [readme])

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].status, "FIX")
        self.assertIn("Broken local link", results[0].detail)

    def test_markdown_link_check_accepts_existing_local_link(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            readme = root / "README.md"
            target = root / "START_HERE.md"
            readme.write_text("[Start](START_HERE.md)\n", encoding="utf-8")
            target.write_text("# Start\n", encoding="utf-8")

            results = check_course_files.check_markdown_links(root, [readme])

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].status, "OK")


if __name__ == "__main__":
    unittest.main()
