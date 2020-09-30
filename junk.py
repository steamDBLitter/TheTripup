import random
import sys

open('copy-of-%s' % sys.argv[0], 'w').write(open(sys.argv[0]).read())
