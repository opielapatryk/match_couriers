import json
import pandas as pd
from orders import orders

# Load the courier rules from JSON file
def load_courier_rules(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Convert courier rules to DataFrame
def courier_rules_to_df(couriers_rules):
    couriers = couriers_rules["couriers"]
    data = []
    for courier, details in couriers.items():
        # Convert weight limits to float, handling "inf"
        weight_limits = [float(x) for x in details["weight_limits"]]
        df = pd.DataFrame({
            'weight_limit': weight_limits,
            'price': details["prices"]
        })
        df['courier'] = courier
        data.append(df)
    return pd.concat(data, ignore_index=True)

# Determine the cheapest courier for a given order weight
def get_cheapest_courier(weight, couriers_df):
    applicable = couriers_df[couriers_df['weight_limit'] >= weight]
    return applicable.loc[applicable['price'].idxmin()]['courier']

# Assign couriers to orders
def assign_couriers_to_orders(orders, couriers_df):
    updated_orders = []
    for order in orders:
        total_weight = sum(product['weight'] for product in order['products'])
        courier = get_cheapest_courier(total_weight, couriers_df)
        updated_order = {**order, 'courier': courier}
        updated_orders.append(updated_order)
    return updated_orders

# Main function to match couriers to orders
def match_couriers():
    filename = 'couriers_rules.json'
    couriers_rules = load_courier_rules(filename)
    couriers_df = courier_rules_to_df(couriers_rules)
    updated_orders = assign_couriers_to_orders(orders, couriers_df)
    return updated_orders

# Print the updated orders with assigned couriers
if __name__ == "__main__":
    print(match_couriers())