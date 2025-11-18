# Assignment 5: Data Processing Challenge
# Given list of daily temperatures
temps = [72, 75, 68, 71, 73, 69, 74, 76, 78, 71, 69, 72, 74, 77, 75, 70, 68, 71, 73, 76, 78, 74, 72, 69, 71, 73, 75, 77, 74, 71]

# 1. Find hottest and coldest days
max_temp = max(temps)
min_temp = min(temps)
hottest_day = temps.index(max_temp) + 1  # Day number (1-based)
coldest_day = temps.index(min_temp) + 1  # Day number (1-based)

# 2. Calculate average temperature
avg_temp = sum(temps) / len(temps)

# 3. Find days with temperatures above average
above_avg_days = [i + 1 for i, t in enumerate(temps) if t > avg_temp]

# 4. Group temperatures into ranges
cold_temps = [t for t in temps if t < 70]
mild_temps = [t for t in temps if 70 <= t <= 75]
warm_temps = [t for t in temps if t > 75]
cold_count = len(cold_temps)
mild_count = len(mild_temps)
warm_count = len(warm_temps)

# 5. Find longest streak of consecutive days above 73 degrees
streak = 0
max_streak = 0
for t in temps:
    if t > 73:
        streak += 1
        max_streak = max(max_streak, streak)
    else:
        streak = 0

# 6. Detect temperature anomalies (differ by more than 5 degrees from previous day)
anomalies = []
for i in range(1, len(temps)):
    if abs(temps[i] - temps[i - 1]) > 5:
        anomalies.append(i + 1)  # Day number (1-based)

# Output
print("Statistical Summary:")
print(f"- Hottest day: Day {hottest_day} with {max_temp}°F")
print(f"- Coldest day: Day {coldest_day} with {min_temp}°F")
print(f"- Average temperature: {avg_temp:.2f}°F")
print(f"- Days above average: {above_avg_days}")

print("\nCategorized Data:")
print(f"- Cold (<70°F): {cold_count} days, temperatures: {cold_temps}")
print(f"- Mild (70-75°F): {mild_count} days, temperatures: {mild_temps}")
print(f"- Warm (>75°F): {warm_count} days, temperatures: {warm_temps}")

print("\nPatterns and Anomalies:")
print(f"- Longest streak of consecutive days above 73°F: {max_streak} days")
print(f"- Anomalies (temperature differs by more than 5°F from previous day): Days {anomalies}")
