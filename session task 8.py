import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [22, 24, 19, 23, 25, 27, 26]  


plt.figure()
plt.plot(days, temperatures, marker='o')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over a Week')
plt.grid(True)
plt.tight_layout()
plt.show()