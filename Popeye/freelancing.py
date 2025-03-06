import os
import requests

class FreelancingManager:
    def __init__(self):
        self.commands = ["manage freelancing tasks", "generate invoices"]
        self.upwork_api_key = os.getenv("UPWORK_API_KEY")
        self.upwork_base_url = "https://www.upwork.com/api/v3/"

    def execute(self, command):
        if command == "manage freelancing tasks":
            self.manage_tasks()
        elif command == "generate invoices":
            self.generate_invoices()

    def manage_tasks(self):
        print("Managing freelancing tasks...")
        jobs = self.find_upwork_jobs()
        for job in jobs:
            if self.is_relevant_job(job):
                self.apply_to_job(job)

    def find_upwork_jobs(self):
        url = f"{self.upwork_base_url}jobs/search"
        headers = {
            "Authorization": f"Bearer {self.upwork_api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("jobs", [])
        else:
            print("Failed to retrieve jobs")
            return []

    def is_relevant_job(self, job):
        keywords = ["python", "automation", "AI"]
        return any(keyword in job["title"].lower() for keyword in keywords)

    def apply_to_job(self, job):
        url = f"{self.upwork_base_url}proposals"
        headers = {
            "Authorization": f"Bearer {self.upwork_api_key}"
        }
        data = {
            "job_id": job["id"],
            "cover_letter": "I am an AI assistant capable of performing this task autonomously."
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            print(f"Applied to job {job['id']}")
        else:
            print(f"Failed to apply to job {job['id']}")

    def generate_invoices(self):
        print("Generating invoices...")
        # Add invoice generation logic here