# RideTogether: розрахунок вартості бронювання

Модуль до user story **RIDE-17** проєкту RideTogether (Jira: `RIDE`), лабораторна робота 4 з ТРПЗ.

> Як пасажир, я хочу бачити підсумкову вартість, щоб знати, скільки заплачу.

Критерії приймання:

1. Вартість дорівнює ціні місця, помноженій на кількість місць.
2. Промокод зменшує суму, але вона не стає від'ємною.
3. Некоректні значення ціни або кількості відхиляються з помилкою.

```python
from booking_price import booking_total

booking_total(180, 3)                     # Decimal('540.00')
booking_total(200, 2, promo_discount=50)  # Decimal('350.00')
booking_total(100, 1, promo_discount=500) # Decimal('0.00')
booking_total(100, 0)                     # ValueError
```

## Запуск тестів

```bash
pip install -r requirements.txt
pytest -v
```

Тести автоматично запускає GitHub Actions (`.github/workflows/ci.yml`) на кожен push і pull request.
Гілки й коміти містять ключ задачі `RIDE-17`, тож у Jira вони видні в картці задачі.
