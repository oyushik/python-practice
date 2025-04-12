def is_vaild_email(email: str) -> bool:
    if "@" and "." not in email:
        print("유효하지 않음")
        return False
    
    print("유효함")
    return True

is_vaild_email("user@example.com")
is_vaild_email("user@example")