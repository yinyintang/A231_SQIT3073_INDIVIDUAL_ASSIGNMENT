# A231 SQIT3073 INDIVIDUAL ASSIGNMENT (HOUSING LOAN ELIGIBILITY AND DSR CALCULATOR)

import os 

try:
    # Attempt to clear the screen for Windows
    os.system('cls')
except:
    try:
        # Attempt to clear the screen for macOS if the first try fails
        os.system('clear')
    except:
        # Output an error message if both attempts fail
        print("Unable to clear the screen.")

# Initialize an empty list to store loan calculations
loan_calculations = []

# Set the DSR threshold
dsr_threshold = 70

# User credentials for login system
user_credentials = {"user_id": "sqit3073", "password": "1234"}

# File to store loan calculations
file_path = "housing_loan_calculations.txt"

# Function to save loan calculations to a file
def save_calculations_to_file():
    with open(file_path, "w") as file:
        for calculation in loan_calculations:
            file.write(str(calculation) + "\n")

# Function to load loan calculations from a file
def load_calculations_from_file():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                try:
                    calculation = eval(line.strip())
                    loan_calculations.append(calculation)
                except Exception as e:
                    print(f"Error loading calculation: {e}")

# Login system
def login():
    # Function to handle user login
    # All users have 3 login attempts
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        print("\nUser Login:")
        user_id = input("Please enter your user ID: ")
        password = input("Please enter your password: ")

        if user_id == user_credentials["user_id"] and password == user_credentials["password"]:
            print("\nLogin successful! Welcome to the Housing Loan Eligibility and DSR Calculators!\n")
            break
        else:
            print("\nInvalid username or password. Please try again!")
            attempts += 1
 
    # If user's try all three attempts
    if attempts == max_attempts:
        print("\nYou have reached maximum login attempts. Exiting program.")
        exit()

# Function to get numeric input with validation
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("\nError: Invalid input. Please enter a valid numeric value.")

# Option 1: Calculate New Loan
def calculate_new_loan():
    print("\nPlease enter loan details:")
    
    # Get user's loan details
    # User's principal loan amount
    while True:
        principal_loan_amount = get_numeric_input("Principal loan amount (RM): ")
        if principal_loan_amount >= 0:
            break
        else:
            print("\nError: Principal loan amount cannot be negative. Please enter a valid amount.")

    # User's annual interest rate
    while True:
        annual_interest_rate = get_numeric_input("Annual interest rate (%): ")
        if 0 <= annual_interest_rate <= 10:
            break
        else:
            print("\nError: Annual interest rate should be between 0 and 10 (in %). Please enter a valid rate.")    
    
    # User's loan term in years
    while True:
        try:
            loan_term_years = int(input("Loan term in years: "))
            if loan_term_years > 0:
                break
            else:
                print("\nError: Loan term should be a positive integer. Please enter a valid term.")
        except ValueError:
            print("\nError: Invalid input. Please enter a valid integer for the loan term.")
   
    # User's monthly income
    while True:
        monthly_income = get_numeric_input("Applicant's monthly income (RM): ")
        if monthly_income >= 0:
            break
        else:
            print("\nError: Monthly income cannot be negative. Please enter a valid amount.")

    # User's other monthly financial commitments
    while True:
        other_commitments = get_numeric_input("Other monthly financial commitments (RM): ")
        if other_commitments >= 0:
            break
        else:
            print("\nError: Other monthly commitments cannot be negative. Please enter a valid amount.")

    # Calculate loan details
    try:
        if loan_term_years == 0:
            raise ValueError("\nError: Loan term is zero. Please enter a valid loan term.")   
        
        # Function to calculate monthly installment for housing loan details
        monthly_interest_rate = (annual_interest_rate / 100) / 12
        num_payments = loan_term_years * 12
        monthly_installment = (principal_loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** - num_payments)
            
        # Function to calculate total amount payable over the term of the loan
        total_amount_payable = monthly_installment * loan_term_years * 12
            
        # Function to calculate the Debt Service Ratio (DSR)
        total_commitments = other_commitments + monthly_installment
        dsr = (total_commitments / monthly_income) * 100
    except ValueError as ve:
        print(ve)
        return
    

    # Display housing loan details
    print("\nLoan Details:")
    print(f"Monthly Installment: RM{monthly_installment:.2f}")
    print(f"Total Amount Payable: RM{total_amount_payable:.2f}")
    print(f"Debt Service Ratio (DSR): {dsr:.2f}%")

    # Check eligibility based on DSR
    # Assume the threshold for DSR is 70%.
    # If the calculated DSR is below this threshold, the user is considered eligible for the housing loan.
    if dsr <= dsr_threshold:
        print("\nCongratulations! You are eligible for the loan.")
    else:
        print("\nSorry, you are not eligible for the loan.")
        
    # Append housing loan calculation details into list
    loan_calculations.append({
        "Principal": principal_loan_amount,
        "Interest Rate": annual_interest_rate,
        "Loan Term": loan_term_years,
        "Monthly Income": monthly_income,
        "Monthly Installment": monthly_installment,
        "Total Amount Payable": total_amount_payable,
        "DSR": dsr,
    })


