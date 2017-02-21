"""Tests to make sure client and server can communicate via sockets."""


import pytest
import client
import server


def test_message_longer_than_buffer():
    """Test if string that is longer than buffer length gets sent."""
    assert client.client("I don't know why you say 'goodbye' I say 'hello'") == "I don't know why you say 'goodbye' I say 'hello'"


def test_message_same_length_as_buffer():
    """Test if string that is same length buffer length gets sent."""
    assert client.client("hlo gdby") == "hlo gdby"


def test_message_shorter_than_buffer():
    """Test if string that is shorter than buffer length gets sent."""
    assert client.client("¡¢£¤¥") == "¡¢£¤¥"


def test_message_non_ascii_same_length_as_buffer():
    """Test if string that is same length buffer length with non ascii characters gets sent."""
    assert client.client("Fl®rg th") == "Fl®rg th"


def test_message_non_ascii_longer_than_buffer():
    """Test if string that is shorter than buffer length with non ascii characters gets sent."""
    assert client.client("Fl®rg the bl®rg!!") == "Flérg the blérg!!"


def test_message_shorter_non_ascii_than_buffer():
    """Test if string that is shorter than buffer length with non ascii character gets sent."""
    assert client.client("Fl®rg") == "Fl®rg"
