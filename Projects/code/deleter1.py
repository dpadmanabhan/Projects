#from which tier you have to delete

import os,fnmatch
from argparse import ArgumentParser
from mpi4py import MPI

comm=MPI.COMM_WORLD
def delete(size, tier,s=0):
    delete=[]
    files=fnmatch.filter(os.listdir(tier),'*rank_'+str(comm.rank))
    for f in files:
        s+=os.path.getsize(tier+'/'+f)
        delete.append(f)
        if(s>=size):
            break
    for f in delete:
        os.remove(tier+"/"+f)

if __name__ == "__main__":

 parser = ArgumentParser()
 parser.add_argument('-d', '--delsize',type=int, help="Sets the amount of data to be deleted",default=8)
 parser.add_argument('-t', '--tier', type=str, help="specifies a tier",default='all')
 args = parser.parse_args()
 s=0
 delete(args.delsize, args.tier,s)
