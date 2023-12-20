"""
This module provides a default schedule and functions to retrieve information from it.

Classes:
    - Subject: Represents a subject with attributes like name, lecturer, room, etc.
    - Timetable: Represents a weekly schedule with subjects scheduled for each day.

Functions:
    - get_timetable(): Returns a default schedule with sample subjects for each day.
    - get_all_subjects(): Returns a list of all non-null subjects from the default schedule.
"""

import array

from src.schedule.subject import Subject
from src.schedule.timetable import Timetable
from src.schedule.days import Day


def get_timetable() -> Timetable:
    """
    Get a default schedule with sample subjects for each day of the week.

    Returns:
        Timetable: An instance of the Timetable class with default subjects.
    """
    timetable: dict = {
        Day.MONDAY:    [
            Subject("WA", "Mgr. Jan Pavlát", "17a", 3, is_lab=True),
            Subject("WA", "Mgr. Jan Pavlát", "17a", 3, is_lab=True),
            Subject("C", "MUDr. Kristina Studénková", "24", 4),
            Subject("A", "Ing. Tomáš Juchelka", "5a", 1),
            Subject("M", "Mgr. Eva Neugebauerová", "24", 4),
            None,
            Subject("PV", "Mgr. Alena Reichlová & Ing. Ondřej Mandík", "18b", 3, is_lab=True),
            Subject("PV", "Mgr. Alena Reichlová & Ing. Ondřej Mandík", "18b", 3, is_lab=True),
            None,
            None
        ],
        Day.TUESDAY:   [
            Subject("M", "Mgr. Eva Neugebauerová", "24", 4),
            Subject("TP", "Ing. Vít Nohejl", "24", 4),
            Subject("DS", "Ing. Ivana Kantnerová", "18a", 3, is_lab=True),
            Subject("DS", "Ing. Ivana Kantnerová", "18a", 3, is_lab=True),
            Subject("A", "Mgr. Eva Neugebauerová", "24", 4),
            Subject("AM", "Ing. Filip Kallmünzer", "24", 4),
            None,
            Subject("TV ", "Mgr. Eva Neugebauerová", "TV", 0),
            None,
            None
        ],
        Day.WEDNESDAY: [
            Subject("PIS", "Ing. Lucie Brčáková", "24", 4),
            Subject("C", "MUDr. Kristina Studénková", "24", 4),
            Subject("CIT", "Mgr. Jakub Mazuch", "17b", 3, is_lab=True),
            Subject("CIT", "Mgr. Jakub Mazuch", "17b", 3, is_lab=True),
            Subject("AM", "Ing. Filip Kallmünzer", "24", 4),
            Subject("M", "Mgr. Eva Neugebauerová", "24", 4),
            Subject("DS", "Ing. Ivana Kantnerová", "24", 4),
            None,
            None,
            None
        ],
        Day.THURSDAY:  [
            Subject("WA", "Mgr. Jan Pavlát", "24", 4),
            Subject("M", "Mgr. Eva Neugebauerová", "24", 4),
            Subject("PIS", "Ing. Lucie Brčáková", "24", 4),
            Subject("PV", "Mgr. Alena Reichlová", "24", 4),
            Subject("A", "Ing. Tomáš Juchelka", "5b", 1),
            Subject("C", "MUDr. Kristina Studénková", "24", 4),
            Subject("PSS", "Ing. Lukáš Masopust", "24", 4),
            None,
            None,
            None
        ],
        Day.FRIDAY:    [
            None,
            Subject("PIS", "Ing. Lucie Brčáková", "19a", 3, is_lab=True),
            Subject("PIS", "Ing. Lucie Brčáková", "19a", 3, is_lab=True),
            Subject("A", "Ing. Tomáš Juchelka", "24", 4),
            Subject("TV", "Mgr. Pavel Lopocha", "TV", 0),
            Subject("PSS", "Ing. Lukáš Masopust", "8a", 1, is_lab=True),
            Subject("PSS", "Ing. Lukáš Masopust", "8a", 1, is_lab=True),
            None,
            None,
            None
        ]
    }
    return Timetable(timetable)
