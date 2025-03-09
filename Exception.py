 try:
    student = {"name": "Shamsa", "age": 21}
    print("Student's grade:", student["grade"])  # Key doesn't exist
except KeyError as e:
    print(f"KeyError: The key {e} is not found in the dictionary.")
finally:
    print("Dictionary operation completed.")