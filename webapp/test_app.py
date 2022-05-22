import datetime
import logging
import os
from concurrent.futures import thread

from app import add

def test_add():
    assert 2 == add(1)