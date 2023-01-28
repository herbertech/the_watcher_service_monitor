from flask import Flask, render_template
import config
import service_info

app = Flask(__name__)

services_list = config.services_to_monitor
service_handler = service_info.service_data(services=services_list)

@app.route('/')
def service_returner():
    services_status_dict_list = []
    for service in services_list:
        services_status_dict_list.append(service_handler.get_status(service))
    return render_template('index.html', services_status=services_status_dict_list)