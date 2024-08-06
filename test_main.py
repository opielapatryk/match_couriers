import unittest
from main import load_courier_rules, courier_rules_to_df, get_cheapest_courier, assign_couriers_to_orders

class TestCourierAssignment(unittest.TestCase):

    def setUp(self):
        self.orders = [
            {"id": 1, "products": [{"weight": 2.5, "dimensions": (10, 20, 30)}, {"weight": 1.2, "dimensions": (5, 5, 10)}], "address": "Ulica Sezamkowa 1"},
            {"id": 2, "products": [{"weight": 12.0, "dimensions": (20, 20, 20)}, {"weight": 5.0, "dimensions": (15, 15, 15)}], "address": "Ulica Sezamkowa 2"},
            {"id": 3, "products": [{"weight": 7.0, "dimensions": (10, 10, 10)}, {"weight": 8.0, "dimensions": (15, 15, 15)}], "address": "Ulica Sezamkowa 3"},
        ]
        
        self.couriers_rules = {
            "couriers": {
                "Courier A": {
                    "weight_limits": [5, 10, "inf"],
                    "prices": [10, 15, 20]
                },
                "Courier B": {
                    "weight_limits": [7, 15, "inf"],
                    "prices": [12, 18, 25]
                },
                "Courier C": {
                    "weight_limits": [10, 20, "inf"],
                    "prices": [8, 14, 22]
                }
            }
        }

        self.couriers_df = courier_rules_to_df(self.couriers_rules)

    def test_load_courier_rules(self):
        rules = load_courier_rules('couriers_rules.json')
        self.assertIn('couriers', rules)
        self.assertEqual(len(rules['couriers']), 3)

    def test_courier_rules_to_df(self):
        df = courier_rules_to_df(self.couriers_rules)
        self.assertEqual(len(df), 9)
        self.assertIn('Courier A', df['courier'].values)
        self.assertIn('Courier B', df['courier'].values)
        self.assertIn('Courier C', df['courier'].values)

    def test_get_cheapest_courier(self):
        self.assertEqual(get_cheapest_courier(1000, self.couriers_df), 'Courier A')
        self.assertEqual(get_cheapest_courier(8, self.couriers_df), 'Courier C')
        self.assertEqual(get_cheapest_courier(12, self.couriers_df), 'Courier C')

    def test_assign_couriers_to_orders(self):
        updated_orders = assign_couriers_to_orders(self.orders, self.couriers_df)
        self.assertEqual(updated_orders[0]['courier'], 'Courier C')
        self.assertEqual(updated_orders[1]['courier'], 'Courier C')
        self.assertEqual(updated_orders[2]['courier'], 'Courier C')

if __name__ == "__main__":
    unittest.main()