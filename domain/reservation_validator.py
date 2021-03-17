import datetime


class ReservationValidator:
    # Validator class for Reservation objects

    def validate(self, reservation):
        """Validation method for a reservation object

        :param reservation: reservation obj. to validate
        :type reservation: Reservation
        :raises ValueError: if reservation obj. is not valid
        """

        error_messages = []
        if not (isinstance(reservation.getID(),
                           int)) or reservation.getID() < 0:
            error_messages.append("ID must be a pozitive integer.")
        try:
            time = str(reservation.getTime())
            time = datetime.datetime.strptime(time, '%H:%M')
        except ValueError:
            error_messages.append("Invalid time. 'HH:MM'")
        try:
            date = str(reservation.getDate())
            date = datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            error_messages.append("Invalid date. 'dd/mm/yyyy'")

        if len(error_messages) != 0:
            raise ValueError(error_messages)
