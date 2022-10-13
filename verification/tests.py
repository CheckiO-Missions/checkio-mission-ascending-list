"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[-5, 10, 99, 123456]],
            "answer": True
        },
        {
            "input": [[99]],
            "answer": True
        },
        {
            "input": [[4, 5, 6, 7, 3, 7, 9]],
            "answer": False
        },
        {
            "input": [[]],
            "answer": True
        },
        {
            "input": [[1, 1, 1, 1]],
            "answer": False
        },
        {
            "input": [[1, 3, 3, 5]],
            "answer": False,
            "explanation": "3 == 3, so it is not __strictly__  ascending"
        }
    ],
    "Extra": [
        {
            "input": [[-5, -6]],
            "answer": False
        },
        {
            "input": [[1, 2, 3]],
            "answer": True
        },
        {
            "input": [[1, 1]],
            "answer": False
        },
        {
            "input": [[-1, 0, 1]],
            "answer": True
        },
        {
            "input": [[1, 0, 1]],
            "answer": False
        },
        {
            "input": [[1, 2, 4, 3, 5]],
            "answer": False
        }
    ]
}
