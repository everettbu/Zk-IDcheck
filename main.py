import subprocess
import os

def truffle_migrate():
    print("Running truffle migrate...")
    # Change working directory to id-card-creation
    os.chdir("digital-id")
    # Run truffle migrate
    subprocess.run(["truffle", "migrate"])
    # Change working directory back to the root
    os.chdir("..")

def truffle_test():
    print("Running truffle test...")
    # Change working directory to id-card-creation
    os.chdir("digital-id")
    # Run truffle migrate
    subprocess.run(["truffle", "test"])
    # Change working directory back to the root
    os.chdir("..")

def run_zk_proof():
    print("Running zk-proof...")
    subprocess.run(["python3", "zk-proof/check.py"])  # Adjust the path as needed

if __name__ == "__main__":
    truffle_migrate()
    truffle_test()
    run_zk_proof()
