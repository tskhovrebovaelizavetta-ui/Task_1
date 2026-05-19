from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns_returns_list_of_bun_objects(self):
        database = Database()
        buns = database.available_buns()

        assert buns
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_returns_list_of_ingredient_objects(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients
        assert all(isinstance(item, Ingredient) for item in ingredients)

    def test_buns_have_expected_values(self):
        database = Database()
        buns = database.available_buns()

        assert buns[0].get_name() == 'black bun'
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == 'white bun'
        assert buns[1].get_price() == 200

    def test_ingredients_have_expected_values(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[0].get_type() == 'SAUCE'
        assert ingredients[0].get_name() == 'hot sauce'
        assert ingredients[0].get_price() == 100
        assert ingredients[-1].get_type() == 'FILLING'
        assert ingredients[-1].get_name() == 'sausage'
        assert ingredients[-1].get_price() == 300