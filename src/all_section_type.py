import asyncio
import pickle
from pprint import pprint

import httpx

base_url = "http://www.sfu.ca/bin/wcm/course-outlines?"

api_url = base_url + "current/current"

departments = [dept["value"] for dept in httpx.get(api_url).json()]

# course_sections = [
#     requests.get(f"{api_url}/{dept}/{course['value']}").json()
#     for dept in departments
#     for course in requests.get(f"{api_url}/{dept}").json()
# ]


async def main():
    # course_sections: list[Any] = []
    # async with httpx.AsyncClient() as client:
    #     for dept in tqdm(departments):
    #         courses_r = await client.get(f"{api_url}/{dept}")
    #         try:
    #             courses = courses_r.json()
    #         except Exception as e:
    #             print(e)
    #             print(dept)
    #             print(courses_r.content.decode())
    #             continue

    #         tasks: list[Coroutine[Any, Any, httpx.Response]] = []
    #         for course in tqdm(courses):
    #             if course == "errorMessage":
    #                 continue
    #             try:
    #                 tasks.append(client.get(f"{api_url}/{dept}/{course['value']}"))
    #             except Exception as e:
    #                 print(e)
    #                 print(dept)
    #                 print(course)

    #         course_sections_responses = await asyncio.gather(*tasks)

    #         for course_sections_response in tqdm(course_sections_responses):
    #             try:
    #                 course_sections.append(course_sections_response.json())
    #             except Exception as e:
    #                 print(e)

    # with open("course_sections.pkl", "wb") as f:
    #     pickle.dump(course_sections, f)

    with open("course_sections.pkl", "rb") as f:
        course_sections = pickle.load(f)

    section_codes: set[str] = set()
    for course_section in course_sections:
        for course in course_section:
            if "errorMessage" in course:
                continue
            try:
                section_codes.add(course["sectionCode"])
            except Exception as e:
                print(e)
                print(course_section)
                raise ValueError

    pprint(list(section_codes))


asyncio.run(main())
