# --------------------WRITE YOUR CODE BELOW-------------------#


# --------------------END OF YOUR CODE------------------------#

'''
CREATE THE BELOW CALLED FUNCTION DEFINITION IN YOUR CODE!
'''

if __name__ == '__main__':

    # Sample data for tasks
    sample_text = "Sample email addresses: abc@example.com, xyz@domain.com"
    sample_numbers = [2, 4, 6, 8, 10]
    sample_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    sample_paragraph = "This is a long paragraph that needs to be wrapped to multiple lines for better readability."
    sample_number = 12345.67
    sample_table_name = "users"
    sample_columns = "id, name, email"
    sample_numbers_for_heap = [3, 1, 4, 1, 5, 9]

    # Task executions
    list_files_in_directory(".")  # Task 1
    extract_emails(sample_text)  # Task 2
    calculate_square_root(16)  # Task 3
    generate_random_integer(1, 100)  # Task 4
    calculate_mean_and_stddev(sample_numbers)  # Task 5
    print_current_datetime()  # Task 6
    time_function_execution()  # Task 7
    truncate_long_string("This is a very long string that needs to be truncated.")  # Task 8
    pretty_print_nested_dict(sample_dict)  # Task 9
    wrap_text_paragraph(sample_paragraph, 30)  # Task 10
    generate_sql_query(sample_table_name, sample_columns)  # Task 11
    setup_logging()  # Task 12
    perform_heap_operations(sample_numbers_for_heap)  # Task 13
