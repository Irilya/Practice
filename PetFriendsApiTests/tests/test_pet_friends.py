from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_without_photo_with_valid_data(name='Fred', animal_type='Frog', age='2'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_valid_data(name='Bob', animal_type='Cat', age='2', pet_photo='images/cat.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_foto_of_new_pet_with_valid_data(pet_photo='images/frog.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_foto_of_new_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id in result.values()


def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Фрэд', animal_type='лягушонок', age=1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_get_api_key_for_invalid_email(email='irma@mail.ru', password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_invalid_password(email=valid_email, password='12345'):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_empty_password(email=valid_email, password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_add_new_pet_with_negative_age(name='Фрэд', animal_type='лягушонок',
                                       age=12345678934334343434333000009348575638):
    """На сегодняшний день сервер обрабатывает отрицательный возраст, из-за чего тест
    падает. Отрицательное значение для возраста неверно - баг"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status != 200


def test_add_new_pet_with_surplus_age(name='Фрэд', animal_type='лягушонок', age=12345678934334343434333000009348575638):
    """На сегодняшний день сервер обрабатывает ослишком большой возраст, из-за чего тест
    падает. Избыточное значение для возраста неверно - баг"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status != 200


def test_add_new_pet_without_data(name='', animal_type='', age=''):
    """На сегодняшний день сервер обрабатывает запрос с полностью пустыми
    полями, из-за чего тест падает. Баг"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status != 200


def test_update_self_pet_info_with_incorrect_age(name='Sema', animal_type='dog', age=-1):
    """На сегодняшний день сервер обрабатывает отрицательный возраст, из-за чего тест
    падает. Отрицательное значение для возраста неверно - баг"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status != 200
    else:
        raise Exception("There is no my pets")


def test_get_my_pets_with_valid_key(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    if len(result['pets']) > 0:
        assert status == 200
    else:
        raise Exception("There is no my pets")



