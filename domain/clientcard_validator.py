import datetime


class ClientcardValidator:

    def validate(self, clientcard):
        error_messages = []
        if not (isinstance(clientcard.getID(), int)) or clientcard.getID() < 0:
            error_messages.append("ID must be a positive integer.")
        if not isinstance(clientcard.getCNP(), int):
            error_messages.append("CNP must be a positive integer.")
        if clientcard.getPoints() < 0:
            error_messages.append("Clientcard points must be at least 0.")
        try:
            time = str(clientcard.getBirthDate())
            time=datetime.datetime.strptime(time,'%d/%m/%Y')
            time=str(clientcard.getRegisterDate())
            time = datetime.datetime.strptime(time, '%d/%m/%Y')
        except ValueError:
            error_messages.append("Clientcard dates must be 'dd/mm/yyyy'")

        if len(error_messages) != 0:
            raise ValueError(error_messages)
