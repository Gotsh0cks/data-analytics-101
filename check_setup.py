from dataclasses import dataclass
from importlib.util import find_spec
from pathlib import Path
import platform
import sys


MIN_PYTHON = (3, 10)

REQUIRED_PACKAGES = [
    ("pandas", "Module 3 data analysis"),
    ("matplotlib", "Module 5 charts"),
    ("seaborn", "Module 5 chart styling"),
    ("openpyxl", "Module 2 Excel files"),
    ("requests", "Module 6 dataset downloads"),
]

LATER_PACKAGES = [
    ("pyodbc", "Module 4 Python and SQL Server"),
]

COURSE_FOLDERS = [
    "00-what-is-data-analytics",
    "01-setting-up",
    "02-spreadsheets",
    "03-data-analysis",
    "04-databases-and-sql",
    "05-visualization",
    "06-real-world-data",
    "07-capstone",
    "cheatsheets",
    "data",
]

CORE_DATA_FILES = [
    ("data/sales_data.csv", "Sales data"),
    ("data/employees.csv", "Employee data"),
    ("data/customers.csv", "Customer data"),
]


@dataclass(frozen=True)
class CheckResult:
    status: str
    name: str
    detail: str
    required: bool = True


def format_result(result):
    return f"[{result.status}] {result.name}: {result.detail}"


def module_available(package_name):
    return find_spec(package_name) is not None


def check_python_version():
    current = sys.version_info
    current_text = platform.python_version()
    minimum_text = ".".join(str(part) for part in MIN_PYTHON)
    if current >= MIN_PYTHON:
        return CheckResult("OK", "Python", f"Version {current_text} is installed")
    return CheckResult(
        "FIX",
        "Python",
        f"Version {current_text} is installed, but this course expects Python {minimum_text} or newer",
    )


def check_working_directory(root, cwd):
    root = root.resolve()
    cwd = cwd.resolve()
    if cwd == root:
        return CheckResult("OK", "Course folder", f"Running from {root}")
    return CheckResult(
        "FIX",
        "Course folder",
        f"Run this from the main course folder: {root}",
    )


def check_package(package_name, required=True, module_available_fn=module_available):
    if module_available_fn(package_name):
        return CheckResult("OK", package_name, "Package is installed", required=required)

    if required:
        return CheckResult(
            "FIX",
            package_name,
            "Package is missing. Run: python -m pip install -r requirements.txt",
            required=True,
        )

    return CheckResult(
        "LATER",
        package_name,
        "Not installed yet. You only need this later for SQL Server lessons.",
        required=False,
    )


def check_path(root, relative_path, name):
    path = root / relative_path
    if path.exists():
        return CheckResult("OK", name, f"Found {relative_path}")
    return CheckResult(
        "FIX",
        name,
        f"Missing {relative_path}. Confirm you extracted the full course folder.",
    )


def collect_results(root, cwd):
    results = [
        check_python_version(),
        check_working_directory(root, cwd),
    ]

    for folder in COURSE_FOLDERS:
        results.append(check_path(root, folder, f"Folder {folder}"))

    for relative_path, name in CORE_DATA_FILES:
        results.append(check_path(root, relative_path, name))

    for package_name, purpose in REQUIRED_PACKAGES:
        result = check_package(package_name, required=True)
        if result.status == "OK":
            results.append(CheckResult("OK", package_name, f"Installed for {purpose}"))
        else:
            results.append(result)

    for package_name, purpose in LATER_PACKAGES:
        result = check_package(package_name, required=False)
        if result.status == "OK":
            results.append(CheckResult("OK", package_name, f"Installed for {purpose}", required=False))
        else:
            results.append(result)

    return results


def print_next_steps(failure_count):
    print()
    if failure_count:
        print("Some required checks need attention.")
        print("Start with the [FIX] messages above.")
        print("If you are not sure what to do, open GET_HELP.md and copy the help template.")
    else:
        print("Core setup looks ready.")
        print("If you are early in the course, you can continue with Module 0 or Module 1.")
        print("Items marked [LATER] are only needed in later modules.")


def main():
    root = Path(__file__).resolve().parent
    cwd = Path.cwd()

    print("=" * 60)
    print("Data Analytics 101 Setup Check")
    print("=" * 60)
    print()

    results = collect_results(root, cwd)
    failure_count = 0

    for result in results:
        print(format_result(result))
        if result.required and result.status == "FIX":
            failure_count += 1

    print_next_steps(failure_count)
    return 1 if failure_count else 0


if __name__ == "__main__":
    sys.exit(main())
