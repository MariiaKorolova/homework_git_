def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {k: v.value for k, v in cookie.items()}
    print(cookies)
    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;surname=igor;') == {'name': 'Dima=User', 'age': '28', 'surname': 'igor'}
    assert parse_cookie('color=green;name=sonia;') == {'color': 'green', 'name': 'sonia'}
    assert parse_cookie('name=; John=User; age=28;') == {'name': '', 'John': 'User', 'age': '28'}
    assert parse_cookie('=; name=John;') == {'': '', 'name': 'John'}
    assert parse_cookie('name=22;surname=57;all=90;') == {'name': '22', 'surname': '57', 'all': '90'}
    assert parse_cookie('color=red;name=user;') == {'color': 'red', 'name': 'user'}
    assert parse_cookie('01234=;') == {'01234': ''}
    assert parse_cookie('user_name=John=age=28;') == {'user_name': 'John=age=28'}
    assert parse_cookie('name=; John=User; age=28;') == {'name': '', 'John': 'User', 'age': '28'}
    assert parse_cookie('=; name=John;') == {'': '', 'name': 'John'}