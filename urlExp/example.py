from selenium import webdriver
from boto.s3.connection import S3Connection, Bucket, Key
from boto.s3.key import Key
import os

def screenshot(request,val):
	if val == 1 :
		conn = S3Connection('AKIAJCPQ4PE6LD6UZ3JA', '0i/etx1tzujRlhRjICWF+ee1W0DE1+2L8OqWZOR7')
		bucket = conn.get_bucket('lheston-bucket')
		k = Key(bucket)
		k.key = '//lab3' + request.split(':')[1] + '_toS3.png'
		driver = webdriver.PhantomJS() # or add to your PATH                                                                
		driver.set_window_size(1024, 768) # optional                                                                        
		driver.get(request)
		driver.save_screenshot('tempfile.png')
		driver.quit
		file1 = open('tempfile.png', 'rb')
		os.remove('tempfile.png')
		k.set_contents_from_file(file1)
		driver.quit
		return str(request + '_toS3.png')
	elif val == 2:
		conn = S3Connection('AKIAJCPQ4PE6LD6UZ3JA', '0i/etx1tzujRlhRjICWF+ee1W0DE1+2L8OqWZOR7')
		S3_BUCKET_NAME = 'lheston-bucket'
		b = Bucket(conn, S3_BUCKET_NAME)
		k = Key(b)
		k.key = '//lab3' + request.split(':')[1] + '_toS3.png'
		b.delete_key(k)
	else:
		return str('incorrect input')

screenshot('http://google.com',2)
screenshot('http://cnn.com',1)