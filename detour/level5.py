LENGTH_CONVERSIONS = {
  "meters": 1.0,
  "kilometers": 0.001,
  "centmeters": 100.0,
  "miles": 0.000621371,
  "feet": 3.28084,
}

WEIGHT_CONVERSIONS = {
  "grams": 1.0,
  "kilograms": 0.001,
  "pounds": 0.00220462,
  "ounces": 0.035274,
}

def convert_units(value, from_unit, to_unit, conversion_dict):
  #Converts standard units using a dictionary as a lookup table
  if from_unit not in conversion_dict or to_unit not in conversion_dict:
    return None
  #Convert to base unit first, then to target unit
  base_value = value / conversion_dict[from_unit]
  return base_value * conversion_dict[to_unit]

def convert_temperature(value, from_scale, to_scale):
  if from_scale == "celcius":
    celcius = value
  elif from_scale == "fahrenheit":
    celcius = (value - 32) * 5/9
  elif from_scale == "kelvin":
    return celcius + 273.15
  else:
    return None


  