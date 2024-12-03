import contextlib
import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import PackageNotFoundError, version
else:
    from importlib_metadata import PackageNotFoundError, version

with contextlib.suppress(PackageNotFoundError):
    __version__ = version("package-name")


from marchingalgo._find_contours import find_contours
from marchingalgo._marching_cubes_lewiner import marching_cubes
__all__ = [
    find_contours,
    marching_cubes,
]
