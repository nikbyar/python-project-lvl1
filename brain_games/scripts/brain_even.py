#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.even import even_answer


def main():
    engine(even_answer)


if __name__ == '__main__':
    main()
