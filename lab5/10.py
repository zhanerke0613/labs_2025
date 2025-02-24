import re

txt = "ThisIsCamelCase JustExample"
print(re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower())  
