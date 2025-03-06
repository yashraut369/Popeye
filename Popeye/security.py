import subprocess

class SecurityManager:
    def __init__(self):
        self.commands = ["audit dependencies", "run static analysis"]

    def execute(self, command):
        if command == "audit dependencies":
            self.audit_dependencies()
        elif command == "run static analysis":
            self.run_static_analysis()

    def audit_dependencies(self):
        print("Auditing dependencies for vulnerabilities...")
        result = subprocess.run(["pip-audit"], capture_output=True, text=True)
        print(result.stdout)

    def run_static_analysis(self):
        print("Running static analysis with Bandit...")
        result = subprocess.run(["bandit", "-r", "."], capture_output=True, text=True)
        print(result.stdout)