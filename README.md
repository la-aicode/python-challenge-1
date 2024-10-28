# Variety Food Truck Ordering System

Welcome to the Variety Food Truck Ordering System! This Python-based program allows users to browse a variety of food and drink categories, select items, specify quantities, and view a detailed receipt of their order. 

## Features
- **Menu Browsing**: View items categorized into `Snacks`, `Meals`, `Drinks`, and `Desserts`.
- **Order Selection**: Select specific items from each category and specify quantities.
- **Receipt Generation**: See a detailed breakdown of your order, including item names, prices, and quantities, followed by the total cost.

## Menu Structure

The menu is stored in a nested dictionary format, organized by categories, which contain items with their respective prices. Some items (like pizza types and drink sizes) are further subdivided into subcategories.

Example of the menu dictionary:
```python
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        ...
    },
    ...
}
