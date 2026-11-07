"""Тести до RIDE-17. Кожен тест позначено критерієм приймання (КП1–КП3)."""
from decimal import Decimal

import pytest

from booking_price import MAX_SEATS, booking_total


# КП1: вартість = ціна місця × кількість місць
def test_one_seat():
    assert booking_total(250, 1) == Decimal("250.00")


def test_several_seats():
    assert booking_total(180, 3) == Decimal("540.00")


def test_kopecks_are_rounded():
    assert booking_total(99.995, 1) == Decimal("100.00")


def test_max_seats_boundary():
    assert booking_total(100, MAX_SEATS) == Decimal("800.00")


# КП2: промокод зменшує суму, але вона не стає від'ємною
def test_promo_reduces_total():
    assert booking_total(200, 2, promo_discount=50) == Decimal("350.00")


def test_promo_equal_to_total_gives_zero():
    assert booking_total(150, 2, promo_discount=300) == Decimal("0.00")


def test_promo_bigger_than_total_never_negative():
    assert booking_total(100, 1, promo_discount=500) == Decimal("0.00")


# КП3: некоректні значення відхиляються з помилкою
@pytest.mark.parametrize("price", [0, -10, "200", None, float("nan"), True])
def test_invalid_price_rejected(price):
    with pytest.raises(ValueError):
        booking_total(price, 1)


@pytest.mark.parametrize("seats", [0, -1, MAX_SEATS + 1, 1.5, "2", None])
def test_invalid_seats_rejected(seats):
    with pytest.raises(ValueError):
        booking_total(100, seats)


def test_negative_promo_rejected():
    with pytest.raises(ValueError):
        booking_total(100, 1, promo_discount=-20)
