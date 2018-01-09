import sys
import unittest
import warnings


def runtests(argv):
  # obtain command line arguments
  try:
    opts, args = getopt.getopt(argv, 'hvp:m')
  except getopt.GetoptError:
    usage()
    sys.exit(2)
    
if __name__ == '__main__':
  runtests(sys.argv[1:])
