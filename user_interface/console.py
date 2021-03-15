from service import cinema_service
from service import UndoService


class Console:
    def __init__(self, movies_service, reservations_service,
                 clientcards_service, undo_service: UndoService):
        self.__movies_service = movies_service
        self.__reservations_service = reservations_service
        self.__clientcards_service = clientcards_service
        self.__undo_service = undo_service

    def run_console(self):
        self.__show_menu()
        while True:
            option = input('Select option: ')
            if option == '1':
                self.__handle_addMovie()
            elif option == '2':
                self.__handle_addReservation()
            elif option == '3':
                self.__handle_addClientcard()
            elif option == '4':
                self.__handle_updateMovie()
            elif option == '5':
                self.__handle_updateReservation()
            elif option == '6':
                self.__handle_updateClientcard()
            elif option == '7':
                self.__handle_deleteMovie()
            elif option == '8':
                self.__handle_deleteReservation()
            elif option == '9':
                self.__handle_deleteClientcard()
            elif option == '10':
                self.__handle_showAllMovies()
            elif option == '11':
                self.__handle_showAllReservations()
            elif option == '12':
                self.__handle_showAllClientcards()
            elif option == '13':
                self.__handle_search()
            elif option == '14':
                self.__handle_showResBetween()
            elif option == '15':
                self.__handle_showClientcardsByPts()
            elif option == '16':
                self._handle_showMoviesByReservations()
            elif option == '17':
                self.__handle_deleteReservationsInInterval()
            elif option == '18':
                self.__handle_birthdayBonus()
            elif option == '19':
                self.__handle_populateMovies()
            elif option == '20':
                self.__handle_populateReservations()
            elif option == '21':
                self.__handle_populateClientcards()
            elif option == '22':
                if not self.__undo_service.undo():
                    print("Nothing to undo.")
            elif option == '23':
                if not self.__undo_service.redo():
                    print("Nothing to redo.")
            elif option == '24':
                self.__handle_binary_search()
            elif option == '25':
                self.__handle_permutate_movies()
            else:
                print("Command does not exist.")

    @staticmethod
    def __show_menu():
        print('''
        1. Add movie
        2. Add reservation
        3. Add clientcard
        4. Update movie
        5. Update reservation
        6. Update clientcard
        7. Delete movie
        8. Delete reservation
        9. Delete clientcard
        10. Show all movies
        11. Show all reservations
        12. Show all clientcards
        13. Search movie and clients (title/firstname/lastname/CNP/etc.)
        14. Show all reservations between time (HH:MM - HH:MM)
        15. Show clientcards in descending order by points
        16. Show movies in descending order by reservations made
        17. Delete all reservations by in interval (dd/mm/yyyy - dd/mm/yyyy)
        18. Clientcard birthday bonus
        19. Populate movies
        20. Populate reservations
        21. Populate clientcards
        22. Undo
        23. Redo
        24. Movie binary search
        25. Permutate movies
        ''')

    def __handle_addMovie(self):
        try:
            movieID = int(input('ID: '))
            movieTitle = input('Movie title: ')
            movieRelease = int(input('Movie release year: '))
            moviePrice = float(input('Give movie price: '))
            movieInSchedule = input('Give movie in schedule: ')
            if movieInSchedule == "True":
                movieInSchedule = True
            else:
                movieInSchedule = False
            self.__movies_service.addMovie(movieID, movieTitle, movieRelease,
                                           moviePrice, movieInSchedule)
            print('Movie added.')
        except KeyError:
            print('ID already exists!')
        except ValueError as ve:
            print('Error', ve)

    def __handle_addReservation(self):
        try:
            reservationID = int(input("ID: "))
            reservationMovieId = int(input("Movie ID: "))
            reservationClientcardId = int(input("Clientcard ID: "))
            reservationDate = input("Give date (dd/mm/yyyy): ")
            reservationTime = input("Give time (HH:MM): ")
            if self.__movies_service.isInSchedule(reservationMovieId):
                self.__reservations_service.addReservation(
                    reservationID, reservationMovieId, reservationClientcardId,
                    reservationDate, reservationTime)
                print("Reservation added.")
            else:
                print("That movie is not in schedule.")
        except KeyError:
            print("ID already exists!")
        except ValueError as ve:
            print('Error', ve)

    def __handle_addClientcard(self):
        try:
            clientcardID = int(input("ID: "))
            clientcardFirstName = input("Firstname: ")
            clientcardLastname = input("Lastname: ")
            clientcardCNP = int(input("CNP: "))
            clientcardBirthDate = input("Birthdate (dd/mm/yyyy): ")
            clientcardRegisterDate = input("Registerdate (dd/mm/yyyy): ")
            clientcardPoints = int(input("Points: "))
            self.__clientcards_service.addClientcard(
                clientcardID, clientcardFirstName, clientcardLastname,
                clientcardCNP, clientcardBirthDate, clientcardRegisterDate,
                clientcardPoints)
            print('Clientcard added.')
        except KeyError:
            print("ID already exists.")
        except ValueError as ve:
            print("Error", ve)

    def __handle_updateMovie(self):
        try:
            movieID = int(input('ID: '))
            movieTitle = input('Movie title: ')
            movieRelease = int(input('Movie release year: '))
            moviePrice = float(input('Give movie price: '))
            movieInSchedule = input('Give movie in schedule: ')
            if movieInSchedule == "True":
                movieInSchedule = True
            else:
                movieInSchedule = False
            self.__movies_service.updateMovie(movieID, movieTitle,
                                              movieRelease, moviePrice,
                                              movieInSchedule)
            print('Movie updated.')
        except ValueError as ve:
            print('Error', ve)

    def __handle_updateReservation(self):
        try:
            reservationID = int(input("ID: "))
            reservationMovieId = int(input("Movie ID: "))
            reservationClientcardId = int(input("Clientcard ID: "))
            reservationDate = input("Give date (dd/mm/yyyy): ")
            reservationTime = input("Give time (HH:MM): ")
            self.__reservations_service.updateReservation(
                reservationID, reservationMovieId, reservationClientcardId,
                reservationDate, reservationTime)
            print("Reservation updated.")
        except ValueError as ve:
            print('Error', ve)

    def __handle_updateClientcard(self):
        try:
            clientcardID = int(input("ID: "))
            clientcardFirstName = input("Firstname: ")
            clientcardLastname = input("Lastname: ")
            clientcardCNP = int(input("CNP: "))
            clientcardBirthDate = input("Birthdate (dd/mm/yyyy): ")
            clientcardRegisterDate = input("Registerdate (dd/mm/yyyy): ")
            clientcardPoints = int(input("Points: "))
            self.__clientcards_service.updateClientcard(
                clientcardID, clientcardFirstName, clientcardLastname,
                clientcardCNP, clientcardBirthDate, clientcardRegisterDate,
                clientcardPoints)
            print('Clientcard updated.')
        except ValueError as ve:
            print('Error', ve)

    def __handle_deleteMovie(self):
        movie_id = input(
            "Give movie ID to delete (all to deletee all movies): ")
        if movie_id != "all":
            movie_id = int(movie_id)
        self.__movies_service.deleteMovie(movie_id)
        print("Movie deleted.")

    def __handle_deleteReservation(self):
        reservation_id = input(
            "Give reservation ID to delete (all to delete all reservations): ")
        if reservation_id != "all":
            reservation_id = int(reservation_id)
        self.__reservations_service.deleteReservation(reservation_id)
        print("Reservation deleted.")

    def __handle_deleteClientcard(self):
        clientcard_id = input(
            "Give clientcard ID to delete (all to delete all clientcards): ")
        if clientcard_id != "all":
            clientcard_id = int(clientcard_id)
        self.__clientcards_service.deleteClientcard(clientcard_id)
        print("Clientcard deleted.")

    def __handle_showAllMovies(self):
        moviesList = self.__movies_service.showAllMovies()
        for movie in moviesList:
            print(str(movie))

    def __handle_showAllReservations(self):
        resList = self.__reservations_service.showAllReservations()
        for res in resList:
            print(str(res))

    def __handle_showAllClientcards(self):
        ccList = self.__clientcards_service.showAllClientcards()
        for cc in ccList:
            print(str(cc))

    def __handle_search(self):
        toSearch = input("What to look for?\n")
        movieList = self.__movies_service.searchMovie(toSearch)
        ccList = self.__clientcards_service.searchClientcard(toSearch)
        for movie in movieList:
            print(str(movie))
        for cc in ccList:
            print(str(cc))

    def __handle_showResBetween(self):
        timeLeft = input("First time (HH:MM):  ")
        timeRight = input("Second time (HH:MM): ")
        resList = self.__reservations_service.showReservationsInInterval(
            timeLeft, timeRight)
        for res in resList:
            print(str(res))

    def __handle_showClientcardsByPts(self):
        ccList = self.__clientcards_service.showClientcardsByPts()
        for cc in ccList:
            print(str(cc))

    def _handle_showMoviesByReservations(self):
        result = self.__movies_service.showMoviesByReservations()
        for movie in result:
            print(movie[0], " ---Number of res. made: ", movie[1])

    def __handle_deleteReservationsInInterval(self):
        dateLeft = input("First date (dd/mm/yyyy): ")
        dateRight = input("Second date (dd/mm/yyyy): ")
        resList = self.__reservations_service.deleteReservationsInInterval(
            dateLeft, dateRight)
        for res in resList:
            print(str(res))

    def __handle_birthdayBonus(self):
        dateLeft = input("First date (dd/mm/yyyy): ")
        dateRight = input("Second date (dd/mm/yyyy): ")
        value = int(input("Value to increment: "))
        self.__clientcards_service.giveBirthdayBonus(value, dateLeft,
                                                     dateRight)
        print("Bonus given.")

    def __handle_populateMovies(self):
        number = int(input("Give number to populate: "))
        self.__movies_service.populateMovies(number)

    def __handle_populateClientcards(self):
        number = int(input("Give number to populate: "))
        self.__clientcards_service.populateClientcards(number)

    def __handle_populateReservations(self):
        number = int(input("Give number to populate: "))
        self.__reservations_service.populateReservations(number)

    def __handle_binary_search(self):
        try:
            _id = int(input("The wanted id:  "))
            if self.__movies_service.search_id(_id):
                print("There is a movie with that id.")
            else:
                print("There is no movie with such id.")
        except ValueError as ve:
            print(ve)

    def __handle_permutate_movies(self):
        list_of_permuted_movies = self.__movies_service.get_movie_permutations(
        )
        for movies_list in list_of_permuted_movies:
            for movie in movies_list:
                print(movie)
            print("\n\n")
