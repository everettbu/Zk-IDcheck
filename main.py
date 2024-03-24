import subprocess
import os

def truffle_migrate():
    print("Running truffle migrate...")
    # Run truffle migrate
    subprocess.run(["truffle", "migrate"])

def truffle_test():
    print("Running truffle test...")
    # Run truffle migrate
    subprocess.run(["truffle", "test"])

def run_zk_proof():
    print("Running zk-proof...")
    subprocess.run(["python3", "zk-proof/check.py"])  # Adjust the path as needed

if __name__ == "__main__":
    truffle_migrate()
    truffle_test()
    run_zk_proof()
