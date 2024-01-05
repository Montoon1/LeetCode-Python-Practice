import requests

url = "https://leetcode.com/graphql/"

body = """
{
    query Query {
        problemsetQuestionList{
            CategorySlug
            limit
        }
    }
}"""

response = requests.get(url=url, json={"query": body})
print(response.status_code)
if response.status_code == 200:
    print("response : ", response.content)