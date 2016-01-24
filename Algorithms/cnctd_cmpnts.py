n=int(raw_input("Enter the number of nodes:\n"))
graph=[int(x+1) for x in range(n)]
a=[]
for x in range (n):

	a.append([int(e) for e in raw_input("Enter the connected nodes for "+str(x+1)+"\n").split(" ")])
print a
visited = [] # Array to store the visited nodes
dfs_array = []
rm_nodes=[]
stack=[] # Initialize a list to manipulate as stack
count=1
def dfs(node): 

	if(node not in dfs_array):
		dfs_array.append(node)

	for each in a[node-1]:
		if each not in dfs_array:
			stack.append(each)

	if (stack):
		dfs(stack.pop())
	visited.extend(set(dfs_array))
	if len(set(graph)-set(visited))>0:
		global count
		count = count+1
		rm_nodes=list(set(graph)-set(visited))
		dfs(rm_nodes[0])

dfs(1)
print "-------------------------\nNo. of connected components : "+str(count)

