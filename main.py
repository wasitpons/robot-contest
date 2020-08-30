from config.init import init_sensor, clear_sensor

try:
    init_sensor()
    
except Exception as err:
    print(err)

finally:
    clear_sensor()