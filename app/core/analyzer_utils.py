from app.schemas import PasswordData
import re

async def get_capital_letter(password: PasswordData) -> bool:
    return bool(re.search(r"[A-Z]", password.password))

async def get_lowercase_letter(password: PasswordData) -> bool:
    return bool(re.search(r"[a-z]", password.password))

async def get_special_character(password: PasswordData) -> bool:
    return bool(re.search(r"[^\w\s]", password.password))

async def get_minimum_length(password: PasswordData, length: int = 8) -> bool:
    return length <= len(password.password)

async def get_descending_sequence(password: PasswordData) -> bool:
    for i in range(len(password.password) - 2):
        character_1 = ord(password.password[i])
        character_2 = ord(password.password[i + 1])
        character_3 = ord(password.password[i + 2])
            
        if character_2 == character_1 - 1 and character_3 == character_2 - 1:
            return True
        
    return False

async def get_ascending_sequence(password: PasswordData) -> bool:
    for i in range(len(password.password) - 2):
        character_1 = ord(password.password[i])
        character_2 = ord(password.password[i + 1])
        character_3 = ord(password.password[i + 2])
            
        if character_2 == character_1 + 1 and character_3 == character_2 + 1:
            return True
            
    return False

async def get_numbers(password: PasswordData, minimum_quantity: int = 3) -> bool:
    numbers = re.finditer(r"\d", password.password)
    try:
        for _ in range(minimum_quantity):
            next(numbers)
        return True
    except StopIteration:
        return False