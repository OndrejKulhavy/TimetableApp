# **Alpha One** 🎓 | TimetableApp 📅

Welcome to **Alpha One** | TimetableApp! This project is a school project designed to optimize and create various schedules based on your preferences and constraints.

### Components

1. **Generator 🔄**: This component generates various versions of the given timetable. It explores different permutations and variations, attempting to swap subjects, move classes around, etc. The goal is quantity rather than quality.

2. **Evaluator 🧮**: Evaluates the generated timetable variations based on a set of rules and assigns points. Rules include considerations like avoiding repeated subjects in a day, minimizing movement between floors, ensuring breaks for lunch, and more.

3. **Watchdog ⏱️**: Monitors the execution time. If the program runs beyond a user-defined timeout (default: 3 minutes), it terminates all activities and displays the results, even if not all variations have been evaluated. 
