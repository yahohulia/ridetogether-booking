"""RIDE-17: розрахунок вартості бронювання (RideTogether).

Історія користувача: як пасажир, я хочу бачити підсумкову вартість,
щоб знати, скільки заплачу.

Критерії приймання:
1. Вартість дорівнює ціні місця, помноженій на кількість місць.
2. Промокод зменшує суму, але вона не стає від'ємною.
3. Некоректні значення ціни або кількості відхиляються з помилкою.
"""
from decimal import ROUND_HALF_UP, Decimal

MAX_SEATS = 8


def _money(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise ValueError(f"{name} має бути числом")
    amount = Decimal(str(value))
    if not amount.is_finite():
        raise ValueError(f"{name} має бути скінченним числом")
    if amount < 0:
        raise ValueError(f"{name} не може бути від'ємною")
    return amount


def booking_total(seat_price, seats, promo_discount=0):
    """Повертає підсумкову вартість бронювання в гривнях з точністю до копійки.

    seat_price      ціна одного місця, яку вказав водій (грн, > 0)
    seats           кількість місць у бронюванні (ціле, 1..MAX_SEATS)
    promo_discount  знижка за промокодом (грн, >= 0)
    """
    price = _money(seat_price, "Ціна місця")
    if price == 0:
        raise ValueError("Ціна місця має бути більшою за 0")
    if isinstance(seats, bool) or not isinstance(seats, int):
        raise ValueError("Кількість місць має бути цілим числом")
    if not 1 <= seats <= MAX_SEATS:
        raise ValueError(f"Кількість місць має бути від 1 до {MAX_SEATS}")
    discount = _money(promo_discount, "Знижка")

    total = price * seats - discount
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
