from flask import Flask, render_template
from flask_socketio import SocketIO
import psutil
import time
import random
import platform  

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def get_cpu_data():
    try:
        load_avg = psutil.getloadavg()  # Load averages for the last 1, 5, and 15 minutes
        
        return {
            'utilization': psutil.cpu_percent(interval=1),
            'processes': len(psutil.pids()),
            'temperature': random.uniform(30.0, 70.0),  # Mock temperature
            'load_average': load_avg,
            'model_name': platform.processor(),  # CPU model name
            'cache_size': 'L1: 32KB, L2: 256KB, L3: 8MB',  # Mocked values
            'interrupts': psutil.cpu_stats().interrupts,
        }
    except Exception as e:
        print(f"Error getting CPU data: {e}")
        return {}

def get_memory_data():
    try:
        memory = psutil.virtual_memory()
        return {
            'total_memory': memory.total,
            'used_memory': memory.used,
            'free_memory': memory.free,
            'cached_memory': memory.cached if hasattr(memory, 'cached') else 0,  # Handle missing attribute
            'buffered_memory': memory.buffers if hasattr(memory, 'buffers') else 0,  # Handle missing attribute
            'available_memory': memory.available,
            'swap_memory': psutil.swap_memory().used,
        }
    except Exception as e:
        print(f"Error getting memory data: {e}")
        return {}

def get_battery_data():
    try:
        battery = psutil.sensors_battery()
        return {
            'percentage': battery.percent,
            'power_plugged': battery.power_plugged,
            'time_remaining': battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else None,
        }
    except Exception as e:
        print(f"Error getting battery data: {e}")
        return {}

def emit_system_data():
    while True:
        cpu_data = get_cpu_data()
        memory_data = get_memory_data()
        battery_data = get_battery_data()

        socketio.emit('cpu_update', cpu_data)
        socketio.emit('memory_update', memory_data)
        socketio.emit('battery_update', battery_data)

        time.sleep(5)  # Update every 5 seconds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cpu')
def cpu():
    return render_template('cpu.html')

@app.route('/memory')
def memory():
    return render_template('memory.html')

@app.route('/battery')
def battery():
    return render_template('battery.html')

if __name__ == '__main__':
    socketio.start_background_task(emit_system_data)  # Start background task to emit data
    socketio.run(app, debug=True)
