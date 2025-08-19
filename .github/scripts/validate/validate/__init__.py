import os
from collections import namedtuple
from typing import List

from .rules.incoherent_path import IncoherentPath
from .rules.invalid_package_name import InvalidPackageName
from .rules.invalid_version_path import InvalidVersionPath
from .rules.invalid_yaml import InvalidYAML
from .rules.missing_mandatory_files import MissingMandatoryFiles
from .rules.missing_manifest_fields import MissingManifestFields
from .rules.no_yaml_extension import NoYAMLExtension

RULES = [
    MissingMandatoryFiles(),
    InvalidVersionPath(),
    InvalidPackageName(),
    IncoherentPath(),
    MissingManifestFields(),
    InvalidYAML(),
    NoYAMLExtension(),
]

ValidationError = namedtuple("ValidationError", "name error")


def validate_package(path: str) -> List[ValidationError]:
    print("Start validation")
    if not os.path.isdir(path):
        raise Exception(f"the given path is not a directory: {path}")

    errors = []

    for rule in RULES:
        try:
            print(f"Running {rule.name()}", end="... ", flush=True)
            rule.validate(path)
        except Exception as e:
            print("❌")
            errors.append(ValidationError(rule.name(), e))
        else:
            print("✅")

    return errors
