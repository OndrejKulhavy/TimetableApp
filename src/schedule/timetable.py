from tabulate import tabulate
from src.schedule.days import Day
from src.schedule.subject import Subject


class Timetable:
    """
    A class representing a timetable that organizes subjects for each day of the week.
    """

    SUBJECTS_PER_DAY = 10
    """int: The maximum number of subjects allowed per day."""

    def __init__(self, subjects=None, rating: int = 0):
        """
        Initializes a Timetable instance.

        Parameters:
        - subjects (Optional[Dict[Day, List[Subject]]]): A dictionary mapping each day to a list of subjects.
        - rating (int): The rating of the timetable. Defaults to 0.
        """
        if subjects is None:
            subjects = {day: [] for day in Day}
        self.subjects = subjects
        """Dict[Day, List[Subject]]: A dictionary representing subjects scheduled for each day."""
        self.rating = rating
        """int: The rating of the timetable."""

    def append_subject_by_day(self, day: Day, subject: Subject) -> None:
        """
        Adds a subject to the timetable for a specific day.

        Parameters:
        - day (Day): The day of the week.
        - subject (Subject): The subject to be added.

        Raises:
        - ValueError: If the day is invalid or if the number of subjects per day is exceeding the maximum value.
        """
        if day not in Day:
            raise ValueError(f"Invalid day. Accepted values are: {', '.join(day.value for day in Day)}")

        if len(self.subjects[day]) == self.SUBJECTS_PER_DAY:
            raise ValueError(f"You can't add more than {self.SUBJECTS_PER_DAY} subjects per day.")

        self.subjects[day].append(subject)

    def get_all_subjects(self) -> list:
        """
        Gets a list of all subjects scheduled in the timetable.

        Returns:
        - List[Subject]: A list of all subjects in the timetable.
        """
        return [subject for day in Day for subject in self.subjects[day] if subject]

    def __getitem__(self, day: Day) -> list[Subject]:
        """
        Gets the list of subjects scheduled for a specific day.

        Parameters:
        - day (Day): The day of the week.

        Raises:
        - ValueError: If the day is invalid.

        Returns:
        - List[Subject]: A list of subjects scheduled for the specified day.
        """
        if day not in Day:
            raise ValueError(f"Invalid day. Accepted values are: {', '.join(day.value for day in Day)}")
        return self.subjects[day]

    def __setitem__(self, day: Day, subjects: list[Subject]):
        """
        Sets the list of subjects for a specific day.

        Parameters:
        - day (Day): The day of the week.
        - subjects (List[Subject]): The list of subjects to set.

        Raises:
        - ValueError: If the day is invalid or if the number of subjects provided is not equal to SUBJECTS_PER_DAY.
        """
        if day not in Day:
            raise ValueError(f"Invalid day. Accepted values are: {', '.join(day.value for day in Day)}")
        if len(subjects) != self.SUBJECTS_PER_DAY:
            raise ValueError(f"Invalid subjects. You must provide exactly {self.SUBJECTS_PER_DAY} subjects.")
        self.subjects[day] = subjects

    def __contains__(self, item):
        """
        Checks if a subject is present in the timetable.

        Parameters:
        - item: The subject to check.

        Returns:
        - bool: True if the subject is present, False otherwise.
        """
        return item in self.subjects.values()

    def __eq__(self, other):
        """
        Checks if two timetables are equal.

        Parameters:
        - other (Timetable): The other timetable to compare.

        Returns:
        - bool: True if the timetables are equal, False otherwise.
        """
        return self.subjects == other.subjects

    def __hash__(self):
        """
        Generates a hash value for the timetable.

        Returns:
        - int: The hash value of the timetable.
        """
        return hash(self.subjects)

    def __str__(self):
        """
        Returns a string representation of the timetable.

        Returns:
        - str: A formatted string representation of the timetable.
        """
        headers = ["Day"] + [f"{i}" for i in range(1, 11)]
        table_data = [[day.value] + [subject.name if subject else "None" for subject in self.subjects[day]] for day in
                      Day]
        return tabulate(table_data, headers, tablefmt="github")
