import random
import string

SIZE_OF_SHORTCODE = 6

def get_chars():
    """
    Returns character's string for code
    :return: string
    """
    chars = string.ascii_letters
    chars += string.digits
    chars += '!@#$%^&*()_+'
    return chars

def code_generator(size=SIZE_OF_SHORTCODE):
    """
    Gemnerates codes for shortcode
    """
    chars = get_chars()
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=SIZE_OF_SHORTCODE):
    new_code = code_generator(size=size)
    model = instance.__class__
    code_exists = model.objects.filter(shortcode=new_code).exists()

    if code_exists:
        return create_shortcode(size=size)
    return new_code
