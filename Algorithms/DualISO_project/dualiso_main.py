#!/usr/bin/python2

import matplotlib.pyplot as plt

def feasibleMatches(G,Q):

	Phi={}
	for u in Q.nodes():
		Phi[u]=[]
		for v in G.nodes():
			if G.out_degree(v)>=Q.out_degree(u):
				Phi[u].append(v)
	return  Phi

def dualSim(G,Q,Phi):

	Phi_={}
	Phi_v={}
	changed=True
	while changed:
		changed=False
		for u in Q.nodes():
			for u_ in Q.successors(u):
				Phi_[u_]=[]
				for v in Phi[u]:
					Phi_v[u_]=list(set(G.successors(v)) & set(Phi[u_]))
					if not Phi_v[u_]:
						Phi[u].remove(v)
						if not Phi[u]:
							Phi.clear()
							return Phi
						changed=True
					Phi_[u_]=list(set(Phi_[u_]) | set(Phi_v[u_]))
				if not Phi_[u_]:
					Phi.clear()
					return Phi
				if len(Phi_[u_])<len(Phi[u_]):
					changed=True
				Phi[u_]=list(set(Phi[u_]) & set(Phi_[u_]))
	return Phi



def findMatches(G,Q):
	matches=[]
	Phi_0=feasibleMatches(G,Q)
	old_Phi=Phi_0.copy()
	Phi_1=dualSim(G,Q,Phi_0)
	new_Phi=Phi_1.copy()
	plot(old_Phi,new_Phi)
	def search(G,Q,Phi,depth):

		if depth==Q.number_of_nodes():
			matches.append(Phi)
		else:
			for v in Phi[depth]:
				setx=set()
				for x in range(depth):
					setx=set(setx | set(Phi[x]))
				if v not in setx:
					Phi_=Phi.copy()
					Phi_[depth]=[v]
					Phi_=dualSim(G,Q,Phi_)
					if Phi_:
						search(G,Q,Phi_,depth+1)

		return matches
	return search(G,Q,Phi_1,0)

def plot(old_Phi,new_Phi):
    samples1 = [len(old_Phi[each]) for each in old_Phi]
    samples2 = [len(new_Phi[each]) for each in new_Phi]
    labels1 = ["v"+str(each) for each in old_Phi]
    labels2 = ["v"+str(each) for each in new_Phi]
   	
    N1 = len( old_Phi )
    x1 = range( N1 )
    N2 = len( new_Phi )
    x2 = range( N2 )
    width = .5

    plt.figure( 1 )

    plt.subplot( 2, 1, 1 ).set_ylim(0,max(samples1)+2)
    plt.bar( x1, samples1, width, color="magenta" )
    plt.xticks([x+width/2.0 for x in x1], labels1 )
    plt.ylabel( 'Number of matches' )
   
    plt.subplot( 2, 1, 2 ).set_ylim(0,max(samples1)+2)
    plt.bar( x2, samples2, width, color="yellow" )
    plt.xticks([x+width/2.0 for x in x2], labels2 )
    plt.ylabel( 'Number of matches (DualSimulation)' )
    
    plt.show()
