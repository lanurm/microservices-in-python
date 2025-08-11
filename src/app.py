from flask import Flask, jsonify,render_template
import socket

app = Flask(__name__)

# function to fetch host_name name and hostIP
def fetch_details():
    host_name=socket.gethostname()
    host_ip=socket.gethostbyname(host_name)
    print("Hostname:",host_name)
    print("IP :",host_ip)
    return str(host_name),str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    host_name,ip=fetch_details()
    return render_template('index.html',HOSTNAME=host_name,IP=ip)
app.run(debug=True, host="0.0.0.0", port=5000)

