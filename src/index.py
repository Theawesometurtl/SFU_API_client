import requests
base_url = "http://www.sfu.ca/bin/wcm/course-outlines?"

# blacklisted_departments = ['arab', 'bot', 'bus', ];

api_url = base_url + "current/current"
departments = requests.get(api_url).json()


total_departments = [dept['value'] for dept in departments]
whitelisted_departments = ['chem', 'cmpt', 'cogs']
# whitelisted_departments = [dept for dept in total_departments if dept not in blacklisted_departments]

# course_numbers = requests.get(f"{api_url}/{'econ'}").json()
course_numbers = [requests.get(f"{api_url}/{dept}").json() for dept in whitelisted_departments]

course_time = [requests.get(f"{api_url}/{dept}").json() for course in course_numbers['value'] if course_numbers['value'] < 600]


print(departments)
print(course_numbers)

