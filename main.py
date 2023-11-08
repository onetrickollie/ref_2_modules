#Kaixiang Liu
#lab09

# --------------------WRITE YOUR CODE BELOW-------------------#
import os, re, math, random, statistics,datetime,timeit,reprlib,pprint
import textwrap,string,logging,heapq

#task 1: list all files in a directory
def list_files_in_directory(directory):
    files = os.listdir(directory)
    for file in files:
        print(os.path.join(directory, file))
#task 2: use re module to search and extract emails 
def extract_emails(sample_text):
    email_pattern = r'\S+@\S+'
    emails = re.findall(email_pattern, sample_text)
    for email in emails:
        print(email)
#task 3: calculate square_root using math module
def calculate_square_root(num):
    sqrt = math.sqrt(num)
    print(f"Square root of {num} is {sqrt}")
#task 4: generate random interger using random.randint
def generate_random_integer(num1,num2):
    random_integer = random.randint(num1,num2)
    print(f"Random integer between {num1} and {num2}: {random_integer}")
#task 5: calculate mean and std using statistics module
def calculate_mean_and_stddev(sample_numbers):
    mean = statistics.mean(sample_numbers)
    std = statistics.stdev(sample_numbers)
    print(f"Mean: {mean}, Standard Deviation: {std}")
#task 6: print date&time using datetime module
def print_current_datetime(): 
    time = datetime.datetime.now()
    print(f"Current Date and Time: {time}")
#task 7: using timeit to measure the time needed for a simple function
def time_function_execution(): 
    #sample_function execution
    def sample_function():
        total = 0
        for i in range(1000):
            total += i
        return total

    time_taken = timeit.timeit(sample_function, number=10000)
#task 8: using reprlib to truncate long strings
def truncate_long_string(sample_text): 
    truncated_text = reprlib.repr(sample_text)
    print(f"Truncated String: {truncated_text}")
#task 9: using pprint to print a dictionary
def pretty_print_nested_dict(sample_dict):
    pprint.pprint(sample_dict)
#task 10: using textwrap to wrap text in specific width
def wrap_text_paragraph(sample_paragraph, width):
    wrapped_text = textwrap.fill(sample_paragraph, width=width)
    print(wrapped_text)
#task 11: using string template to geneate sql_query w/ placeholders
def generate_sql_query(sample_table_name, sample_columns):
    query_template = string.Template("SELECT $columns FROM $table_name")
    query = query_template.substitute(columns=sample_columns, table_name=sample_table_name)
    print(f"Generated SQL Query: {query}")
#task 12: using logging module to log 
def setup_logging():
    logging.basicConfig(filename='app.log', level=logging.INFO)
    logging.info('This is a log message.')
#task 13: using heap module to perform heap operations on integers
def perform_heap_operations(sample_numbers_for_heap):
    heapq.heapify(sample_numbers_for_heap)
    print(f"Heapified List: {sample_numbers_for_heap}")
    print(f"Smallest Element: {heapq.heappop(sample_numbers_for_heap)}")
# --------------------END OF YOUR CODE------------------------#


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
