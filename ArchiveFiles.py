
#/usr/local/bin/python3

import boto3
from boto3 import client

def archAuth(source):
    # method for autorization
    # auto is currently using global key
    # create tempory session and perform this vs permenent key
    print ("Connection Successfu To %s",source)
    

def getFileList(source):
    # list of files which need move
    fList = []
    # again assumes boto.cfg setup, assume AWS S3
    for key in conn.list_objects(Bucket=bucketSource)['Contents']:
        #print(key['Key'])
        fList.append(key['Key'])
    return fList

def archiveFiles(dFiles):
    #archive files based on list supplied to method
    for i in dFiles:
        print("File Archived:",i)
        #conn.copy_key(i.key.name, archvieSource, i.key.name)
        #i.delete()

#Main()
# TODO: archive folders are dyanmic based on dates
# Sources are dynamic based on all buckets based on age and catgory of files
source="AWS S3 bucket location  s3://my-bucket/Files"
#s3 = boto3.resource('s3')
#copy_source = {
#      'Bucket': 'mybucket',
#      'Key': 'mykey'
#    }
#bucket = s3.Bucket('otherbucket')
#bucket.copy(copy_source, 'otherkey')

bucketSource="dharmafiles"
archvieSource="archivedharmafiles"
conn = client('s3')
# get the list of files
flList = getFileList(source)
archiveFiles(flList)

