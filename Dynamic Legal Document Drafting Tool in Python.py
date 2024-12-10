#!/usr/bin/env python
# coding: utf-8
Creating a Python program for legal drafting requires a dynamic approach where users can input details, select drafting options, and view the output without errors. Here’s a complete program:
# In[ ]:


def draft_legal_document():
    print("\nWelcome to Legal Drafting Tool")
    print("Choose the type of legal document you want to draft:")
    print("1. Employment Agreement")
    print("2. Non-Disclosure Agreement (NDA)")
    print("3. Rent Agreement")
    print("4. Termination Letter")
    print("5. Exit\n")

    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                employment_agreement()
            elif choice == 2:
                nda_agreement()
            elif choice == 3:
                rent_agreement()
            elif choice == 4:
                termination_letter()
            elif choice == 5:
                print("Exiting Legal Drafting Tool. Thank you!")
                break
            else:
                print("Invalid input. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def employment_agreement():
    print("\n--- Employment Agreement Drafting ---")
    employer = input("Enter Employer's Name: ")
    employee = input("Enter Employee's Name: ")
    position = input("Enter Position Title: ")
    salary = input("Enter Salary (per annum): ")
    joining_date = input("Enter Joining Date (DD-MM-YYYY): ")

    print("\n--- Employment Agreement ---")
    print(f"THIS EMPLOYMENT AGREEMENT is made and entered into as of {joining_date}, by and between {employer} ('Employer') and {employee} ('Employee').")
    print(f"The Employer agrees to employ the Employee in the position of {position} with a salary of {salary} per annum.\n")

def nda_agreement():
    print("\n--- Non-Disclosure Agreement Drafting ---")
    disclosing_party = input("Enter Disclosing Party's Name: ")
    receiving_party = input("Enter Receiving Party's Name: ")
    effective_date = input("Enter Effective Date (DD-MM-YYYY): ")

    print("\n--- Non-Disclosure Agreement ---")
    print(f"THIS NON-DISCLOSURE AGREEMENT is made and entered into on {effective_date}, by and between {disclosing_party} and {receiving_party}.")
    print(f"The parties agree to protect and not disclose confidential information shared between them.\n")

def rent_agreement():
    print("\n--- Rent Agreement Drafting ---")
    landlord = input("Enter Landlord's Name: ")
    tenant = input("Enter Tenant's Name: ")
    property_address = input("Enter Property Address: ")
    rent_amount = input("Enter Monthly Rent Amount: ")
    lease_start_date = input("Enter Lease Start Date (DD-MM-YYYY): ")

    print("\n--- Rent Agreement ---")
    print(f"THIS RENT AGREEMENT is made and entered into on {lease_start_date}, by and between {landlord} ('Landlord') and {tenant} ('Tenant').")
    print(f"The property located at {property_address} is leased to the Tenant at a monthly rent of {rent_amount}.\n")

def termination_letter():
    print("\n--- Termination Letter Drafting ---")
    employer = input("Enter Employer's Name: ")
    employee = input("Enter Employee's Name: ")
    termination_date = input("Enter Termination Date (DD-MM-YYYY): ")
    reason = input("Enter Reason for Termination: ")

    print("\n--- Termination Letter ---")
    print(f"Dear {employee},")
    print(f"We regret to inform you that your employment with {employer} will be terminated effective {termination_date}.")
    print(f"Reason for Termination: {reason}.")
    print("We wish you all the best in your future endeavors.\n")

# Run the program
draft_legal_document()


# In[ ]:




