from schedule import Timetable, Subject, Day
from data import default_timetable


def main():
    setos = set()
    rozvh = default_timetable.get_timetable()
    rozvh2 = Timetable()

    setos.add(rozvh)
    setos.add(rozvh2)

    print(len(setos))


if __name__ == "__main__":
    main()
