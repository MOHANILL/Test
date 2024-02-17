# Python program to display platform processor
  
# import module
import platform
  
# displaying platform processor
print('Platform processor:', platform.processor())

# Python program to display platform architecture
  

# displaying platform architecture
print('Platform architecture:', platform.architecture())
# displaying machine type
print('Machine type:', platform.machine())
# displaying system network name
print("System's network name:", platform.node())
# displaying platform information
print('Platform information:', platform.platform())
# displaying platform processor name
print('System info:', platform.system())
# displaying python build date and no.
print('Python build no. and date:', platform.python_build())
# displaying python compiler
print('Python compiler:', platform.python_compiler())
# displaying python SCM info
print('Python SCM:', platform.python_compiler())
print(platform.win32_ver())