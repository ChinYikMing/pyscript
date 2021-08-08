#!/usr/bin/python

class Employee:
    name = ""
    job_list = []

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print("%s" % (self.name))

    def set_job(self, job):
        self.job_list.insert(0, job)
        print("Successfully insert job: %s" % job)

    def get_job(self):
        if len(self.job_list) == 0:
            print("No job")
        else:
            for job in self.job_list:
                print(job)

employee = Employee("Ming")

employee.get_name()

employee.get_job()

employee.set_job("coding")
employee.set_job("eating")
employee.set_job("exercising")

employee.get_job()