import sys
import requests
from datetime import datetime

today = datetime.now().day
curr_year = datetime.now().year
day = sys.argv[1]
year = sys.argv[2]
if day == "0":
    day = today
if year == "0":
    year = curr_year

print ("Day: ", day, ", Year: ", year ,file=sys.stderr)
url = f"https://adventofcode.com/{year}/day/{day}/input"  # Replace this with your URL
session_id = '53616c7465645f5f4221d9ea7f96b43443772de2d03636dd883e50e98996ea04e338667998318efb51602f50a4e628b4595399e94027e43709525ddd1ed8c4e7'  # Replace this with your session ID

# Create a session object to persist cookies (including the session ID)
session = requests.Session()
session.headers.update({'Cookie': f'session={session_id}'})

# Make the request and allow redirections
response = session.get(url, allow_redirects=True)

# Check if the response is a successful one (status code 200)
if response.status_code == 200:
    # Print or use the content of the redirected page
    print(response.text)
else:
    # Handle other status codes or errors
    print(f"Error: {response.status_code}")
