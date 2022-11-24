#!/usr/bin/env python3.7

from sources.core import Core


def main():
    try:
        core = Core()
        core.start()
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    main()
