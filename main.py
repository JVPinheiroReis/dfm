import sys

from dfm.fs.link import link_to


def main():
    link_to(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
