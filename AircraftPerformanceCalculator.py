#calculate lift and drag of a aircraft at diff altitudes with aircraft model, and its wing surface area, and velocity at that height

print('===AIRCRAFT PERFORMANCE CALCULATOR===')

#Constants
GRAVITY = 9.81  # m/s^2
AIR_DENSITY = 1.225  # kg/m^3
lift_coefficient = 1.2
drag_coefficient = 0.02

#User Inputs
aircraft_model = input('Enter the aircraft model: ')
wing_surface_area = float(input('Enter the wing surface area (in m^2): '))
altitude = float(input('Enter the altitude (in meters): '))
velocity = float(input('Enter the velocity (in m/s): '))

# Calculate air density at the given altitude using the barometric formula
def air_density_at_altitude(altitude):
    # Simplified model for air density decrease with altitude
    if altitude < 11000:  # Troposphere
        return AIR_DENSITY * (1 - (0.0065 * altitude) / 288.15) ** 5.2561
    else:  # Above Troposphere
        return AIR_DENSITY * (1 - (0.0065 * 11000) / 288.15) ** 5.2561 * (1 - (0.0065 * (altitude - 11000)) / 216.65) ** 11.388

# Calculate lift and drag
def calculate_lift(wing_surface_area, air_density, velocity):
    return 0.5 * air_density * (velocity ** 2) * wing_surface_area * lift_coefficient

def calculate_drag(wing_surface_area, air_density, velocity):
    return 0.5 * air_density * (velocity ** 2) * wing_surface_area * drag_coefficient

# Main Calculation
air_density = air_density_at_altitude(altitude)
lift = calculate_lift(wing_surface_area, air_density, velocity)
drag = calculate_drag(wing_surface_area, air_density, velocity)

# Output Results
print('\n===RESULTS===')
print(f'\nAircraft Model:{aircraft_model}')
print(f'Altitude: {altitude} m')
print(f'Air Density at Altitude: {air_density} kg/m^3')
print(f'Lift: {lift} N')
print(f'Drag: {drag} N')
