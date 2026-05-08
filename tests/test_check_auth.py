from check_auth import check_auth

def test_is_admin():
    result = check_auth("admin", "password")
    assert result == "Добро пожаловать"

def test_invalid_login():
    result = check_auth("user", "password")
    assert result == "Доступ ограничен"

def test_invalid_password():
    result = check_auth("admin", "123")
    assert result == "Доступ ограничен"

def test_both_invalid():
    result = check_auth("no_auth_user", "wrong_password")
    assert result == "Доступ ограничен"
