import sys

from trolo import *
from trepiconfig import TEMPLATE_BOARD_ID, PRIMORDIAL_SOUP_LIST_ID, EPIC_LABEL_ID

# verbosity
LOG = True

# process

if len(sys.argv) < 2:
    print('Please pass the name of the new epic.')
    sys.exit(1)

epic_name = ' '.join(sys.argv[1:])

if LOG: print('Creating new epic board ...')
(epic_board_id, epic_board_url) = copy_board(epic_name, TEMPLATE_BOARD_ID)

if LOG: print('Adding epic to main board ...')
epic_ticket_id = new_ticket(PRIMORDIAL_SOUP_LIST_ID, epic_name)

if LOG: print('Labelling ticket as epic ...')
label_ticket(epic_ticket_id, EPIC_LABEL_ID)

if LOG: print('Linking epic ticket and board ...')
add_attachment(epic_ticket_id, epic_board_url)

if LOG: print('Done.')

