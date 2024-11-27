class UserInputValidator:
    def __init__(self):
        pass

    def validate_positive_integers(self, inputs):
        """
        Validates a list of strings and returns a list of valid positive integers.

        :param inputs: List of strings
        :return: List of valid positive integers
        """
        valid_integers = []
        for item in inputs:
            if item.isdigit() and int(item) > 0:
                valid_integers.append(int(item))
        return valid_integers

    def display_validation_message(self, inputs):   
    """
    Displays a message with the number of validated items.

    :param inputs: List of inputs validated
    """
    print(f"Validation complete: {len(inputs)} inputs were checked.")
