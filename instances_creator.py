from user_input_validator import UserInputValidator

# Create instances
validator1 = UserInputValidator()
validator2 = UserInputValidator()

from user_input_validator import UserInputValidator

# Create instances
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Input lists
inputs1 = ["10", "-5", "apple", "42"]
inputs2 = ["20", "abc", "0", "100"]

# Validate inputs
validated1 = validator1.validate_positive_integers(inputs1)
validated2 = validator2.validate_positive_integers(inputs2)

# Display results
print("Validator 1:", validated1)
validator1.display_validation_message(inputs1)

print("Validator 2:", validated2)
validator2.display_validation_message(inputs2)
