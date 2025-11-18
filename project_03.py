# Create a nested list structure
cart = [["Electronics", []], ["Clothing", []], ["Food", []]]

# Add at least 2 items to each category
cart[0][1].extend(["Laptop", "Headphones"])  # Electronics
cart[1][1].extend(["T-Shirt", "Jeans"])      # Clothing
cart[2][1].extend(["Apple", "Bread"])        # Food

# Display the total number of items in the cart
total_items = sum(len(category[1]) for
                   category in cart)
print(f"Total items in cart: {total_items}")

# Find and display the category with the most items
max_category = max(cart, key=lambda x: len(x[1]))
print(f"Category with most items: {max_category[0]} ({len(max_category[1])} items)")

# Create a function to move an item from one category to another
def move_item(cart, from_category, to_category, item):
    for cat in cart:
        if cat[0] == from_category and item in cat[1]:
            cat[1].remove(item)
            break
    for cat in cart:
        if cat[0] == to_category:
            cat[1].append(item)
            break

# Example: Move "Apple" from Food to Electronics
move_item(cart, "Food", "Electronics", "Apple")

# Generate a final receipt showing all categories and their items
print("\nFinal Receipt:")
for category, items in cart:
    print(f"{category}: {', '.join(items) if items else 'No items'}")