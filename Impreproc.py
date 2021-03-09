#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:29:17 2021

@author: molierenguile-makao
"""
# import the package 
import os 

# function that rename the file
def changeName(path_from, path_to):
    """

    Parameters
    ----------
    path_from : string
        all path of the file with file name at the end.
    path_to : string
        all path of the destination file with the new file name at the end.

    Returns
    -------
    the new name

    """
    os.rename(path_from,path_to)
    
    print('End')
    
    
# the function that generate the names 
def Genername(unity_number,stop,start=0):
    """

    Parameters
    ----------
    unity_number : inter
        number of the unities for the numero to create ex: 5 ==> 00001.
    stop : inter
        The numero to beging ex 45. it's very import to give the numbre that contains the 
        unities number lower or equale unity_number
    start : inter, optional
        number to started. The default is 0.

    Returns
    -------
    the liste contains the numero in string fotmat ex '00005'

    """
    
    # petite fonction 
    def indxg(unit_num,rang):
        n=len(str(rang))
        p=unit_num-n
        if p==0:
            answ=str(rang)
        elif p>0:
            answ=p*"0"+str(rang)
        else:
            answ="NA"
        
        return answ
    
    try:
        assert unity_number>=len(str(start)) and unity_number>=len(str(stop))
    except AssertionError:
        print("Error: the length of one of two number start or stop is upper to number of unities")
    else:
        return [indxg(unity_number,xx) for xx in range(start,stop+start)]
    finally:
        pass
    
# the function that change the file name in the repository 

def modifyName(newfileName,path_repo1,ext1,unity_number,start_num=0,path_repo2=None,ext2='.xml'):
    """

    Parameters
    ----------
    newfileName : string
        the name racine..
    path_repo1 : string
        the repositiry where found the file.
    ext1 : string
        the extension of file that will change the names.
    unity_number : int
        the max unity number for the indexation of file .
    start_num : int, optional
        the starting numero. The default is 0.
    path_repo2 : string, optional
        the second repos. The default is None.
    ext1 : string, optional
        the extension of the second repo. The default is None.

    Returns
    -------
    the repos with the file names changed.

    """
    lstfile = os.listdir(path_repo1)
    goofile = [i for i in lstfile if i.endswith(ext1)]
    m=len(goofile)
    try:
        assert unity_number>=len(str(start_num)) and unity_number>=len(str(m))
    except AssertionError:
        print("Error: the length of one of two number start or file number is upper to number of unities")
    else:
        fileIndex = Genername(unity_number,m,start=start_num)
        if path_repo2 is None:
            i=0
            for uu in goofile:
                path_from=path_repo1+'/'+uu
                path_to = path_repo1+'/'+newfileName+'_'+fileIndex[i]+ext1
                changeName(path_from, path_to)
                i+=1
            
        else:
            i=0
            for uu in goofile:
                path_from1 =path_repo1+'/'+uu
                path_to1 = path_repo1+'/'+newfileName+'_'+fileIndex[i]+ext1
                changeName(path_from1, path_to1)
                path_from2 =path_repo2+'/'+uu.replace(ext1,ext2)
                path_to2 = path_repo2+'/'+newfileName+'_'+fileIndex[i]+ext2
                changeName(path_from2, path_to2)
                i+=1
                
        
    finally:
        pass

        
                
            
        
        




        
        

        
  
        
            
        
        
    


    
    
