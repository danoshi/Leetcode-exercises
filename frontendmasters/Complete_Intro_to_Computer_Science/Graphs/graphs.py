class Solution:
    def findMostCommonTitle(self, myId, degreesOfSeparation):
        queue = [myId]
        seen = set(queue)
        jobs = {}

        for _ in range(degreesOfSeparation + 1):
            new_queue = []
            while queue:
                user = get_user(queue.pop(0))
                if user:
                # Queue up next iteration of connections
                    for connection in user['connections']:
                        if connection not in seen:
                            new_queue.append(connection)
                            seen.add(connection)
                    title = user['title']
                    jobs[title] = jobs.get(title, 0) + 1
            queue = new_queue
        job_name, biggest_number = max(jobs.items(), key=lambda item: item[1])

        return job_name


users = [
    {
        "id": 1,
        "name": "Leia Goede",
        "company": "Bluejam",
        "title": "Analog Circuit Design manager",
        "connections": [2, 3, 4, 5]
    },
    {
        "id": 2,
        "name": "Evan Elsmore",
        "company": "Thoughtmix",
        "title": "Software Consultant",
        "connections": [1, 3, 6, 7]
    },
    {
        "id": 3,
        "name": "Darcy Canet",
        "company": "Realpoint",
        "title": "Network Administrator",
        "connections": [1, 2, 4, 8]
    },
    {
        "id": 4,
        "name": "Loren Brabon",
        "company": "Twimm",
        "title": "Data Analyst",
        "connections": [1, 3, 5, 9]
    },
    {
        "id": 5,
        "name": "Griselda Hum",
        "company": "Katz",
        "title": "Human Resources Manager",
        "connections": [1, 4, 6, 10]
    },
    {
        "id": 6,
        "name": "Jarred Labeuil",
        "company": "Yakidoo",
        "title": "Marketing Manager",
        "connections": [2, 5, 7, 11]
    },
    {
        "id": 7,
        "name": "Lindsey Dacres",
        "company": "Eire",
        "title": "Sales Representative",
        "connections": [2, 6, 8, 12]
    },
    {
        "id": 8,
        "name": "Aubrey Morley",
        "company": "Topiclounge",
        "title": "Product Manager",
        "connections": [3, 7, 9, 13]
    },
    {
        "id": 9,
        "name": "Kippar Fidgeon",
        "company": "Voomm",
        "title": "Project Manager",
        "connections": [4, 8, 10, 14]
    },
    {
        "id": 10,
        "name": "Morton Oxtiby",
        "company": "Skilith",
        "title": "Chief Technology Officer",
        "connections": [5, 9, 11, 15]
    },
    {
        "id": 11,
        "name": "Averil Pidgen",
        "company": "Meeveo",
        "title": "Chief Technology Officer",
        "connections": [6, 10, 12, 16]
    },
    {
        "id": 12,
        "name": "Perren Grishukhin",
        "company": "Trudoo",
        "title": "Product Designer",
        "connections": [7, 11, 13, 2]
    },
    {
        "id": 13,
        "name": "Alyda Penberthy",
        "company": "Jaxworks",
        "title": "Quality Assurance Engineer",
        "connections": [8, 12, 14, 3]
    },
    {
        "id": 14,
        "name": "Sydney Tapply",
        "company": "Buzzdog",
        "title": "Chief Technology Officer",
        "connections": [9, 13, 15, 4]
    },
    {
        "id": 15,
        "name": "Felicia Castagnasso",
        "company": "Eidel",
        "title": "Chief Technology Officer",
        "connections": [10, 14, 16, 5]
    },
    {
        "id": 16,
        "name": "Lorilyn Cockshoot",
        "company": "Avavee",
        "title": "Financial Analyst",
        "connections": [11, 15, 6, 1]
    }
]

def get_user(user_id):
    return users[user_id - 1] if 0 < user_id <= len(users) else None
