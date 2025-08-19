import glob
import os
import sys
from pathlib import Path

from validate import validate_package

report_errors = []


def main():

    print("Generating CI report...")

    print("## CI Quality Check 🤖🚨")
    for package in glob.glob("src/*"):
        package_name = os.path.basename(package)

        print(f"Validating package: {package_name}... ", end="", flush=True)

        errors = validate_package(package)
        if len(errors) == 0:
            print("OK")
            continue

        print(f"Found {len(errors)} errors:")

        for error in errors:
            print(f"Check: {error.name}")
            print(f" ->: {error.error}")

        report_errors.append(
            {
                "package": package_name,
                "errors": errors,
            }
        )

    if len(report_errors) == 0:
        print("All checks passed ✅ Great job!\n")

    else:
        print(
            "Oh snap! Our robots detected some errors 🤖 We need to solve them before merging the package:\n"
        )
        for package in report_errors:
            package_name = package["package"]
            package_errors = package["errors"]
            print(f"### Package: {package_name}\n\n")
            for error in package_errors:
                error_name = error.name
                error_message = error.error
                print(f"#### Check: **{error_name}** ❌\n\n")
                print(f"```\n{error_message}\n```\n\n")
        print(
            "After you fixed the problems, please create another commit and push it to re-run the checks 🚀"
        )

    if len(report_errors) == 0:
        print("All ok!")
    else:
        print("Errors detected, please see attached report.")
        sys.exit(1)


if __name__ == "__main__":
    main()
