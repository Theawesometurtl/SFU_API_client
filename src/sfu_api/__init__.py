from __future__ import annotations

import httpx

from sfu_api.models import CourseOutline, Term, Terms, Year, Years

# blacklisted_departments = ['arab', 'bot', 'bus', ];

# api_url = base_url + "current/current"
# departments = httpx.get(api_url).json()


# total_departments = [dept["value"] for dept in departments]
# whitelisted_departments = ["chem", "cmpt", "cogs"]
# whitelisted_departments = [dept for dept in total_departments if dept not in blacklisted_departments]

# course_numbers = requests.get(f"{api_url}/{'econ'}").json()


# async def get_course_numbers() -> Any:
#     async with httpx.AsyncClient() as client:
#         course_numbers_tasks = [
#             client.get(f"{api_url}/{dept}") for dept in whitelisted_departments
#         ]

#         course_number_responses = await asyncio.gather(*course_numbers_tasks)

#         return [response.json() for response in course_number_responses]


# course_numbers = asyncio.run(get_course_numbers())

# course_time = [requests.get(f"{api_url}/{dept}").json() for course in course_numbers['value'] if course_numbers['value'] < 600]

# if __name__ == "__main__":
#     print(departments)
#     print(course_numbers)

#     with open("file2.txt", "w") as f:
#         for dept in course_numbers:
#             for sfu_class in dept:
#                 print(sfu_class)
#                 f.write(sfu_class["value"] + " " + sfu_class["title"])
#                 f.write("\n")


BASE_URL = "http://www.sfu.ca/bin/wcm/course-outlines?"


class Client:
    def __init__(self) -> None:
        self.client = httpx.Client()

    def get_years(self) -> Years:
        years_json = self.client.get(BASE_URL).json()
        years: list[Year] = []
        for year in years_json:
            years.append(Year(**year))

        return Years(years)

    def get_terms(self, year: Year) -> Terms:
        terms_json = self.client.get(BASE_URL + year.value).json()
        terms: list[Term] = []
        for term in terms_json:
            terms.append(Term(**term))

        return Terms(terms)


def _main():
    print(
        CourseOutline.model_validate(
            httpx.get(BASE_URL + "2023/summer/math/150/d101").json()
        )
    )


if __name__ == "__main__":
    _main()
