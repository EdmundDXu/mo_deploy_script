import os
from qiniu import Auth, put_file, etag
import qiniu.config
from qiniu import BucketManager


# 需要填写你的 Access Key 和 Secret Key
access_key = 'm1lGO9G95Aq-vXkUy4jM-3jwCx3kWhSIQX_O694U'
secret_key = '3KeBSg65SVzdHaVitod3kiy1vC9PtkwZ4CFRXcyD'
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'frontend'

def delete_all_file():
    bucket = BucketManager(q)
    prefix = None
    limit = None
    delimiter = None
    marker = None
    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
    from pprint import pprint
    pprint([e['key'] for e in ret['items']])
    keys = [e['key'] for e in ret['items']]
    ops = build_batch_delete(bucket_name, keys)

def upload_file():
    directory="/home/admin/www/mo_prod/frontend/dist"
    file_set = set()

    for dir_, _, files in os.walk(directory):
        for file_name in files:
            rel_dir = os.path.relpath(dir_, directory)
            rel_file = os.path.join(rel_dir, file_name)
            file_set.add(rel_file)

    for file_ in file_set:
        print(file_.split("./")[-1])
        # token = q.upload_token(bucket_name, file_, 3600)
        # return put_file(token, key, localfile)

delete_all_file()
upload_file()
