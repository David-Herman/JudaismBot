import praw
import json
import pymongo
import datetime

def main():
    file = open("keys.conf", "r")
    conf = json.loads(file.read())
    client_id = conf["client_id"]
    client_secret = conf["client_secret"]
    reddit_username = conf["reddit_username"]
    reddit_password = conf["reddit_password"]
    db_username = conf["db_username"]
    db_password = conf["db_password"]

    db_uri = 'mongodb://%s:%s@ds032340.mlab.com:32340/judaismterms' % (db_username, db_password)
    database_client = pymongo.MongoClient(db_uri)
    db = database_client.get_default_database()
    termsCollection = db["terms"]
    last_db_update = datetime.datetime.now()
    terms = []
    update_terms_list(termsCollection, terms)

    reddit = praw.Reddit(user_agent='rJudaismStats (by u/AMWJ)', client_id = client_id, client_secret = client_secret, username = reddit_username.lower(), password = reddit_password)
    subreddit = reddit.subreddit('test')
    for comment in subreddit.stream.comments():
        process_comment(comment)

def process_comment(comment):
    termList = terms.find({});
    comment

def update_terms_list(termsCollection, terms):
    del terms[:]
    for term in termsCollection.find({}):
        terms.append(term)
        
if __name__ == '__main__':
    main()