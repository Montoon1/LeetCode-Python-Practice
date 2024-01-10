import requests
import random
import re
import html

url = "https://leetcode.com/graphql/"

query_total_number = {"query":"query problemsetQuestionList($categorySlug: String, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n      }\n}","variables":{"categorySlug":"","skip":0,"filters":{}}}

def get_total():
    response = requests.get(url=url, json=query_total_number).json()
    return int(response["data"]["problemsetQuestionList"]["total"])

def set_random_int(question_total: int) -> int:
    return random.randrange(question_total) - 1

def get_random_question(current_question_id: int):
    query = {"query":"query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    questions: data {\n      difficulty\n      frontendQuestionId: questionFrontendId\n      title\n      titleSlug\n      content\n      }\n  }\n}","variables":{"categorySlug":"","limit":1,"skip":current_question_id,"filters":{}}}
    response = requests.get(url=url, json=query).json()
    title = response["data"]["problemsetQuestionList"]["questions"][0]["title"]
    difficulty = response["data"]["problemsetQuestionList"]["questions"][0]["difficulty"]
    problem_description = response["data"]["problemsetQuestionList"]["questions"][0]["content"]
    problem_description = re.sub("\<.*?\>", "", problem_description)
    problem_description = html.unescape(problem_description)
    return title, difficulty, problem_description
