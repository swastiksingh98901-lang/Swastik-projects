# Create a list called library with 5 book titles
library = ['physics', 'Maths', 'Basic Mathematics', 'English', 'python']

print("Initial Library:", library)

# Add 2 more books using append()
library.append('Data science')
library.append('Database Management')

print("After adding books:", library)

# Remove one book that you've "read" (e.g., '1984')
library.remove('Maths')

print("After removing 'Maths':", library)

# Display the total number of books
print("Total books:", len(library))

# Check if a specific book exists (e.g., 'The Great Gatsby')
book_to_check = 'English'
print(f"Is '{book_to_check}' in library? {book_to_check in library}")

# Sort the library alphabetically and display it
library.sort()
print("Sorted library:", library)