import argparse


def sizeof_fmt(num: int, suffix: str = 'B') -> str:
    """
    Return file size in human readable format.
    :param num:
    :param suffix:
    :return: The human readable string of file size
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
