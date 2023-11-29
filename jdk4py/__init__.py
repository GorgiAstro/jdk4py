"""JDK packaged for Python."""

from pathlib import Path

_PACKAGE_DIRECTORY = Path(__file__).parent

JAVA_HOME = _PACKAGE_DIRECTORY.absolute() / "java-runtime"
JAVA = JAVA_HOME / "bin" / "java"

_major, _minor, _patch = [
    int(part)
    for part in (_PACKAGE_DIRECTORY / "java_version.txt").read_text().strip().split(".")
][:3]
JAVA_VERSION = _major, _minor, _patch
