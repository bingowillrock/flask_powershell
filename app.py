from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/initiate_ssh', methods=['POST'])
def initiate_ssh():
    try:
        # Define static IP address and username
        ip_address = "192.168.1.1"
        username = os.getlogin()
        port_number = "22"
        
        # Customize the command to open a new PowerShell window with the static IP address and dynamic username
        command = f"powershell -NoExit -Command \"Start-Process powershell -ArgumentList 'ssh {username}@{ip_address} -p {port_number}'\""
        subprocess.Popen(command, shell=True)
        
        return jsonify({'status': 'success', 'message': 'SSH session initiated successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
