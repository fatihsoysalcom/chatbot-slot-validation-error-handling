import re

def validate_name(name):
    """Validates the user's name."""
    if not name.strip():
        # This is a validation error. Instead of an internal exception,
        # we return a user-friendly message.
        return False, "İsim boş bırakılamaz. Lütfen geçerli bir isim girin."
    return True, ""

def validate_email(email):
    """Validates the user's email format."""
    # A simple regex for email validation (not exhaustive but sufficient for demonstration)
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        # This is a validation error. The message is tailored for the user.
        return False, "Geçersiz e-posta formatı. Lütfen geçerli bir e-posta adresi girin."
    return True, ""

def validate_age(age_str):
    """Validates the user's age, ensuring it's a number within a reasonable range."""
    try:
        age = int(age_str)
        if not (1 <= age <= 120): # Define a reasonable age range for validation
            # Validation error: age out of expected range.
            return False, "Yaş 1 ile 120 arasında bir sayı olmalıdır. Lütfen geçerli bir yaş girin."
        return True, ""
    except ValueError:
        # This catches an internal Python error (e.g., trying to convert "abc" to int)
        # and translates it into a user-friendly validation error message.
        return False, "Yaş bir sayı olmalıdır. Lütfen geçerli bir yaş girin."

def run_onboarding_bot():
    """Simulates a slot-filling onboarding bot with validation error management."""
    print("Merhaba! Yeni ürünümüze kaydolmak için size yardımcı olacağım.")
    print("Lütfen bazı bilgileri benimle paylaşın.")

    user_data = {}

    # Slot 1: Name
    # The bot keeps asking until a valid name is provided.
    while "name" not in user_data:
        name_input = input("Adınız nedir? ")
        is_valid, error_message = validate_name(name_input)
        if is_valid:
            user_data["name"] = name_input
        else:
            # Crucial: Display a user-friendly error message without exposing internal logic.
            print(f"Hata: {error_message}")

    # Slot 2: Email
    # The bot keeps asking until a valid email is provided.
    while "email" not in user_data:
        email_input = input("E-posta adresiniz nedir? ")
        is_valid, error_message = validate_email(email_input)
        if is_valid:
            user_data["email"] = email_input
        else:
            # Crucial: Display a user-friendly error message without exposing internal logic.
            print(f"Hata: {error_message}")

    # Slot 3: Age
    # The bot keeps asking until a valid age is provided.
    while "age" not in user_data:
        age_input = input("Yaşınız kaç? ")
        is_valid, error_message = validate_age(age_input)
        if is_valid:
            user_data["age"] = int(age_input) # Store as int after successful validation
        else:
            # Crucial: Display a user-friendly error message without exposing internal logic.
            # This handles both non-numeric input (ValueError) and out-of-range numbers.
            print(f"Hata: {error_message}")

    print("\nHarika! Bilgilerinizi aldım:")
    for key, value in user_data.items():
        print(f"- {key.capitalize()}: {value}")
    print("Kaydınız başarıyla tamamlandı. Teşekkür ederiz!")

if __name__ == "__main__":
    run_onboarding_bot()
