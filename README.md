# Inventory Tracker CLI

![Git](https://img.shields.io/badge/Git-F05033?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![Terminal](https://img.shields.io/badge/CLI-Terminal-blue)

Command-line inventory management system for tracking products, quantities, and prices.

## Features

✅ View all products  
✅ Add new products  
✅ Update product quantities  
✅ Delete products  
✅ Calculate total inventory value  
✅ Persistent storage (JSON file)  
✅ Input validation and error handling

## Installation

```bash
# Clone the repository
git clone git@github.com:chris-kechagias/inventory-tracker-cli.git
cd inventory-tracker-cli

# No dependencies needed - uses Python standard library!
```

## Usage

```bash
python inventory.py
```

### Example Workflow

1. Choose option 2 to add products
2. Choose option 1 to view inventory
3. Choose option 5 to see total value
4. Choose option 6 to exit (auto-saves)

## Technical Details

**Language:** Python 3.13.7  
**Storage:** JSON file (`products.json`)  
**Libraries:** json, os (standard library)

## Skills Demonstrated

- File I/O operations
- JSON data handling
- User input validation
- Error handling (try/except)
- Function modularization
- Git version control

## Future Improvements

- [ ] Search products by name
- [ ] Category filtering
- [ ] Low stock alerts
- [ ] Export to CSV
- [ ] SQLite database integration

## Author

Chris Kechagias - Learning AI Engineering  
Part of my 10-month roadmap (Nov 2025 - Sep 2026)

## License

MIT
