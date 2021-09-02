    # Assistant capabilities

    ## Working with phonebook
    This bot can create own phonebook and do many things with it.

    ## basic syntax
    command --> the command only --> without separators
    command: arg --> command with arg --> separator (between command & arg) --> ': '
    command: arg1, arg2, arg3, arg4 --> separator (between args) --> ', '
    command: arg1, arg2-1; arg2-2; arg3 --> separator (between multiple args) --> '; '
    everything is lowercase
    'space' or empty space used instead missing argument

    ## COMMANDS

    ### add-contact
    	using to add contact information to phonebook.
    attributes:
    	'name', 'phones', 'address', 'birthday' and 'emails'
    	'phones' and 'addresses' can be multiple
    Examples of usage:
    	add-contact: victor, +380(66)000-00-00; +380(66)000-00-11, 15 Rada st., 2021-09-09, sk@gh.net


    ### find-contact
    	using to finding contact by the name in list of phonebook.
    attributes:
    	'name'
    Examples of usage:
    	find-contact: victor

    ### del-contact
    	using for remove contact from phonebook.
    attributes:
    	'name'
    Examples of usage:
    	del-contact: victor

    ### show-all-contacts
    	using for display list of all contacts.
    attributes: -
    Examples of usage:
    	show-all-contacts

    ### change-pnone
    	using for change phone number of contact.
    attributes:
    	'name', 'old phone number', 'new phone number'
    Examples of usage:
    	change-pnone: victor, +380(66)000-00-00; +380(66)000-00-11,

    ### add-phone
    Command "add-phone" using for add new phone number to the contact.


    ### show-bdays
    Command "show-bdays" using for display birthdays of all contacts what will be
    in interval less than You print.


    ## Working with notes
    Our bot can create, change and delete notes.

    ### write-note
    Command "write-note" using for create new note.

    ### del-note
    Command "del-note" using for delete a chosen note.

    ### find-note
    Command "find-note" using for searching note by name.

    ### edit-note
    Command "edit-note" using for editing text of note.

    ### add-note-tag
    Command "add-note-tag" using for adding tag to note.

    ### del-tag
    Command "del-tag" using for delete tag of chosen note.

    ### find_tag
    Command "find_tag" using for searching note by tag.


    ## Files sorting
    Also bot can sort all files in Your Download folder and clean up there!

    ### sort-folder
    Command "sort-folder" using for sort files and folders in chosen folder.
    For sort folder need to know whole Path of folder what You want to sort or
    need to be on one level upper than chosen folder.

    e.g. as argument you can print next:

    ```python
    assistant sort C:\Users\username\folder\folder\folder_what_you_want_to_sort
    ```

    or

    ```python
    assistant sort folder_what_you_want_to_sort
    ```

    if in terminal you alreade at
    "C:\Users\username\folder\folder\"
