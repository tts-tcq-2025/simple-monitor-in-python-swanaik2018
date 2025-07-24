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

def battery_is_ok(temp, soc, rate, reporter=print):
checks = [
is_temperature_ok(temp),
is_soc_ok(soc),
is_charge_rate_ok(rate)
]
for ok, msg in checks:
if not ok:
reporter(msg)
return False
return True

if __name__ == '__main__':
assert(battery_is_ok(25, 70, 0.7) is True)
assert(battery_is_ok(50, 85, 0) is False)
assert(battery_is_ok(-1, 50, 0.7) is False)
assert(battery_is_ok(25, 10, 0.7) is False)
assert(battery_is_ok(25, 50, 0.9) is False)
