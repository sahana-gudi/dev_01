# dev_01
def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        print(check_voting_eligibility(age))
    except ValueError:
        print("Please enter a valid number.")
