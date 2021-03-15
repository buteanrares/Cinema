class MovieValidator:

    def validate(self, movie):
        """
        Validator for Movie type object.
        :param movie: Movie type object.
        :return:
        """
        error_messages = []
        if not (isinstance(movie.getID(), int)) or movie.getID() < 0:
            error_messages.append("Movie ID must be a positive integer.")
        if not (isinstance(movie.getRelease(), int)) or movie.getRelease() < 0:
            error_messages.append("Release year must be a positive integer.")
        if movie.getPrice() < 0:
            error_messages.append("Price must be positive.")
        if movie.getInSchedule() not in [True, False]:
            error_messages.append("In schedule must be True / False.")

        if len(error_messages) != 0:
            raise ValueError(error_messages)
