import requests

page_count = 1
records = []

def sort_by_num_comments(rec):
    if rec.get("num_comments"):
        return rec.get("num_comments")
    return -1

# total pages - 5
while page_count < 6:
    response = requests.get(f"https://jsonmock.hackerrank.com/api/articles?page={page_count}")
    response = response.json()
    records.extend(response["data"])
    page_count += 1

sorted_records = sorted(records, key=sort_by_num_comments, reverse=True)

print("Top two titles with most number of comments")
print("*******************************************")
for rec in sorted_records[0:2]:
    print(rec["title"] + "-" +  str(rec["num_comments"]))


print()
print()

page_count = 1
records = []

# total pages - 2

def sort_by_submission_counts(rec):
    if rec.get("submission_count"):
        return rec.get("submission_count")
    return -1

while page_count < 3:
    response = requests.get(f"https://jsonmock.hackerrank.com/api/article_users?page={page_count}")
    response = response.json()
    records.extend(response["data"])
    page_count += 1

sorted_records = sorted(records, key=sort_by_submission_counts, reverse=True)



print("Top two users with most number of submissions")
print("*********************************************")
for rec in sorted_records[0:2]:
    print(rec["username"] + "-" +  str(rec["submission_count"]))
