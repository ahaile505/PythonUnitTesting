import pytest
from .phonebook import PhoneBook



@pytest.fixture
def phonebook():
    return PhoneBook()

def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")

def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "123")
    assert "Bob" in phonebook.names()




