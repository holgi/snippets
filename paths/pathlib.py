""" some helpers for working with the pathlib module """


import pathlib
import stat


def is_hidden(path_like):
    """ returns True if a path appears to be hidden

    This will not fit all possibilities, but the majorities of cases
    """
    item_path = pathlib.Path(path_like)
    # check for POSIX-like dot convention
    if item_path.name.startswith("."):
        return True
    # check for windows hidden attribute
    # "st_file_attributes" only available on windows
    file_attrs = item_path.stat()
    st_file_attrs = getattr(file_attrs, "st_file_attributes", 0)
    return bool(st_file_attrs & stat.FILE_ATTRIBUTE_HIDDEN)


def recursive_iterdir(directory, include_hidden=False):
    """ like pathlib.Path.iterdir, but recurses into directories """
    dir_path = pathlib.Path(directory)
    content = dir_path.iterdir()
    if not include_hidden:
        content = (item for item in content if not is_hidden(item))
    for item in content:
        if item.is_dir():
            yield from recursive_iterdir(item)
        yield item
