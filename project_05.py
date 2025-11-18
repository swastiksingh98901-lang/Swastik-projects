# Given list of daily temperatures
temperatures = [72, 75, 68, 71, 73, 69, 74, 76, 78, 71, 69, 72, 74, 77, 75, 70, 68, 71, 73, 76, 78, 74, 72, 69, 71, 73, 75, 77, 74, 71]

# Find the hottest and coldest days
hottest = max(temperatures)
coldest = min(temperatures)
print(f"Hottest day: {hottest}°F")
print(f"Coldest day: {coldest}°F")

# Calculate the average temperature
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp:.2f}°F")

# Find all days with temperatures above average
above_average_days = [i+1 for i, temp in enumerate(temperatures) if temp > average_temp]
print(f"Days above average (1-indexed): {above_average_days}")

# Group temperatures into ranges: Cold (<70), Mild (70-75), Warm (>75)
cold = [temp for temp in temperatures if temp < 70]
mild = [temp for temp in temperatures if 70 <= temp <= 75]
warm = [temp for temp in temperatures if temp > 75]
print(f"Cold temperatures (<70): {cold} (Count: {len(cold)})")
print(f"Mild temperatures (70-75): {mild} (Count: {len(mild)})")
print(f"Warm temperatures (>75): {warm} (Count: {len(warm)})")

# Find the longest streak of consecutive days above 73 degrees
max_streak = 0
current_streak = 0
for temp in temperatures:
    if temp > 73:
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0
print(f"Longest streak above 73°F: {max_streak} days")

# Detect temperature anomalies (differ by more than 5 degrees from the previous day)
anomalies = []
for i in range(1, len(temperatures)):
    if abs(temperatures[i] - temperatures[i-1]) > 5:
        anomalies.append((i+1, temperatures[i], temperatures[i-1]))  # Day, current, previous
print(f"Temperature anomalies (day, temp, prev_temp): {anomalies}")

# Statistical summary
print("\nStatistical Summary:")
print(f"Total days: {len(temperatures)}")
print(f"Range: {coldest}°F to {hottest}°F")
print(f"Average: {average_temp:.2f}°F")
print(f"Days above average: {len(above_average_days)}")
print(f"Category breakdown: Cold {len(cold)}, Mild {len(mild)}, Warm {len(warm)}")
print(f"Patterns: Longest hot streak: {max_streak} days. Anomalies: {len(anomalies)} detected.")