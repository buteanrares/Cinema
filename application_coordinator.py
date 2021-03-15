from Tests import main_test
from domain.movie_validator import MovieValidator
from domain.reservation_validator import ReservationValidator
from domain.clientcard_validator import ClientcardValidator
from repository.generic_repository import GenericFileRepository
from service.cinema_service import MovieService
from service.cinema_service import ReservationService
from service.cinema_service import ClientcardService
from service.UndoService import UndoService
from user_interface.console import Console


def main():
    movie_repository = GenericFileRepository('movies.pickle')
    reservation_repository = GenericFileRepository('reservations.pickle')
    clientcard_repository = GenericFileRepository('clientcards.pickle')

    movie_validator = MovieValidator()
    reservation_validator = ReservationValidator()
    clientcard_validator = ClientcardValidator()

    undo_service = UndoService()

    movie_service = MovieService(movie_repository, movie_validator,
                                 reservation_repository, undo_service)
    reservation_service = ReservationService(reservation_repository,
                                             reservation_validator,
                                             movie_repository,
                                             clientcard_repository,
                                             undo_service)
    clientcard_service = ClientcardService(clientcard_repository,
                                           clientcard_validator,
                                           reservation_repository,
                                           undo_service)

    cinema_ui = Console(movie_service, reservation_service, clientcard_service,
                        undo_service)
    cinema_ui.run_console()


main_test.run_tests()
main()
