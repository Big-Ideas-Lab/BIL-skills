#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
def main():
 from importlib.util import spec_from_file_location,module_from_spec
 spec=spec_from_file_location('catalog',ROOT/'design-system/validate_catalog.py'); mod=module_from_spec(spec); spec.loader.exec_module(mod)
 return mod.main()
if __name__=='__main__': sys.exit(main())
