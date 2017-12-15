colors = ['Red', 'Blue', 'Green', 'Yellow']

states = ['Andhra', 'Karnataka', 'TamilNadu', 'Kerala']

neighbors = {}
neighbors['Andhra'] = ['Karnataka', 'TamilNadu']
neighbors['Karnataka'] = ['Andhra', 'TamilNadu', 'Kerala']
neighbors['TamilNadu'] = ['Andhra', 'Karnataka', 'Kerala']
neighbors['Kerala'] = ['Karnataka', 'TamilNadu']

colors_of_states = {}
colors_of_states['Andhra'] = None
colors_of_states['Karnataka'] = None
colors_of_states['TamilNadu'] = None
colors_of_states['Kerala'] = None

already_coloured = {}
alreadycoloredlistofneighbours = {}
alreadycoloredlistofneighbours['Andhra'] = None
alreadycoloredlistofneighbours['Karnataka'] = None
alreadycoloredlistofneighbours['TamilNadu'] = None
alreadycoloredlistofneighbours['Kerala'] = None

def updatealreadycolored(state, color):
    #changing colors in already_colored
    #print("states having STATE as neighbor")
    for key in neighbors[state]:
        if(state in neighbors[key]):
            #the state is a neighbor of another state
            if(key in already_coloured.keys()):
                #print("appending")
                newlist = []
                already_coloured[key]=newlist.append(already_coloured[key])
                newlist.append([state, color])
                already_coloured[key] = newlist
            else:
                #print("adding fresh")
                already_coloured[key] = [state, color]
        if(alreadycoloredlistofneighbours[key] != None):
            if(color not in  alreadycoloredlistofneighbours[key]):               
                    alreadycoloredlistofneighbours[key].append(color)
        else:
            alreadycoloredlistofneighbours[key] = [color]
            
def nonecolored(state):
    nc = True
    for neighbour in neighbors[state]:
        if(colors_of_states[neighbour] == None):
            continue
        else:
            nc = False
    return nc

def main():
    for state in colors_of_states.keys():
        print("\n\n")
        print("colouring state " + state)

        #check if none of the neighbours are colored
        nc = nonecolored(state)
        #if nonecoloured is False here then some neighbour has been coloured
        #allocating Red to it
        if(nc == True):
            #allocating color here
            colors_of_states[state] = colors[0]
            #updating data structures
            updatealreadycolored(state, colors[0])
        else:
            #Some neighbour is coloured
            for neighbour in neighbors[state]:
                #populating the already coloured neighbours
                if(colors_of_states[neighbour] == None):
                    #neighbour not colored - continue
                    continue
                else:
                    #making a list of lists so that you can append
                    already_coloured[state] = [neighbour, colors_of_states[neighbour]]
            #Example:{'Kerala': ['TamilNadu', 'Red'],
                        #'Karnataka': [['TamilNadu', 'Red'], ['Andhra', 'Green']],
                        #'Andhra': ['TamilNadu', 'Red'],
                        #'TamilNadu': [['Karnataka', 'Blue'], ['Andhra', 'Green']]}
            
            #allocate a colour
            for color in colors:
                if((alreadycoloredlistofneighbours[state] == None) or (color not in alreadycoloredlistofneighbours[state])):
                    #allocating color here
                    colors_of_states[state] = color
                    #changing colors in already_colored
                    updatealreadycolored(state, color)
                    break
                else:
                    continue
        print(colors_of_states)
                
                        


main()
