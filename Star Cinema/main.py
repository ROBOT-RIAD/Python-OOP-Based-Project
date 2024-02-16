from Star_cinema import *

def main():
    cinema = Star_Cinema()
    hall1 = Hall(rows=4, cols=4, hall_no=1)
    hall1.entry_show(id=1, movie_name="The Matrix     ", time="19:00")
    hall1.entry_show(id=2, movie_name="Inception      ", time="21:00")

    counter = Counter(cinema)
    print('<-----------------Option--------------------->')
    print('Options 1: view all shows')
    print('Options 2: view available seats')
    print('Options 3: Book tickets ')
    print('Options 4: End program')

    while True:
        options =int(input())
        if options == 1:
            counter.view_all_shows()
            print('\n')
        elif options == 2:
            counter.view_available_seats(1)
            print('\n')
        elif options == 3:
            show_id=int(input('input shou id :'))
            tup=[]
            print('enter column and row :')
            x, y = map(int, input().split())
            tup.append((x, y))
            counter.book_tickets(show_id,tup)
        elif options == 4:
            break

if __name__=='__main__':
    main()