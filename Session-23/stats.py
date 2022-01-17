import matplotlib.pyplot as plt

# Dataset
data = {"Windows": 85, "ChromeOS": 65, "Mac": 350}
x_axis = data.keys()
y_axis = data.values()

fig = plt.figure(figsize=(8, 5))

# Create a bar chart
plt.bar(x_axis, y_axis, color="darkviolet", width=0.6)

plt.xlabel("Operating systems")
plt.ylabel("Number of users")

plt.title("Number of users per operating system")

plt.ylim(0, 450)
plt.grid(axis = "y")

plt.show()
