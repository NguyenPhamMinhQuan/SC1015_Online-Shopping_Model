graph = {
    '3,-1' : ['3,0','2,0'] , # [ down , left ]
    
    #branching out on going down from first step 
    '3,0' : ['5,0','2,1'] ,#[ rotating , goin left ]
    
    #under rotating
    '5,0' :['4,1'] , #going left
    '4,1' : ['3,2'] , #going left 
    '3,2' : ['3,3'] , #going down to reach endgoal
    
    #under going left
    '2,1' : ['1,2','4,1'] , #[going left , rotating]
    #under rotating
    '4,1' : ['3,2'], # going left
    '3,2' : ['3,3'],
    #under going left
    '1,2' : ['3,2'], #rotating
    '3,2' : ['3,3'] , #going down
    
    
    
    #branching out on going LEFT from first step 
    '2,0' : ['1,1','2,1'] ,  #[going left , going down]
    #under left 
    '1,1' : ['3,1','1,2'], #[rotate,going down]
    #under rotatnin¥e
    '3,1' : ['3,2'] ,
    '3,2' : ['3,3'] ,
    #under going down
    '1,2': ['3,2'] ,
    '3,2' : ['3,3'] ,
    
    #under going down
    '2,1' : ['4,1','1,2'],  #[rotate , left]
    #under rotate
    '4,1' : ['3,2'] , #left
    '3,2' : ['3,3'] , #down
    #under left
    '1,2' : ['3,2'] ,#rotate
    '3,2' : ['3,3'], #down
    
    '3,3' : []
     
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)
    
    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        print ("({item})".format(item = m), end = " ") 

        for neighbour in graph[m]:
            visited.append(neighbour)
            queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '3,-1')    # function calling
print('\n')
print(visited)
print('\n')
print(queue)
