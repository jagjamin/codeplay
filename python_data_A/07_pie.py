import matplotlib.pyplot as plt

# plt.pie([10, 20])
# plt.show()

# size = [2441, 2312, 1031, 1233]
# plt.axis('equal')
# plt.pie(size)
# plt.show()


# plt.rc( 'font', family='Malgun Gothic')
# size = [2441, 2312, 1031, 1233, 555]
# lebel=['A형', 'B형', 'AB형', '0형', '우리형']
# plt.axis('equal')
# plt.pie(size, labels=lebel)
# plt.show()

# plt.rc('font', family='Malgun Gothic')
# size = [2441, 2312, 1031, 1233]
# label= ['A형', 'B형','AB형', '0형']
# plt.axis('equal')
# plt.pie(size, labels=label, autopct='%.2f%%')
# plt. legend()
# plt.show()

plt.rc('font', family='Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label=['A형','B형','A형', '0형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink'] 
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%', colors=color, explode=(0.1,0,0,0)) 
plt.legend()
plt.show()