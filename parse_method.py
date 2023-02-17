from urllib import parse as p


def parse(query: str) -> dict:
    p.parse_qs(p.urlsplit(query).query)
    w = dict(p.parse_qsl(p.urlsplit(query).query))
    print(w)
    return w


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&?') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name====ferret&color=purple&?') == {'name': 'ferret', 'color': 'purple'}
    assert parse("http://www.example.org/default.html?to=55&too=77&summer=12") == {'summer': '12', 'too': '77', 'to': '55'}
    assert parse("http://www.example.org/default.html?to=80&too=154") == {'to': '80', 'too': '154'}
    assert parse('http://example.com/?&') == {}
    assert parse('http://example.com/?&=printing') == {'': 'printing'}
    assert parse('https://example.com/store?page=4&sort=21&price=MARNI') == {'page': '4', 'sort': '21', 'price': 'MARNI'}
    assert parse('http://127.0.0.1:8000/items/?reboot=3&enjoy=2') == {'reboot': '3', 'enjoy': '2'}
    assert parse('https://example.com/path/to/page?shoes=gucci&&&&&&&&&?=white') == {'shoes': 'gucci', '?': 'white'}
    assert parse('https://example.com/path/to/page?clothes=size&?color=red') == {'clothes': 'size', '?color': 'red'}