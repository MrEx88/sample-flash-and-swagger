from datetime import datetime

# 3rd party modules
from flask import (
    make_response,
    abort
)

def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))

# Data to serve to api
PEOPLE = {
    'Wesneski': {
        'fname': 'Jon',
        'lname': 'Wesneski',
        'timestamp': get_timestamp()
    },
    'Simpson': {
        'fname': 'Homer',
        'lname': 'Simpson',
        'timestamp': get_timestamp()
    },
    '47': {
        'fname': 'Agent',
        'lname': '47',
        'timestamp': get_timestamp()
    }
}


# GET (people.read)
def read():
    """This function responds to a request for /api/people
    with the complete lists of people

    Returns:
        sorted list of people"""
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):
    """ Gets the person that matches the name.

    Returns:
        person with same last name"""
    if lname in PEOPLE:
        return PEOPLE[lname]
    else: 
        abort(404, 'Person with last name {lname} not found'.format(lname=lname))


# POST (people.create)
def create(person):
    """Create a new person in the people structure basesd
    on the passed in person data

    Args:
        person - person to create in people structure
    
    Returns:
        201 on success, 406 if person exists"""
    lname = person.get('lname', None)
    fname = person.get('fname', None)
    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            'fname': fname,
            'lname': lname,
            'timestamp': get_timestamp()
        }
        return make_response('{lname} successfully created'.format(lname=lname), 201)
    else:
        abort(406, 'Person with last name {lname} already exists'.format(lname=lname))


# PUT (people.update)
def update(lname, person):
    """Updates a person who matches the last name.
    
    Returns:
        updated person structure or 404 if person dones't exists"""
    new_lname = person.get('lname', None)
    new_fname = person.get('fname', None)
    if lname and lname in PEOPLE:
        PEOPLE[lname] = {
            'fname': new_fname,
            'lname': new_lname,
            'timestamp': get_timestamp()
        }
        return PEOPLE[lname]
    else:
        abort(404, "Person with last name {lname} doesn't exist".format(lname=lname))


# DELETE (people.delete)
def delete(lname):
    """Deletes the person from the people list

    Returns:
        201 on success, 404 if person doesn't exist."""
    try:
        del PEOPLE[lname]
        return make_response('{lname} successfully deleted'.format(lname=lname), 201)
    except KeyError as name:
        abort(404, "Person with last name {lname} doesn't exist".format(lname=lname))