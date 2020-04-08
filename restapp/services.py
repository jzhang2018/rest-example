import requests


class AWXTest:
    def callawx(self):
        print("=============== service call to AWX Ansible job =============")
        response = requests.post('http://192.168.187.155/api/v2/job_templates/21/launch/', auth=('admin', 'devops'))
        print(response)

        return response
