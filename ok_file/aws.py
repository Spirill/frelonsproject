
import boto3
from botocore.exceptions import NoCredentialsError
import os
from picamera import PiCamera
from time import strftime

AWS_ACCESS_KEY="AKIAQY3EKDORUGLQGGEH"
AWS_ACCESS_SECRET_KEY ="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"

ACCESS_KEY = AWS_ACCESS_KEY
SECRET_KEY = AWS_ACCESS_SECRET_KEY 
#pathupld = r"/home/pi/Documents/token.json"
pathupld = r"/home/pi/Pictures/test.jpg"
pathdl = r"/home/pi/Documents"

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def download_s3_folder(bucket_name, s3_folder, local_dir=None):
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)


def pic_take():
    full_datetime = strftime("%d_%m_%y_%I_%M%p")
    camera = PiCamera()
    file = "img_"+full_datetime+".jpg"
    path = "/home/pi/Pictures/"+file 
    #time.sleep(2)
    camera.capture(path)
    print("Done.")
    return file, path

#Example
pic , path  = pic_take()
uploaded = upload_to_aws(path, "frelons","Datas/Pictures/"+pic) #modifier le path et le file du fichier
downlaod = download_s3_folder("frelons","Config/",pathdl)