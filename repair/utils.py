import random
import string


def generate_repair_code():
    REPAIRING_CODE_LENGTH = 8
    alphanumeric_chars = string.ascii_letters + string.digits
    return "".join(random.choice(alphanumeric_chars) for _ in range(REPAIRING_CODE_LENGTH))
