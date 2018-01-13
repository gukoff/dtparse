from __future__ import absolute_import

from datetime import datetime
from ._dtparse import Parser  # Import Parser from the rust binary

__all__ = ['parse']

# It doesn't make sense to create a Parser instance every time.
# We'll create just one and put it's parse method into the global scope.
parse = Parser(datetime).parse
