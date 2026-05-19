import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize(
        'type_, name, price',
        [
            ('Соус', 'Соус Spicy-X', 90),
            ('Начинка', 'Говяжий метеорит (отбивная)', 3000),
        ],
    )
    def test_ingredient_fields_and_getters(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.type == type_
        assert ingredient.name == name
        assert ingredient.price == price
        assert ingredient.get_type() == type_
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price