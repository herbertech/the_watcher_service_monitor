import subprocess

class service_data:
    def __init__(self, services):
        self.services = services

    def get_status(self, service_name):
        service_status = subprocess.call(['systemctl', 'is-active', '--quiet', service_name], stdout=subprocess.PIPE)
        return {'name': service_name, 'status': service_status}