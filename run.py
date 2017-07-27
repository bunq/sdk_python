#! /usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print('Invalid argument count. Usage: python3 run.py '
          'examples/example_name.py')

path = sys.argv[1]
module_ = path.rstrip('.py').replace('/', '.')
exec('import {}'.format(module_))
exec('{}.run()'.format(module_))
