import glob
import os

from . import ValidationRule


class InvalidVersionPath(ValidationRule):
    def name(self):
        return "invalid_version_path"

    def validate(self, path: str):
        package = "/".join(path.split("/")[-1])
        version_entries = glob.glob(os.path.join(package, "[0-9].[0-9].[0-9]"))
        all_entries = glob.glob(os.path.join(package, "*"))

        difference = list(set(all_entries) - set(version_entries))
        if len(difference) == 0:
            # All good, no differences
            return

        for diff in difference:
            raise Exception(
                f"unexpected file '{diff}', in that directory there should only be version number directories (like 0.1.0)"
            )
