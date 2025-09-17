# sys_stats.py
import psutil

print("psutil:", psutil.__version__)
print("CPU cores (logical):", psutil.cpu_count())
print("CPU usage (1s sample):", psutil.cpu_percent(interval=1), "%")
print("Memory percent:", psutil.virtual_memory().percent)
print(f"battery: {psutil.sensors_battery().percent}%")
print(f"users:{psutil.users()}")