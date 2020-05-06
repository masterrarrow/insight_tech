# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from os import environ
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path


class InsightPipeline:
    def __init__(self):
        super().__init__()
        # Loading environment variables
        env = Path(__file__).parent.parent.joinpath('.env')
        load_dotenv(env)
        # Setup database
        self.client: MongoClient = MongoClient(environ.get('MONGODB_HOST'))
        self.database = self.client[environ.get('DATABASE')]
        self.collection = self.database[environ.get('COLLECTION')]

    def process_item(self, item, spider):
        # Insert only unique items to the database
        match = {"link": item.get("link")}
        if not self.collection.find_one(match):
            self.collection.insert(dict(item))

        return item
