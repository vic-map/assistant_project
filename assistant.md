	# Assistant capabilities 
	
	## Working with phonebook
	Our bot can create own phonebook and do many things with it. 
	Below You can find all functions what You can do.
	
	### add-contact
	Command "add-contact" using for add information about contact in phonebook.
	You can 'name', 'phones', 'address', 'birthday' and 'emails' of contact to Your phonebook.
	
	### find-contact
	Command "find-contact" using for finding contact in list of contacts.
	
	### get-contact
	Command "get-contact" using for get information about contact in Your phonebook.
	
	### change-pnone
	Command "change-pnone" using for change phone number of contact.
	
	### add-phone
	Command "add-phone" using for add new phone number to the contact.
	
	### show-all-contacts
	Command "show-all-contacts" using for display list of all contacts.
	
	### show-bdays
	Command "show-bdays" using for display birthdays of all contacts what will be
	in interval less than You print.
	
	### change-contact
	Command "change-contact" using for change information about contact by argument.
	
	### del-contact
	Command "del-contact" using for delete contact in phonebook.
	
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