import data
import sender_stand_request


def get_kit_body(name):
    new_body = data.kit_body.copy()
    new_body["name"] = name
    print(new_body)
    return new_body

def get_token():
    token = sender_stand_request.get_new_user_token()
    return token

def assert_negative_response_400(new_body):
    auth_token = get_token()
    print(new_body)
    response = sender_stand_request.post_new_client_kit(new_body, auth_token)
    assert response.status_code == 400

def assert_positive_response_201(new_body):
    auth_token = get_token()
    response = sender_stand_request.post_new_client_kit(new_body, auth_token)
    assert response.status_code == 201

def test_kit_name_a_get_assert_positive_response_201():
    kit_body = get_kit_body("a")
    assert_positive_response_201(kit_body)

def test_kit_name_511_characters_get_assert_positive_response_201():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    assert_positive_response_201(kit_body)

def test_kit_0_characters_get_assert_negative_response_400():
    kit_body = get_kit_body("")
    assert_negative_response_400(kit_body)

def test_kit_name_512_characters_get_assert_negative_response_400():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    assert_negative_response_400(kit_body)

def test_kit_special_characters_get_assert_positive_response_201():
    kit_body = get_kit_body("\"№%@\",")
    assert_positive_response_201(kit_body)

def test_kit_space_get_assert_positive_response_201():
    kit_body = get_kit_body(" A Aaa ")
    assert_positive_response_201(kit_body)

def test_kit_name_numbers_get_assert_positive_response_201():
    kit_body = get_kit_body("123")
    assert_positive_response_201(kit_body)

def test_kit_name_not_passed_get_assert_negative_response_400():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    assert_negative_response_400(kit_body)

def test_kit_name_different_parameters_get_assert_negative_response_400():
    kit_body = get_kit_body(123)
    assert_negative_response_400(kit_body)
