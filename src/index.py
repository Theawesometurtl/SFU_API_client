from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
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

# course_time = [requests.get(f"{api_url}/{dept}").json() for course in course_numbers['value'] if course_numbers['value'] < 600]


print(departments)
print(course_numbers)

with open('file2.txt', 'w') as f:
    for dept in course_numbers:
        for sfu_class in dept:
            print(sfu_class)
            f.write(sfu_class["value"] + " " + sfu_class["title"])
            f.write('\n')


class Client:
    def __init__(self):
        self.base_url = "http://www.sfu.ca/bin/wcm/course-outlines?"
    def get_years(self) -> Years:
        years_json = requests.get(self.base_url).json()
        results: list[Year] = []
        for year in years_json:
            value = year["value"]
            text = year["text"]
            results.append(Year(**year))
            
        return Years(**results)
        
        # year: Year = 
        # years = [year["text"] for year in years_json, year["value"] for year in years_json]
        ...
    
    def get_semesters(self, year: Year) -> Terms:
        ...


@dataclass
class TextValue:
    text: str
    value: str


class Year(TextValue): ...
class Term(TextValue): ...


@dataclass
class NamedTextValue:
    text: str
    value: str
    name: str


class Department(NamedTextValue): ...
class CourseNumber(NamedTextValue): ...  # name is title

    
@dataclass
class CourseSection:
    text: str
    value: str
    # title
    name: str
    # classType (e=true, n=false)
    enrollment: bool
    # sectionCode
    section_code: 


@dataclass
class Years:
    results: list[Year]


@dataclass
class Terms:
    results: list[Term]


@dataclass
class Departments:
    results: list[Department]


@dataclass
class CourseNumbers:
    results: list[CourseNumber]


@dataclass
class CourseSection:
    results: list[Class]