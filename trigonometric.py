import math


angle = float(input("Enter angle in degrees: "))

radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print("Sin:", sin_value)
print("Cos:", cos_value)
print("Tan:", tan_value)
