import datetime


class ClientcardValidator:
    # Validator class for clientcard objects

    def validate(self, clientcard):
        """Validation method for a clientcard object

        :param clientcard: clientcard obj. to validate
        :type clientcard: Clientcard
        :raises ValueError: if clientcard obj. is not valid
        """

        error_messages = []
        if not (isinstance(clientcard.getID(), int)) or clientcard.getID() < 0:
            error_messages.append("ID must be a positive integer.")
        if not isinstance(clientcard.getCNP(), int):
            error_messages.append("CNP must be a positive integer.")
        if clientcard.getPoints() < 0:
            error_messages.append("Clientcard points must be at least 0.")
        try:
            time = str(clientcard.getBirthDate())
            time = datetime.datetime.strptime(time, '%d/%m/%Y')
            time = str(clientcard.getRegisterDate())
            time = datetime.datetime.strptime(time, '%d/%m/%Y')
        except ValueError:
            error_messages.append(
                "Clientcard date format must be 'dd/mm/yyyy'")

        if len(error_messages) != 0:
            raise ValueError(error_messages)
