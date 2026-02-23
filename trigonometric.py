import math

# Ask user for angle in degrees
angle = float(input("Enter angle in degrees: "))

# Convert degrees to radians
radians = math.radians(angle)

# Calculate trigonometric values
sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

# Display results
print("Sin:", sin_value)
print("Cos:", cos_value)
print("Tan:", tan_value)