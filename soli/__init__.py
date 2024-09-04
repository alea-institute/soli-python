"""
Python library for SOLI, the Standard for Open Legal Information
"""

# SPDX-License-Identifier: MIT
# (c) 2024 ALEA Institute.

__version__ = "0.1.4"
__author__ = "ALEA Institute"
__license__ = "MIT"
__description__ = "Python library for SOLI, the Standard for Open Legal Information"
__url__ = "https://openlegalstandard.org/"


# import graph to re-export
from .graph import SOLI, SOLITypes, SOLI_TYPE_IRIS
from .models import OWLClass, NSMAP

__all__ = ["SOLI", "SOLITypes", "SOLI_TYPE_IRIS", "OWLClass", "NSMAP"]
