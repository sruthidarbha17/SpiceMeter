# Simple Food Spice Level and Reference Suggestion Program

# Predefined dictionary of foods with spice levels and references
food_spice_data = {
    "chili": {"spice_level": "High", "reference": "Commonly used in Mexican and Indian cuisine."},
    "curry": {"spice_level": "Medium-High", "reference": "A blend of spices from South Asia, varies in heat."},
    "black pepper": {"spice_level": "Mild", "reference": "Widely used worldwide as a seasoning."},
    "ginger": {"spice_level": "Mild", "reference": "Adds warmth and zest, used in many Asian dishes."},
    "paprika": {"spice_level": "Mild to Medium", "reference": "Made from ground peppers, used in Hungarian and Spanish food."},
    "wasabi": {"spice_level": "High", "reference": "Japanese horseradish, very pungent and spicy."},
    "jalapeno": {"spice_level": "Medium", "reference": "Popular chili pepper with moderate heat."},
    "garlic": {"spice_level": "None", "reference": "Adds pungent flavor, not spicy but strong."},
    "cinnamon": {"spice_level": "None", "reference": "Sweet and warm spice, not hot."},
    "mustard": {"spice_level": "Mild to Medium", "reference": "Adds a tangy heat, common in dressings and sauces."}
}

def get_food_spice_info(food_name):
    food = food_name.lower()
    if food in food_spice_data:
        info = food_spice_data[food]
        return f"{food_name.title()} typically has a spice level of {info['spice_level']}. Reference: {info['reference']}"
    else:
        return f"Sorry, spice level info for '{food_name}' is not available."

# Example usage:
if __name__ == "__main__":
    food_input = input("Enter a food or spice name to get its spice level and reference: ")
    print(get_food_spice_info(food_input))
