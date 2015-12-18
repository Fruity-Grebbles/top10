from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
getters = [ basename(f)[:-3] for f in modules if isfile(f)]
__all__ = getters
