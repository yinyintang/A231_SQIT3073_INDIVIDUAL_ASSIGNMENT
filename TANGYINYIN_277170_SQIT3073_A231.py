
# Initialize an empty list to store loan calculations
loan_calculations = []

# User credentials for login system
user_credentials = {"user_id": "sqit3073", "password": "1234"}

# Login system
while True:
    print("Login:")
    user_id = input("Please enter your user ID: ")
    password = input("Please enter your password: ")

    if user_id == user_credentials["user_id"] and password == user_credentials["password"]:
        print("Login successful! Welcome to the Housing Loan Eligibility and DSR Calculators!\n")
        break
    else:
        print("Invalid username or password. Please try again!")
        
# Main loop
while True:
    # Display the menu options
    print("\nMenu:")
    print("1. Calculate New Loan")
    print("2. Display All Previous Loan Calculations")
    print("3. Delete Previous Calculations")
    print("4. Exit")

    # User's option
    option = input("Enter your option (1, 2, 3 or 4): ")

    if option == '1':
        # Calculate New Loan
        print("Enter loan details:")
        principal_loan_amount = float(input("Principal loan amount (RM): "))
        annual_interest_rate = float(input("Annual interest rate (%): "))
        loan_term_years = int(input("Loan term in years: "))
        monthly_income = float(input("Applicant's monthly income (RM): "))
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

        # Display loan details
        print("\nLoan Details:")
        print(f"Monthly Installment: ${monthly_installment:.2f}")
        print(f"Total Amount Payable: ${total_amount_payable:.2f}")
        print(f"Debt Service Ratio (DSR): {dsr:.2f}%")

        # Check eligibility
        if dsr <= 70:
            print("Congratulations! You are eligible for the loan.")
        else:
            print("Sorry, you are not eligible for the loan.")
        
        # Store loan calculation details in the list
        loan_calculations.append({
            "Principal": principal_loan_amount,
            "Interest Rate": annual_interest_rate,
            "Loan Term": loan_term_years,
            "Monthly Income": monthly_income,
            "Monthly Installment": monthly_installment,
            "Total Amount Payable": total_amount_payable,
            "DSR": dsr,
        })

    elif option == '2':
        # Display All Previous Loan Calculations
        if not loan_calculations:
            print("No previous loan calculations.")
        else:
            print("\nPrevious Loan Calculations:")
            for index, calculation in enumerate(loan_calculations, start=1):
                print(f"\nCalculation {index}:")
                print(f"Principal: ${calculation['Principal']:.2f}")
                print(f"Monthly Installment: ${calculation['Monthly Installment']:.2f}")
                print(f"Total Amount Payable: ${calculation['Total Amount Payable']:.2f}")
                print(f"DSR: {calculation['DSR']:.2f}%")

    elif option == '3':
        # Delete Previous Calculation
        if not loan_calculations:
            print("No previous loan calculations to delete.")
        else:
                index_to_delete = int(input("Enter the index of the calculation to delete: ")) - 1
                if 0 <= index_to_delete < len(loan_calculations):
                    deleted_calculation = loan_calculations.pop(index_to_delete)
                    print(f"Calculation {index_to_delete + 1} deleted.")
                else:
                    print("Invalid index.")

    elif option == '4':
         # Exit the program
            print("Logging out program. Goodbye!")
            break

    else:
            print("Invalid option. Please enter 1, 2, 3 or 4.")