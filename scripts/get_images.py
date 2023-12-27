import json
import os

question_files = []
file_names = os.listdir("./web/src/utils/questions/")
file_names.remove("index.ts")

for file_name in file_names:
    with open(f"./web/src/utils/questions/{file_name}", "r") as f:
        question_files.append(
            {
                "name": file_name,
                "data": json.loads(f.read().lstrip("export default ")),
            }
        )

# images = []

# for file in question_files:
#     for question in file["data"]:
#         try:
#             image_link = question["question_image"]
#         except KeyError:
#             continue

#         image_name = image_link.split("/")[-1]
#         images.append(
#             {
#                 "name": image_name,
#                 "link": image_link,
#             }
#         )


# for image in images:
#     os.system(f"wget {image['link']} -O ./web/src/lib/images/{image['name']}")


for file in question_files:
    for question in file["data"]:
        try:
            image_link = question["question_image"]
        except KeyError:
            continue

        image_name = image_link.split("/")[-1]
        question["question_image"] = image_name

    with open(f"./web/src/utils/questions/{file['name']}", "w") as f:
        f.write(f"export default {json.dumps(file['data'], indent=2)}")

