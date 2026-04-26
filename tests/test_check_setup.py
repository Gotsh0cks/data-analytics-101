import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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

    def test_missing_required_package_detail_installs_core_packages_only(self):
        result = check_setup.check_package(
            "pandas",
            required=True,
            module_available_fn=lambda package_name: False,
        )

        self.assertIn(
            "python -m pip install pandas matplotlib seaborn openpyxl requests",
            result.detail,
        )
        self.assertNotIn("requirements.txt", result.detail)

    def test_missing_later_package_does_not_count_as_required_collect_failure(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for folder in check_setup.COURSE_FOLDERS:
                (root / folder).mkdir()
            for relative_path, _name in check_setup.CORE_DATA_FILES:
                path = root / relative_path
                path.parent.mkdir(exist_ok=True)
                path.write_text("example\n", encoding="utf-8")

            def fake_check_package(package_name, required=True):
                if required:
                    return check_setup.CheckResult("OK", package_name, "Package is installed")
                return check_setup.CheckResult(
                    "LATER",
                    package_name,
                    "Not installed yet. You only need this later for SQL Server lessons.",
                    required=False,
                )

            with patch("check_setup.check_package", side_effect=fake_check_package):
                results = check_setup.collect_results(root, root)

        later_results = [result for result in results if result.status == "LATER"]
        failure_count = sum(
            1 for result in results if result.required and result.status == "FIX"
        )

        self.assertEqual(len(later_results), 1)
        self.assertFalse(later_results[0].required)
        self.assertEqual(failure_count, 0)

    def test_check_working_directory_reports_wrong_folder(self):
        with tempfile.TemporaryDirectory() as root_dir, tempfile.TemporaryDirectory() as other_dir:
            result = check_setup.check_working_directory(Path(root_dir), Path(other_dir))

        self.assertEqual(result.status, "FIX")
        self.assertIn("Run this from the main course folder", result.detail)


if __name__ == "__main__":
    unittest.main()
