import tempfile
import unittest
from pathlib import Path

import check_setup


class SetupCheckTests(unittest.TestCase):
    def test_format_result_includes_status_name_and_detail(self):
        result = check_setup.CheckResult("OK", "Python", "Version is available")
        self.assertEqual(check_setup.format_result(result), "[OK] Python: Version is available")

    def test_path_exists_reports_existing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_file = root / "data" / "sales_data.csv"
            data_file.parent.mkdir()
            data_file.write_text("date,revenue\n2024-01-01,10\n", encoding="utf-8")

            result = check_setup.check_path(root, "data/sales_data.csv", "Sales data")

        self.assertEqual(result.status, "OK")
        self.assertEqual(result.name, "Sales data")

    def test_path_exists_reports_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            result = check_setup.check_path(root, "data/sales_data.csv", "Sales data")

        self.assertEqual(result.status, "FIX")
        self.assertIn("Missing data/sales_data.csv", result.detail)

    def test_check_package_reports_missing_required_package(self):
        result = check_setup.check_package(
            "not_a_real_package_for_this_course",
            required=True,
            module_available_fn=lambda package_name: False,
        )

        self.assertEqual(result.status, "FIX")
        self.assertTrue(result.required)

    def test_check_working_directory_reports_wrong_folder(self):
        with tempfile.TemporaryDirectory() as root_dir, tempfile.TemporaryDirectory() as other_dir:
            result = check_setup.check_working_directory(Path(root_dir), Path(other_dir))

        self.assertEqual(result.status, "FIX")
        self.assertIn("Run this from the main course folder", result.detail)


if __name__ == "__main__":
    unittest.main()
