from openff.evaluator.utils.packmol import _find_packmol
from openff.evaluator import __version__

assert __version__ != "0.0.0", f"Version mangled! Found {__version__=}"

assert _find_packmol() is not None