# Option 2: Display Previous Loan Calculations
def display_previous_calculations():
    # If user's do not have previous loan calculations
    if not loan_calculations:
        print("\nNo Previous loan calculations.")
    else:
    # If user's have previous loan calculations 
        print("\nPrevious loan calculations:")
        for index, calculation in enumerate(loan_calculations, start=1):
            print(f"\nHousing Loan Calculation {index}:")
            print(f"Principal: RM{calculation['Principal']:.2f}")
            print(f"Monthly Installment: RM{calculation['Monthly Installment']:.2f}")
            print(f"Total Amount Payable: RM{calculation['Total Amount Payable']:.2f}")
            print(f"DSR: {calculation['DSR']:.2f}%")


# Option 3: Delete Previous Calculation
def delete_previous_calculation():
    try: 
        # If user's do not have previous loan to delete
        if not loan_calculations:
            print("\nNo previous loan calculations to delete.")
        else:
            try:
                index_to_delete = int(input("\nPlease enter the index of the calculation to delete: ")) - 1
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")
                return
                
            if 0 <= index_to_delete < len(loan_calculations):
                deleted_calculation = loan_calculations.pop(index_to_delete)
                print(f"\nCalculation {index_to_delete + 1} successfully deleted.")
            else:
                print("\nError: Invalid input. Please enter a valid index.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Option 4: Modify the DSR threshold
def modify_dsr_threshold():
    try:
        # Modify DSR Threshold between 0 and 100
        modified_dsr = float(input("Please enter the new DSR threshold: "))

        # Check if the entered DSR threshold is valid
        if 0 <= modified_dsr <= 100:
            # Recalculate DSR
            # Check eligibility based on the modified threshold
            if 0 < dsr_threshold < 100 and dsr_threshold <= modified_dsr:
                print(f"\nCongratulations! You are eligible to apply for a housing loan with a DSR of {dsr_threshold:.2f}%.")
            else:
                print(f"\nSorry, your DSR of {dsr_threshold:.2f}% does not meet the eligibility criteria for a housing loan.")

            print(f"\nDSR threshold successfully modified to {modified_dsr:.2f}%.")
        else:
            print("\nInvalid DSR threshold. Please enter a value between 0 and 100.")
    except ValueError:
        print("\nInvalid input. Please enter a valid numeric value for the DSR threshold.")


# Main loop for the system
def main():
    load_calculations_from_file()
    login()

    while True:
        print("\nPlease choose one of the options below:")
        # Display menu options for users to choose
        # Five options available for the users to choose from as shown in below
        print("1. Calculate New Housing Loan")
        print("2. Display Previous Loan Calculations")
        print("3. Delete Previous Calculations")
        print("4. Modify DSR Threshold")
        print("5. Exit the program")

        # User's options
        option = input("\nPlease enter your option (1/2/3/4/5): ")

        #If choose Option 1
        if option == '1':
            calculate_new_loan()
        #If choose Option 2
        elif option == '2':
            display_previous_calculations()
        #If choose Option 3
        elif option == '3':
            delete_previous_calculation()
        #If choose Option 4
        elif option == '4':
            modify_dsr_threshold()
        #If choose Option 5
        elif option == '5':
            save_calculations_to_file()
            print("\nLogging out program. Thank you for using this program!")
            break
        else:
            print("\nError: Invalid option. Please enter 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()