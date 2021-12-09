from submarine import SubmarineAim
submarine_instance = SubmarineAim()
from utils import diagnostic_bits
submarine_instance.get_gamma_decimal(diagnostic_bits)
submarine_instance.get_epsilon_decimal(diagnostic_bits)
submarine_instance.calculate_power_consumption(diagnostic_bits)
print(submarine_instance.gamma_decimal)
print(submarine_instance.epsilon_decimal)
print(f'Power consumption: {submarine_instance.power_consumption}')