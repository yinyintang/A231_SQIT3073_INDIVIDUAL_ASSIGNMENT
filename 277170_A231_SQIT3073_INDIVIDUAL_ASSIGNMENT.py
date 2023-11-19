# A231 SQIT3073 INDIVIDUAL ASSIGNMENT (HOUSING LOAN ELIGIBILITY AND DSR CALCULATOR)

import os 
# Windows 
os.system('cls')
# Mac
# os.system('clear')

# Initialize an empty list to store loan calculations
loan_calculations = []

# User credentials for login system
user_credentials = {"user_id": "sqit3073", "password": "1234"}

# Login system
def login():
    while True:
        print("User Login:")
        user_id = input("Please enter your user ID: ")
        password = input("Please enter your password: ")

        if user_id == user_credentials["user_id"] and password == user_credentials["password"]:
            print("\nLogin successful! Welcome to the Housing Loan Eligibility and DSR Calculators!\n")
            break
        else:
            print("\nInvalid username or password. Please try again!")


# Calculate New Loan
def calculate_new_loan():
    print("\nPlease enter loan details:")
     
    # User's principal loan amount
    principal_loan_amount = float(input("Principal loan amount (RM): "))
        
    # User's annual interest rate
    annual_interest_rate = float(input("Annual interest rate (%): "))
       
    # User's loan term in years
    loan_term_years = int(input("Loan term in years: "))
        
    # User's monthly income
    monthly_income = float(input("Applicant's monthly income (RM): "))
       
    # User's other monthly financial commitments
    other_commitments = float(input("Other monthly financial commitments (RM): "))

    
    # Calculate loan details
        
    # Function to calculate monthly installment for housing loan details
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    num_payments = loan_term_years * 12
    monthly_installment = (principal_loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** - num_payments)
       
    # Function to calculate total amount payable over the term of the loan
    total_amount_payable = monthly_installment * loan_term_years * 12
       
    # Function to calculate the Debt Service Ratio (DSR)
    total_commitments = other_commitments + monthly_installment
    dsr = (total_commitments / monthly_income) * 100

    # Display housing loan details
    print("\nLoan Details:")
    print(f"Monthly Installment: RM{monthly_installment:.2f}")
    print(f"Total Amount Payable: RM{total_amount_payable:.2f}")
    print(f"Debt Service Ratio (DSR): {dsr:.2f}%")

    # Assume the threshold for DSR is 70%.
    # Check eligibility
    if dsr <= 70:
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


# Display Previous Loan Calculations
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


# Delete Previous Calculation
def delete_previous_calculation():
    # If user's do not have previous loan to delete
    if not loan_calculations:
        print("\nNo previous loan calculations to delete.")
    else:
        index_to_delete = int(input("\nPlease enter the index of the calculation to delete: ")) - 1
        if 0 <= index_to_delete < len(loan_calculations):
            deleted_calculation = loan_calculations.pop(index_to_delete)
            print(f"Calculation {index_to_delete + 1} successfully deleted.")
        else:
            print("Invalid input. Please enter a valid index.")


# Main loop for the system
def main():
    login()

    while True:
        print("\nPlease choose one of the options below:")
        # Display menu options for users to choose
        # Four options available for the users to choose from as shown in below
        print("1. Calculate New Housing Loan")
        print("2. Display Previous Loan Calculations")
        print("3. Delete Previous Calculations")
        print("4. Exit the program")

        # User's options
        option = input("\nPlease enter your option (1/2/3/4): ")

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
            print("Logging out program. Thank you for using this program!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()