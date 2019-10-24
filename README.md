# Trolo

Trolo is a little cheesy Python utility that supports Trello REST API calls. It
is configured with a file `troloconfig.py` that needs to define the following
two values:

*   `API_KEY`: the API key for accessing Trello, which can be obtained from the
    [Trello developer site](https://trello.com/app-key); and

*   `ACCESS_TOKEN`: the Trello access token, obtained from the same site.

Both are to be provided as strings.

# Trepic

## Why?

I organise my personal work in Kanban style. I have a main Trello board that has
several lists, including "backlog", "in progress", and "done", and also a
"primordial soup" that contains raw ideas that haven't yet been prioritised into
the backlog.

The main board can contain two different kinds of tickets: _oddballs_, which are
one-off tasks with little or no inherent complexity; and _epics_, which
themselves contain tasks. Each epic ticket has a Trello board attached to it
that has all the tickets constituting it flow through it. The board is basically
the same for all epics, with a standard set of lists.

## So What?

Every time I create a new epic, I have to create a new board for it, add a
ticket to the main board, attach the epic board to that ticket, and label the
ticket as en epic. This calls for automation. Hence, `trepic`.

Running the `trepic.py` Python script; for instance, with the following bash
script, creates a new epic ticket and board from a template board.

    #!/bin/bash
    (cd whereverYouPutThis/trolo; python trepic.py $@)

The `trepic.py` script relies on `trolo.py`. It requires configuration in a file
named `trepiconfig.py`, which needs to provide the following values:

*   `TEMPLATE_BOARD_ID`: the Trello ID of the epic board template;

*   `PRIMORDIAL_SOUP_LIST_ID`: the Trello ID of the primordial soup list on the
    main board (in other words, the list on the main board where the newly
    created epic ticket should be placed); and

*   `EPIC_LABEL_ID`: the Trello ID of the label that is put on epic tickets in
    the main board.

All of these IDs can be found out by fiddling with the Trello REST API on the
[Trello API documentation
pages](https://developers.trello.com/docs/api-introduction). I'll leave it to
the reader to figure that out.

