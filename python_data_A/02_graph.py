# import matplotlib.pyplot as plt
# plt.plot([10,20,30,40])
# plt.show()

# import matplotlib.pyplot as plt
# plt.plot([10,20,30,40],[12,430,25,15])
# plt.show()

# import matplotlib.pyplot as plt
# plt.title('graph')
# plt.plot([10,20,30,40])
# plt.show()

# import matplotlib.pyplot as plt
# plt.title('legend')
# plt.plot([10,20,30,40], label= 'up')
# plt.plot([40,30,20,10], label= 'down')
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# plt.title('color')
# plt.plot([10,20,30,40], color = 'skyblue', label= 'skyblue')
# plt.plot([40,30,20,10],'yellow', label= 'yellow')
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# plt.title('linestyle')
# plt.plot([10,20,30,40], color = 'r',linestyle= '--', label= 'dashed')
# plt.plot([40,30,20,10],color= 'g', label= 'dotted')
# plt.legend()
# plt.show()

import matplotlib.pyplot as plt
plt.title('marker')
plt.plot([10,20,30,40], 'r.', label= 'circle')
plt.plot([40,30,20,10], 'g^', label= 'triangle up')
plt.legend()
plt.show()