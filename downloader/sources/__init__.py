from os import path
import glob
modules = glob.glob(path.dirname(__file__)+"/*.py")
sources = [ path.basename(f)[:-3] for f in modules if path.isfile(f) and not f.endswith('__init__.py') ]
__all__ = sources


