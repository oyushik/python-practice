time = 12345
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print(f"{time}초는 {hours}시간 {minutes}분 {seconds}초입니다.")
