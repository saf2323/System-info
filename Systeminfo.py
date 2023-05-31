import platform, psutil
os1 = platform.platform()
vm = psutil.virtual_memory()
tvm = vm.total
ac = platform.architecture()

print('Batter power:',psutil.sensors_battery().percent,'%')
print('OS:',os1)
print('Machine:',platform.machine())
print('Processor:',platform.processor())
print('Design:', ac)
print('Network name:',platform.node())
print('CPU percentage:',psutil.cpu_percent())
print('Total RAM:',tvm/1024/1024/1024,'GB')