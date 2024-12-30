import math
import time
from datetime import datetime, timedelta

INSTALLED_POWER = 3.0  # 3 kW installed power
SIMULATION_SECONDS = 100  # Simulation time in seconds (instead of 365 days)
REACTIVE_POWER_RATIO = 0.1  # Reactive power is 10% of active power

class PowerData:
    def __init__(self):
        self.active_power_sum1 = 0.0
        self.active_power_sum2 = 0.0
        self.reactive_power_sum1 = 0.0
        self.reactive_power_sum2 = 0.0
        self.max_active_power = 0.0
        self.last_max_power_date = datetime.now()
        self.last_month_max_power = 0.0
        self.start_date = datetime.now()

def is_in_tariff_i(hour):
    return (6 <= hour < 13) or (15 <= hour < 22)

def simulate_active_power(time):
    return (math.sin(time * math.pi / 180) + 1) * INSTALLED_POWER / 2

def process_power_readings(data, active_power, reactive_power, current_time, current_hour):
    if is_in_tariff_i(current_hour):
        data.active_power_sum1 += active_power
        data.reactive_power_sum1 += reactive_power
    else:
        data.active_power_sum2 += active_power
        data.reactive_power_sum2 += reactive_power

    current_month = current_time.month
    last_max_month = data.last_max_power_date.month

    if current_month != last_max_month or data.last_month_max_power == 0:
        data.last_month_max_power = data.max_active_power
        data.max_active_power = active_power
        data.last_max_power_date = current_time
    elif active_power > data.max_active_power:
        data.max_active_power = active_power
        data.last_max_power_date = current_time

def display_results(data):
    print('=== Raport zużycia energii ===')
    print(f'Moc Czynna (Taryfa I): {data.active_power_sum1:.2f} kWh')
    print(f'Moc Bierna (Taryfa I): {data.reactive_power_sum1:.2f} kVArh')
    print(f'Moc Czynna (Taryfa II): {data.active_power_sum2:.2f} kWh')
    print(f'Moc Bierna (Taryfa II): {data.reactive_power_sum2:.2f} kVArh')
    print(f'Moc maksymalna w ostatnim miesiącu: {data.last_month_max_power:.2f} kW')
    print(f'Moc maksymalna w obecnym miesiącu: {data.max_active_power:.2f} kW')
    print('==============================')

def control_program(data):
    for elapsed_seconds in range(SIMULATION_SECONDS + 1):
        current_time = data.start_date + timedelta(seconds=elapsed_seconds)
        current_hour = current_time.hour

        active_power = simulate_active_power(elapsed_seconds)
        reactive_power = active_power * REACTIVE_POWER_RATIO

        process_power_readings(data, active_power, reactive_power, current_time, current_hour)
        display_results(data)

        time.sleep(0.1)

if __name__ == "__main__":
    power_data = PowerData()
    control_program(power_data)
    input('Wcisnij Enter aby wyjść z programu...')