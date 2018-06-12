from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))

# Data to serve to api
PEOPLE = {
    'Me': {
        'fname': 'Jon',
        'lname': 'Wesneski',
        'timestamp': get_timestamp()
    },
    'Jesus': {
        'fname': 'J',
        'lname': 'C',
        'timestamp': get_timestamp()
    },
    'Pet': {
        'fname': 'Trouble',
        'lname': 'Wesneski',
        'timestamp': get_timestamp()
    }
}


# GET (people.read) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    Returns:
        sorted list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]