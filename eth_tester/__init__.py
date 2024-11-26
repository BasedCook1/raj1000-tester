from importlib.metadata import (
    version as __version,
)

from .backends import (
    MockBackend,
    PyEVMBackend,
)
from .main import (
    RAJ1000ereumTester,
)

__version__ = __version("RAJ1000-tester")
