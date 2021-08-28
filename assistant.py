if __name__ == "__main__":

    
    welcome_text = "---\nHello. I'm CLI bot.\nThe commands are:\nhello; add; change ... ; phone ... ; show all; good bye; close; exit; and '.'\n---"

    print(welcome_text)

    address_book = load_address_book(DEFAULT_ADDRESS_BOOK_PATH)

    while True:
        input_text = input('Input your command: ')
        answer = input_parcer(input_text)
        print(answer)
        if answer == 'Good bye!':
            break
