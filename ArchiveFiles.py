
#/usr/local/bin/python3
# _*_ coding: utf-8 _*_ 


import boto3
from boto3 import client

def archAuth():
    # method for autorization
    # auto is currently using global key
    # create tempory session and perform this vs permenent key
    print ("Connection Successfu To ")
    

def getFileList():
    # list of files which need move
    fList = []
    # again assumes boto.cfg setup, assume AWS S3
    for key in conn.list_objects(Bucket=bucketSource)['Contents']:
        #print(key['Key'])
        fList.append(key['Key'])
    return fList

def archiveFiles(dFiles):
    #archive files based on list supplied to method
    bucket = s3.Bucket(archvieSource)
    for i in dFiles:
     
        copy_source = {
            'Bucket': bucketSource,
            'Key': i
        }
        bucket.copy(copy_source, i)
        #conn.copy_key(i.key.name, archvieSource, i.key.name)
        response = conn.delete_object(
                Bucket=bucketSource,
                Key=i,
             )
        print("File Archived:",i,response)
#Main()
# TODO: archive folders are dyanmic based on dates
# Sources are dynamic based on all buckets based on age and catgory of files
#bucketSource="dharmafiles"
#archvieSource="archivedharmafiles"
bucketSource="archivedharmafiles"
archvieSource="dharmafiles"
s3 = boto3.resource('s3')
#bucketSource="dharmafiles"
#archvieSource="archivedharmafiles"
conn = client('s3')
# get the list of files
flList = getFileList()
archiveFiles(flList)

