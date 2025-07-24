def is_temperature_ok(temp, reporter):
  if temp < 0:
    reporter("Temperature too low!")
    return False
  if temp > 45:
    reporter("Temperature too high!")
    return False
  return True

def is_soc_ok(soc, reporter):
  if soc < 20:
    reporter("State of Charge too low!")
    return False
  if soc > 80:
    reporter("State of Charge too high!")
    return False
  return True

def is_charge_rate_ok(rate, reporter):
  if rate > 0.8:
    reporter("Charge rate too high!")
    return False
  return True

def battery_is_ok(temp, soc, rate, reporter=print):
  return (
    is_temperature_ok(temp, reporter) and
    is_soc_ok(soc, reporter) and
    is_charge_rate_ok(rate, reporter)
  )

# Tests
if __name__ == "__main__":
  assert battery_is_ok(25, 70, 0.7) is True
  assert battery_is_ok(50, 85, 0) is False
