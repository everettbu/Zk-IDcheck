from zkp import ZKProof

zkp = ZKProof()

# Generate proof for a date
secret_date = '2000-01-01'  # Date format: YYYY-MM-DD
x = zkp.generate_proof(secret_date)
print('Proof:', x)

# Verify if a date is 21 years before the current date
response_date = input('Enter the date to verify (YYYY-MM-DD): ')
print('Verified:', zkp.verify_date(response_date))