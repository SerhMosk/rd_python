from task_1_phone_number_regex import find_record


def test_find_record_success():
    assert find_record('Serhiy').get('name') == 'Serhiy'
    assert find_record('Noname') is None


if __name__ == "__main__":
    test_find_record_success()
