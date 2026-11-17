# Grading for the Lab Internal Exam.
#
# Edit the settings below, push, and update the dojo. The admin Grades page
# (/dojo/<dojo>/admin/grades) recalculates every time it loads, so you can
# change marks after the exam is over.

# Marks for solving each challenge, keyed by challenge id from dojo.yml.
# Solving a challenge earns its full marks. Not solving it earns 0.
# Starting values follow the question paper: Section A = 1 mark, Section B = 3.
MARKS = {
    "apple": 1,         # Q1  Access Control level1
    "kiwi": 1,          # Q2  Listen
    "banana": 1,        # Q3  Access Control level4 (SETUID)
    "mango": 1,         # Q4  Firewall 1
    "papaya": 1,        # Q5  Access Control level6
    "grapes": 2,        # Q6  Scan 2
    "pineapple": 2,     # Q7  Access Control level16 (Bell-LaPadula)
    "tomato": 2,        # Q8  Sniffing Cookies
    "guava": 2,         # Q9  Access Control level12
    "dragon-fruit": 2,  # Q10 Intercept
}

MODULE_ID = "fruit-market"

# Exam window (IST). Only solves at or after EXAM_START and at or before
# EXAM_END earn marks; solves outside the window score 0. ISO 8601 with the
# +05:30 offset = IST. Set either to None to remove that bound.
EXAM_START = "2026-11-18T10:00:00+05:30"
EXAM_END   = "2026-11-18T12:00:00+05:30"

#
# Grading logic: you shouldn't need to change anything below.
#

import datetime

IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30), "IST")


def parse_time(value):
    if not value:
        return None
    return datetime.datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def fmt(value):
    return f"{value:g}"


def grade(data):
    if any(field not in data for field in ["solves", "modules", "course"]):
        return None

    start = parse_time(EXAM_START)
    end = parse_time(EXAM_END)

    first_solve = {}
    for solve in data["solves"]:
        if solve["module_id"] != MODULE_ID:
            continue
        solved_at = parse_time(solve["timestamp"])
        challenge_id = solve["challenge_id"]
        if challenge_id not in first_solve or solved_at < first_solve[challenge_id]:
            first_solve[challenge_id] = solved_at

    module = next((m for m in data["modules"] if m["id"] == MODULE_ID), {})

    assignments = []
    earned_total = 0
    max_total = 0
    for challenge in module.get("challenges", []):
        challenge_id = challenge["id"]
        max_marks = MARKS.get(challenge_id, 0)
        max_total += max_marks

        solved_at = first_solve.get(challenge_id)
        earned = 0
        if solved_at is None:
            status = "Not solved"
        elif start and solved_at < start:
            status = f"Solved before window ({solved_at.astimezone(IST):%d %b %H:%M} IST)"
        elif end and solved_at > end:
            status = f"Solved after window ({solved_at.astimezone(IST):%d %b %H:%M} IST)"
        else:
            earned = max_marks
            status = f"Solved at {solved_at.astimezone(IST):%H:%M} IST"
        earned_total += earned

        # Key order matters: the admin "Download CSV" button reads these
        # five columns by position (name, deadline, weight, progress, credit).
        assignments.append({
            "name": challenge.get("name", challenge_id),
            "deadline": EXAM_END or "-",
            "marks": max_marks,
            "progress": f"{status}: {fmt(earned)}/{fmt(max_marks)}",
            "credit": earned / max_marks if max_marks else 0,
        })

    return {
        "overall": {
            "credit": earned_total / max_total if max_total else 0,
            "letter": f"{fmt(earned_total)} / {fmt(max_total)} marks",
        },
        "assignments": assignments,
    }
