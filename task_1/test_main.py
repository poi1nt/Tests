from main_1 import get_unique_teacher_names
from main_2 import get_unique_id
from main_3 import get_geo_logs

def test_main_1():
    expected = 'Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'
    res = get_unique_teacher_names()
    assert res == expected

def test_main_2():
    expected = [98, 35, 213, 54, 119, 15]
    res = get_unique_id()
    assert res == expected

def test_main_3():
    expected = {'Россия'}
    res = get_geo_logs()
    country_list = []
    for item in res:
        for value in item.values():
            country_list.append(value[1])
    assert set(country_list) == expected