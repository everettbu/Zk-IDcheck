import hashlib
import os
import random
from datetime import datetime, timedelta

class ZKProof:
    def __init__(self):
        self.N = 20
        self.salt = os.urandom(16)

    def _hash(self, x):
        return hashlib.sha256(x.encode('utf-8') + self.salt).hexdigest()

    def generate_proof(self, secret):
        self.secret = secret
        self.v = self._hash(secret)
        r = str(random.randint(1, self.N))
        self.x = self._hash(r)
        return self.x

    def get_secret(self):
        return self.secret

    def verify(self, response):
        return self.v == self._hash(response)

    def verify_date(self, response_date):
        current_date = datetime.now()
        response_date = datetime.strptime(response_date, '%Y-%m-%d')
        # Calculate the difference in years
        delta_years = current_date.year - response_date.year - ((current_date.month, current_date.day) < (response_date.month, response_date.day))
        # Check if the difference is exactly 21 years
        return delta_years == 21
