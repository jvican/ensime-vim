# coding: utf-8

import os
from contextlib import contextmanager
from pprint import pformat


class Util:

    @staticmethod
    def read_file(path):
        with open(path, "r") as f:
            result = f.read()
        return result

    @staticmethod
    def write_file(path, contents):
        with open(path, "w") as f:
            result = f.write(contents)
        return result

    @staticmethod
    def mkdir_p(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def extract_package_name(lines):
        found_package = False
        package = ""

        for line in lines:
            if "package" not in line and not found_package:
                continue
            elif "package" in line:
                if not package:
                    package = line.split("package ")[-1].replace("\n", "")
                else:
                    package += "." + line.split("package ")[-1].replace("\n", "")
            else:
                break
        return package


@contextmanager
def catch(exception, handler=lambda h: None):
    """If exception runs handler."""
    try:
        yield
    except exception as e:
        handler(str(e))


def module_exists(module_name):
    res = False
    with catch(ImportError):
        __import__(module_name)
        res = True
    return res


class Pretty(object):
    """Wrapper to pretty-format object's string representation.

    Reduces boilerplate for logging statements where we don't want to eagerly
    :func:`pprint.pformat` when the logging level isn't enabled.
    """

    def __init__(self, data):
        self._data = data

    def __str__(self):
        return '\n' + pformat(self._data)
