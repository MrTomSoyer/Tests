from check_email import check_email  # замените «ваш_файл» на имя вашего файла с функцией

def test_valid_email():
    assert check_email('test@example.com') is True

def test_valid_russian_email():
    assert check_email('мояпочта@нетология.ру') is True

def test_multiple_at_symbols():
    assert check_email('python@email@net') is False

def test_email_with_space():
    assert check_email(' em@il.ru') is False

def test_email_without_at():
    assert check_email('example.com') is False

def test_email_without_dot():
    assert check_email('test@domain') is False
