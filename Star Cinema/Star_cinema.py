""" 
Author : MD RIAD HOSSEN
DATE : 2/8/2024
"""
class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()

        self.entry_hall(self)

    def _initialize_seats(self):
        for i in range(self._rows):
            self._seats[i] = [0] * self._cols

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self._seats[id] = [[0] * self._cols for _ in range(self._rows)]

    def book_seats(self, show_id, seats):
        try:
            for row, col in seats:
                if 0 <= row < self._rows and 0 <= col < self._cols:
                    if self._seats[show_id][row][col] == 0:
                        self._seats[show_id][row][col] = 1
                    else:
                        raise ValueError("Seat already booked")
                else:
                    raise ValueError("Invalid seat")
        except StopIteration:
            raise ValueError("Invalid show ID")
        

    def view_show_list(self):
        print("id                movie name              time")
        for show in self.__show_list:
            print(f'{show[0]}                 {show[1]}         {show[2]}')



    def view_available_seats(self, show_id):
        try:
            show = next(show for show in self.__show_list if show[0] == show_id)
            print("<----------------Available seats for show", show[0], "--------------->")
            for i, row in enumerate(self._seats[show_id]):
                for j, seat in enumerate(row):
                    if seat == 0:
                        print(f"Seat{i},{j}: Available" ,end="  ")
                    else:
                        print(f"Seat{i},{j}: Booked",end="     ")
                print(end='\n')
        except StopIteration:
            raise ValueError("Invalid show ID")


class Counter:
    def __init__(self, cinema):
        self.cinema = cinema

    def view_all_shows(self):
        print("<----------------All shows running----------------->")
        for hall in self.cinema._Star_Cinema__hall_list:
            hall.view_show_list()

    def view_available_seats(self, show_id):
        for hall in self.cinema._Star_Cinema__hall_list:
            try:
                hall.view_available_seats(show_id)
                return
            except ValueError as e:
                print(e)
        print("Show not found.")

    def book_tickets(self, show_id, seats):
        for hall in self.cinema._Star_Cinema__hall_list:
            try:
                hall.book_seats(show_id, seats)
                print("Booking successful!")
                return
            except ValueError as e:
                print(e)
        print("Show not found or seats are already booked.")





    



