import os
# 현재 파일의 경로
print(os.path.abspath(__file__))

# 해당 파일이 들어 있는 폴더까지의 경로
print(os.path.dirname(os.path.abspath(__file__)))

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))