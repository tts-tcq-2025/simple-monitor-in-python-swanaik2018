# check_limits.py

def is_temperature_ok(temp):
if temp < 0:
return (False, "Temperature too low!")
if temp > 45:
return (False, "Temperature too high!")
return (True, "")

def is_soc_ok(soc):
if soc < 20:
return (False, "State of Charge too low!")
if soc > 80:
return (False, "State of Charge too high!")
return (True, "")

def is_charge_rate_ok(rate):
if rate > 0.8:
return (False, "Charge Rate too high!")
return (True, "")

def battery_is_ok(temperature, soc, charge_rate, reporter=print):
if temperature < 0:
reporter("Temperature too low!")
return False
if temperature > 45:
reporter("Temperature too high!")
return False
if soc < 20:
reporter("State of Charge too low!")
return False
if soc > 80:
reporter("State of Charge too high!")
return False
if charge_rate > 0.8:
reporter("Charge rate too high!")
return False
return True

if __name__ == "__main__":
assert battery_is_ok(25, 70, 0.7) is True
assert battery_is_ok(50, 85, 0) is False 
