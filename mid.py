class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall_ob):
        self.__hall_list.append(hall_ob)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        stcinema = Star_Cinema()
        stcinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seat_list = [[0 for _ in range(self.__rows)]
                     for _ in range(self.__cols)]
        self.__seats[id] = seat_list

    def book_seats(self, show_id, seats_to_book):
        if show_id not in self.__seats:
            print("Invalid show ID.")
            return

        for seat in seats_to_book:
            row, col = seat
            if not (1 <= row <= self.__rows and 1 <= col <= self.__cols):
                print(f"Invalid seat: ({row}, {col}).")
                continue

            if self.__seats[show_id][row - 1][col - 1] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self.__seats[show_id][row - 1][col - 1] = 1
                print(f"Seat ({row}, {col}) booked for show {show_id}")


    def view_show_list(self):
        for show in self.__show_list:
            print("ID:", show[0], "| Movie:", show[1], "| Time:", show[2])


    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID.")
            return

        print("Available seats for show", show_id)
        for row_idx, row in enumerate(self.__seats[show_id], start=1):
            for col_idx, seat in enumerate(row, start=1):
                if seat == 0:
                    print(f"Seat ({row_idx}, {col_idx})")

        print("Updated seats matrix after booking:")
        for row in self.__seats[show_id]:
            print(row)


    def __repr__(self):
        return f'Hall: {self.__hall_no}, Rows: {self.__rows}, Cols: {self.__cols}'


hall1 = Hall(10, 10, 1)

hall1.entry_show(111, 'Interstellar', '5/05/24')
hall1.entry_show(333, 'The Shawshank Redemption', '5/05/24')

while True:
    print('-----------------------')
    print('-----------------------')
    print('1. View All Shows Today')
    print('2. View Available Seats')
    print('3. Book Tickets')
    print('4. Exit')
    print('-----------------------')
    print('-----------------------')

    user_input = input('Enter Option: ')

    if user_input == '1':
        hall1.view_show_list()
    elif user_input == '2':
        show_id = int(input('Enter show ID: '))
        hall1.view_available_seats(show_id)
    elif user_input == '3':
        show_id = int(input('Enter show ID: '))
        num_tickets = int(input('Enter number of tickets: '))
        seats_to_book = []
        for _ in range(num_tickets):
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            seats_to_book.append((row, col))
        hall1.book_seats(show_id, seats_to_book)
    elif user_input == '4':
        break
    else:
        print('Invalid option. Please try again.')
