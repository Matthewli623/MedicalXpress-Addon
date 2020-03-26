import json
import requests
import time
import sys
import os
# sys.path.append(os.getcwd())
print(sys.argv)
# os.chdir(sys.argv[0])
os.chdir(sys.path[0])

time_start = time.time()
if __name__ == '__main__':
    testData = {"name": "小明", "age": 18}
    response = requests.post('http://127.0.0.1:5000/test_1.0', json=testData)

print(response.text)

time_end = time.time()
print('totally cost', time_end-time_start)
