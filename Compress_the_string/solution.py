import itertools as it


def compress_string(s):
    """ Compress the string s as (X, c); 
    X occurences  of char 'c' in s"""
    grouped_data = sort_n_group(s)
    for key, group in grouped_data:
        print("({}, {})".format(key, len(list(group))))


def main():
    s = input()
    print(compress_string(s))


def sort_n_group(iterable, key=None):
    """Group sorted 'iterable' on 'key'. """
    return it.groupby(sorted(iterable, key=key), key=key)


if __name__ == "__main__":
    main()
