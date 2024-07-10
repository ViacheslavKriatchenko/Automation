import pytest
from string_utils import StringUtils
from contextlib import nullcontext as does_not_raise


# функция capitilize
@pytest.mark.positive
@pytest.mark.parametrize('input, output', [
    ('name', 'Name'),
    ('FIRST', 'First'),
    ('python3', 'Python3'),
     ])
def test_check_capitilize(input, output):
    result = StringUtils().capitilize(input)
    assert output == result


@pytest.mark.negative
@pytest.mark.parametrize('input, output, expectation', [
    ('!you', '!you', does_not_raise()),
    ('12level', '12level', does_not_raise()),
    (None, None, pytest.raises(AttributeError)),
    ])
def test_check_capitilize_negative(input, output, expectation):
    with expectation:
        result = StringUtils().capitilize(input)
        assert output == result


# функция trim
@pytest.mark.positive
@pytest.mark.parametrize('input, output', [
    (' one', 'one'),
    ('     five', 'five'),
    (' 7_Days', '7_Days'),
    ])
def test_check_trim(input, output):
    result = StringUtils().trim(input)
    assert result == output


@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize('input, output', [
    ('   12345', 12345),
    (None, None),
    ])
def test_check_trim_negative(input, output):
    result = StringUtils().trim(input)
    assert result == output


# функция to_list
@pytest.mark.positive
@pytest.mark.parametrize('input, delim, output', [
    ('a,b,c,d', ',', ['a', 'b', 'c', 'd']),
    ('', '', []),
    ('a-b-c-d', '-', ['a', 'b', 'c', 'd']),
    ('2,3,5,8', ',', ['2', '3', '5', '8']),
    ('1-2-3-5-8-13', '-', ['1', '2', '3', '5', '8', '13']),
    ('P:y:t:h:o:n', ':', ['P', 'y', 't', 'h', 'o', 'n']),
    ('que pasa/chico', '/', ['que pasa', 'chico']),
    ])
def test_check_to_list(input, delim, output):
    result = StringUtils().to_list(input, delim)
    assert result == output


@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('input, delim, output', [
    (None, ',', None),
    (1*2*3, '*', ['1', '2', '3']),
    ('1*2*3', '*', [1, 2, 3]),
    (['a=b=c'], '=', ['a', 'b', 'c'])
    ])
def test_check_to_list_negative(input, delim, output):
    result = StringUtils().to_list(input, delim)
    assert result == output


# функция contains
@pytest.mark.positive
@pytest.mark.parametrize('input_1, input_2, output', [
    ('Чемпион', 'пион', True),
    ('mail.com', 'com', True),
    ('J', 'j', False),
    ])
def test_check_contains(input_1, input_2, output):
    result = StringUtils().contains(input_1, input_2)
    assert result == output


@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('input_1, input_2, output', [
    ('Чемпион', 'пион', False),
    ('Galaxy', 'а', True),
    ('12Twelf', 12, True),
    ])
def test_check_contains_negative(input_1, input_2, output):
    result = StringUtils().contains(input_1, input_2)
    assert result == output


# функция delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize('input_1, input_2, output', [
    ('ряд', 'р', 'яд'),
    ('Букварь', 'рь', 'Буква'),
    ('Pyt hon', ' ', 'Python'),
    ('     ', '   ', '  '),
    ])
def test_check_delete_symbol(input_1, input_2, output):
    result = StringUtils().delete_symbol(input_1, input_2)
    assert result == output


@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('input_1, input_2, output', [
    ('Python', 'р', 'ython'),
    ('Zero_0', 0, 'Zero'),
    ])
def test_check_delete_symbol_negative(input_1, input_2, output):
    result = StringUtils().delete_symbol(input_1, input_2)
    assert result == output


# функция starts_with
@pytest.mark.positive
@pytest.mark.parametrize('input_1, input_2, output', [
    ('Symbol', 'S', True),
    ('0blom', '0', True),
    ('$грязная зеленая бумажка', '$', True),
    ('(_o_)', '(', True),
    ('Ёшки', 'ё', False),
    ])
def test_check_starts_with(input_1, input_2, output):
    result = StringUtils().starts_with(input_1, input_2)
    assert result == output


@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('input_1, input_2, output', [
    ('Medal', 'М', True),  # ланитица-кирилица
    ('0блом', 0, True)
    ])
def test_check_starts_with_negative(input_1, input_2, output):
    result = StringUtils().starts_with(input_1, input_2)
    assert result == output


# функция end_with
@pytest.mark.positive
@pytest.mark.parametrize('input_1, input_2, output', [
    ('Symbol', 'l', True),
    (' ', ' ', True),
    ])
def test_check_end_with(input_1, input_2, output):
    result = StringUtils().end_with(input_1, input_2)
    assert result == output


@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('input_1, input_2, output', [
    ('Symbol', 'l', False),
    (' _', ' ', True),
    ('One1', 1, True),
    (1, '1', True)
    ])
def test_check_end_with_negative(input_1, input_2, output):
    result = StringUtils().end_with(input_1, input_2)
    assert result == output


# функция is_empty
@pytest.mark.positive
@pytest.mark.parametrize('input, output', [
    ('', True),
    ('   ', True),
    ('information', False),
    ])
def test_check_is_empty(input, output):
    result = StringUtils().is_empty(input)
    assert result == output


@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('input, output', [
    ('   ', False),
    ('_', True),
    ('†', True),
    (1, True)
    ])
def test_check_is_empty_negative(input, output):
    result = StringUtils().is_empty(input)
    assert result == output


# функция list_to_string
@pytest.mark.positive
@pytest.mark.parametrize('input_1, delim, output', [
    (['a', 'b', 'c'], ', ', 'a, b, c'),
    (['1', '2', '3'], '---', '1---2---3'),
    ([1, 2, 3], '---', '1---2---3'),
    ([], '_', ''),
    (['+', '!', '@'], '---', '+---!---@'),
    ([' A ', ' B '], '%', ' A % B ')
    ])
def test_check_list_to_string(input_1, delim, output):
    result = StringUtils().list_to_string(input_1, delim)
    assert result == output


@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize('input_1, delim, output', [
    ('a, b, c', ', ', 'a, b, c'),
    (None, '_', None),
    (['A'], '%', 'A%')
    ])
def test_check_list_to_string_negative(input_1, delim, output):
    result = StringUtils().list_to_string(input_1, delim)
    assert result == output
