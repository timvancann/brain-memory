from brain_memory.majorsystem import word_to_number


def test_major_convert():
    assert word_to_number('cheese') == '60'
    assert word_to_number('jump') == '639'
    assert word_to_number('racket') == '471'
    assert word_to_number('mnemonic') == '2327'
    assert word_to_number('ball') == '95'
    assert word_to_number('favour') == '884'
