使用前：pip install speedtest-cli psutil


import speedtest
import psutil
import platform

def get_network_speed():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    return download_speed, upload_speed

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_system_info():
    system_info = platform.system() + " " + platform.version()
    return system_info

def main():
    network_speed = get_network_speed()
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    system_info = get_system_info()

    print(f"System Information: {system_info}")
    print(f"Download Speed: {network_speed[0] / 10**6:.2f} Mbps")
    print(f"Upload Speed: {network_speed[1] / 10**6:.2f} Mbps")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

if __name__ == "__main__":
    main()
