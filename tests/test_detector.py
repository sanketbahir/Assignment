from sensitive_info_detector.detector import check_for_secrets


#
def test_secrets_present():

    file_path = "/home/user/assignments/assignments/sensitive_info_detector/demo.txt"
    assert check_for_secrets(file_path) == True


#
def test_no_secrets_present():

    file_path = "assignments/sensitive_info_detector/demonosecrets.txt"
    check_for_secrets(file_path) == False


#
def test_file_not_found():

    file_path = "non_existent_file.txt"
    assert check_for_secrets(file_path) == False
