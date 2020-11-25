from dateutil.parser import parse as dtparse
from datetime import datetime as dt

start = '2018-12-26T10:00:00+01:00'   # Let's say your start value returns this as 'str'
tmfmt = '%d %B, %H:%M %p'             # Gives you date-time in the format '26 December, 10:00 AM' as you mentioned

# now use the dtparse to read your event start time and dt.strftime to format it
stime = dt.strftime(dtparse(start), format=tmfmt