import boto3
from flask import Flask, jsonify
from prometheus_client import Counter, start_http_server
import threading

# Prometheus Counter
Counters = Counter('http_request_total', 'Total Number Of Requests')

app = Flask(__name__)
client = boto3.client('ecs', region_name="us-east-1")

def get_clusters():
    return client.list_clusters()

@app.route('/ecs/list-cluster', methods=['GET'])
def list_cluster():
    Counters.inc()
    cluster_arns = get_clusters().get('clusterArns', [])
    return jsonify({"success": True, "clusters": cluster_arns})

@app.route('/ecs/list-tasks', methods=['GET'])
def list_tasks():
    Counters.inc()
    tasks = []
    details = get_clusters().get('clusterArns', [])
    for detail in details:
        response = client.list_tasks(cluster=detail)
        tasks.append(response.get('taskArns', []))
    return jsonify({"clusters": details, "tasks": tasks})

# Start Prometheus HTTP Server in a separate thread
def start_prometheus():
    start_http_server(9000, addr="127.0.0.1")  # Change to 9000 if needed

if __name__ == '__main__':
    threading.Thread(target=start_prometheus, daemon=True).start()
    app.run(debug=False, port=8080, host='0.0.0.0')