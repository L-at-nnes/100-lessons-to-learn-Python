"""Lesson 12 - Object Basics (Solution)

Reference solution for the Mentor Dashboard exercise.
"""

class Mentee:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.sessions_completed = 0
        self.total_minutes = 0

    def record_session(self, duration):
        self.sessions_completed += 1
        self.total_minutes += duration

    def progress(self):
        return (
            f"{self.name} ({self.level}) -> "
            f"sessions: {self.sessions_completed}, minutes: {self.total_minutes}"
        )


class Mentor:
    def __init__(self, name):
        self.name = name
        self.mentees = []

    def add_mentee(self, mentee):
        self.mentees.append(mentee)

    def report(self):
        print(f"Mentor: {self.name}")
        for mentee in self.mentees:
            print(" -", mentee.progress())


class Session:
    def __init__(self, mentor, mentee, duration, topic):
        self.mentor = mentor
        self.mentee = mentee
        self.duration = duration
        self.topic = topic

    def describe(self):
        return (
            f"Session: {self.mentor.name} with {self.mentee.name} "
            f"for {self.duration} min on {self.topic}"
        )


# Demonstration
mentee_a = Mentee("Alex", "beginner")
mentee_b = Mentee("Riley", "intermediate")

mentor = Mentor("Sam")
mentor.add_mentee(mentee_a)
mentor.add_mentee(mentee_b)

session1 = Session(mentor, mentee_a, 45, "control flow")
session2 = Session(mentor, mentee_b, 30, "file handling")

print(session1.describe())
print(session2.describe())

mentee_a.record_session(45)
mentee_b.record_session(30)
mentee_b.record_session(35)

mentor.report()
