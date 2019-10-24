import requests
import sys

from troloconfig import API_KEY, ACCESS_TOKEN

# base URL for all requests
_BASE_URL = 'https://api.trello.com/1'


# build a request URL from a command and keyword arguments
def build_request_url(cmd, **kwargs):
    url = '%s/%s?key=%s&token=%s' % (_BASE_URL, cmd, API_KEY, ACCESS_TOKEN)
    for k in kwargs:
        url = url + '&%s=%s' % (k, kwargs[k])
    return url


# to get all my boards; returns JSON response
def get_boards(member):
    result = requests.get(build_request_url('members/%s/boards' % member))
    return result.json()


# to get one specific board; returns JSON response
def get_board(board_id):
    result = requests.get(build_request_url('boards/%s' % board_id))
    return result.json()


# to create a new board with a given name as a clone of the source - returns the new board's ID and short URL
def copy_board(name, source):
    result = requests.post(build_request_url('boards/', name = name, idBoardSource = source))
    json = result.json()
    return (json['id'], json['shortUrl'])


# to retrieve all lists from a board; returns JSON response
def get_board_lists(board_id):
    result = requests.get(build_request_url('boards/%s/lists' % board_id))
    return result.json()


# to get a board's labels; returns JSON response
def get_board_labels(board_id):
    result = requests.get(build_request_url('boards/%s/labels' % board_id))
    return result.json()


# to create a new ticket in a given board and list, with a given name; returns the ticket ID
def new_ticket(list_id, name):
    result = requests.post(build_request_url('cards', idList = list_id, name = name))
    json = result.json()
    return json['id']


# to label a ticket (the label is given by colour name)
def label_ticket(ticket_id, label_id):
    requests.post(build_request_url('cards/%s/idLabels' % ticket_id, value = label_id))


# to add an attachment (URL only) to a ticket
def add_attachment(ticket_id, attachment_url):
    requests.post(build_request_url('cards/%s/attachments' % ticket_id, url = attachment_url))


# to get the number of tickets in a given list
def get_list_tickets(list_id):
    result = requests.get(build_request_url('lists/%s/cards' % list_id))
    return result.json()

