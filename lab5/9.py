import re

txt = "WaveToEarth"
print(re.sub(r'([a-z])([A-Z])', r'\1 \2', txt))  

