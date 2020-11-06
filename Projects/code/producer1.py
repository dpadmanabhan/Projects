#producer:

#-->small io, medium , large io
#-->specify tier where data needs to go
from mpi4py import MPI
from os import urandom
from argparse import ArgumentParser
import os
import random
from statistics import median

small_IO = [32,128, 16*1024, 32*1024,64*1024]
medium_IO= [1*1024*1024, 2*1024*1024, 3*1024*1024]
large_IO= [8*1024*1024,9*1024*1024,10*1024*1024]
Total=1024*1024*1024

comm=MPI.COMM_WORLD
drives=["/", "/home/cc/pythio", "/home/cc/pythio-2"]

def produce(size, tier, total):
    i=0
    count=0
    if(size=='small_IO'):
       s=small_IO
       iterations=int(total/median(s))
    elif(size=='medium_IO'):
       s=medium_IO
       iterations=int(total/median(s))
    else:
       s=large_IO
       iterations=int(total/median(s))
    print(iterations)
    if(args.tier!='all'):
        folder=os.path.basename(tier)
        if(folder==""):
            folder='root'
        while(iterations):
            rs=random.choice(s)
            iterations=iterations-1
            if(count==0):
                f = open(tier+"/"+"file_"+str(i)+folder+"_rank_"+str(comm.rank), "ab")
            if(os.path.getsize(tier+"/"+"file_"+str(i)+folder+"_rank_"+str(comm.rank))>=104857600):
                f.close()
                i=i+1
                f = open(tier+"/"+"file_"+str(i)+folder+"_rank_"+str(comm.rank), "ab")
                f.write(urandom(rs))
            else:
                f.write(urandom(rs))
                count=count+1

    else:
        for path in drives:
            if(path=="/"):
               folder='root'
               f=open(path+"/"+folder+path+"rank_"+str(comm.rank),"wb")
               f.write(urandom(int(0.10*Total)))
            elif(path=="/home/cc/pythio"):
               folder=os.path.basename(path)
               f=open(path+"/"+folder+"rank_"+str(comm.rank),"wb")
               f.write(urandom(int(0.40*Total)))
            else:
               folder=os.path.basename(path)
               f=open(path+"/"+folder+"rank_"+str(comm.rank),"wb")
               f.write(urandom(int(0.50*Total)))

if __name__ == "__main__":

 parser = ArgumentParser()
 parser.add_argument('-io', '--size',type=str, help="Sets the amount of data to be written",default='small_IO')
 parser.add_argument('-t', '--tier', type=str, help="specifies a tier",default='all')

 args = parser.parse_args()
 produce(args.size, args.tier,Total)
