from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Subject:
    """
    A data class representing a subject with details such as name, teachers, classroom, and lab information.
    """

    name: str
    """str: The name of the subject."""

    teachers: str
    """str: The teachers responsible for the subject."""

    classroom_id: str
    """str: The identifier of the classroom where the subject is taught."""

    classroom_floor: int
    """int: The floor number of the classroom where the subject is taught."""

    is_lab: bool = False
    """bool: Indicates whether the subject involves a laboratory component. Defaults to False."""

    def __post_init__(self):
        """
        Custom initialization method to check and raise a ValueError if classroom_floor is less than 0.
        """
        if self.classroom_floor < 0:
            raise ValueError("classroom_floor cannot be less than 0")
