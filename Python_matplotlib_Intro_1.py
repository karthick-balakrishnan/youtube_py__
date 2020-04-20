import matplotlib.pyplot as plt

year=[2010,2015,2020]
version=[2.8,3,3.8]

plt.subplot(2,2,1)
plt.plot(version,"ro")
plt.ylabel("version")

#######################


plt.subplot(2,2,2)
plt.plot(year,version)
plt.xlabel("year")
plt.ylabel("version")

######################

plt.show()
