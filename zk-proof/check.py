from zkp import ZKProof

zkp = ZKProof()

# Verify if a date is 21 years before the current date
response_date = input('Enter the date to verify (YYYY-MM-DD): ')
print('Verified:', zkp.verify_date(response_date))