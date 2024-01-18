
def pytest_configure(config):
    marks = [
        "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
        "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five",
        "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty"
    ]
    
    for number, mark in enumerate(marks, start=1):
        config.addinivalue_line('markers', f'{mark}: mark test as {number} challenge')
