# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 01:47:21 2018

@author: Mostafa
"""

#%%library
import numpy as np




#%% 
def IDW(flp,coordinates,prec_data):
    
    shape_base_dem = flp.ReadAsArray().shape
    geo_trans = flp.GetGeoTransform() # get the coordinates of the top left corner and cell size [x,dx,y,dy]
    # X_coordinate= upperleft corner x+ index* cell size+celsize/2
    coox=np.ones(shape_base_dem)
    cooy=np.ones(shape_base_dem)
    for i in range(shape_base_dem[0]): # iteration by row
        for j in range(shape_base_dem[1]):# iteration by column
            coox[i,j]=geo_trans[0]+geo_trans[1]/2+j*geo_trans[1] # calculate x
            cooy[i,j]=geo_trans[3]+geo_trans[5]/2+i*geo_trans[5] # calculate y
    #%%
#    Dist=np.ones((shape_base_dem[0],shape_base_dem[1],len(coordinates['x'])))
    inverseDist=np.ones((shape_base_dem[0],shape_base_dem[1],len(coordinates['x'])))
    denominator=np.ones((shape_base_dem[0],shape_base_dem[1]))
    for i in range(shape_base_dem[0]): # iteration by row
        for j in range(shape_base_dem[1]):# iteration by column
            for st in range(len(coordinates['x'])): #iteration by station [0]: #
            # distance= sqrt((xstation-xcell)**2+ystation-ycell)**2)
    #            Dist[i,j,st]=np.sqrt(np.power((coordinates['x'][st]-coox[i,j]),2)
    #                             +np.power((coordinates['y'][st]-cooy[i,j]),2))
                inverseDist[i,j,st]=1/(np.sqrt(np.power((coordinates['x'][st]-coox[i,j]),2)
                                     +np.power((coordinates['y'][st]-cooy[i,j]),2)))
    denominator=np.sum(inverseDist,axis=2)
    #%%
#    prec_IDW=np.ones((shape_base_dem[0],shape_base_dem[1],len(prec_data[:,0])))
    prec_IDW=np.ones((len(prec_data[:,0]),shape_base_dem[0],shape_base_dem[1]))
    for t in range(len(prec_data[:,0])): # iteration by time step
        for i in range(shape_base_dem[0]): # iteration by row
            for j in range(shape_base_dem[1]):# iteration by column
    #            for st in range(len(coordinates['x'])): #iteration by station [0]: #
    #                prec_IDW[i,j,t]=inverseDist[i,j,st]*prec_data[]
#                    prec_IDW[i,j,t]=np.sum(inverseDist[i,j,:]*prec_data[t,:])/denominator[i,j]
                    prec_IDW[t,i,j]=np.sum(inverseDist[i,j,:]*prec_data[t,:])/denominator[i,j]
    
    return prec_IDW
#%%
def ISDW(flp,coordinates,prec_data):
    
    shape_base_dem = flp.ReadAsArray().shape
    geo_trans = flp.GetGeoTransform() # get the coordinates of the top left corner and cell size [x,dx,y,dy]
    # X_coordinate= upperleft corner x+ index* cell size+celsize/2
    coox=np.ones(shape_base_dem)
    cooy=np.ones(shape_base_dem)
    for i in range(shape_base_dem[0]): # iteration by row
        for j in range(shape_base_dem[1]):# iteration by column
            coox[i,j]=geo_trans[0]+geo_trans[1]/2+j*geo_trans[1] # calculate x
            cooy[i,j]=geo_trans[3]+geo_trans[5]/2+i*geo_trans[5] # calculate y
    #%%
#    Dist=np.ones((shape_base_dem[0],shape_base_dem[1],len(coordinates['x'])))
    inverseDist=np.ones((shape_base_dem[0],shape_base_dem[1],len(coordinates['x'])))
    denominator=np.ones((shape_base_dem[0],shape_base_dem[1]))
    
    for i in range(shape_base_dem[0]): # iteration by row
        for j in range(shape_base_dem[1]):# iteration by column
            for st in range(len(coordinates['x'])): #iteration by station [0]: #
            # distance= sqrt((xstation-xcell)**2+ystation-ycell)**2)
    #            Dist[i,j,st]=np.sqrt(np.power((coordinates['x'][st]-coox[i,j]),2)
    #                             +np.power((coordinates['y'][st]-cooy[i,j]),2))
                inverseDist[i,j,st]=1/(np.sqrt(np.power((coordinates['x'][st]-coox[i,j]),2)
                                     +np.power((coordinates['y'][st]-cooy[i,j]),2)))**2
    denominator=np.sum(inverseDist,axis=2)
    #%%
#    prec_IDW=np.ones((shape_base_dem[0],shape_base_dem[1],len(prec_data[:,0])))
    prec_IDW=np.ones((len(prec_data[:,0]),shape_base_dem[0],shape_base_dem[1]))
    for t in range(len(prec_data[:,0])): # iteration by time step
        for i in range(shape_base_dem[0]): # iteration by row
            for j in range(shape_base_dem[1]):# iteration by column
    #            for st in range(len(coordinates['x'])): #iteration by station [0]: #
    #                prec_IDW[i,j,t]=inverseDist[i,j,st]*prec_data[]
#                    prec_IDW[i,j,t]=np.sum(inverseDist[i,j,:]*prec_data[t,:])/denominator[i,j]
                    prec_IDW[t,i,j]=np.sum(inverseDist[i,j,:]*prec_data[t,:])/denominator[i,j]
    
    return prec_IDW