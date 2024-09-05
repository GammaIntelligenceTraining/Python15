# 1234565 seconds = 14:6:56:5
seconds = 1234565

days = seconds // (24 * 3600)
seconds %= 24 * 3600
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f'{days}:{hours}:{minutes}:{seconds}')
