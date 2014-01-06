# -*- coding: utf-8 -*-
from flask import Blueprint
app = Blueprint('mongo', __name__, url_prefix='/mongo')

from flask_sample import mongo

import json
from bson import json_util

@app.route('/find', methods=['GET', 'POST'])
def find():
    recs = mongo.db.sample.find().limit(10)
    s = ""
    for rec in recs:
        # BSON -> JSONへの変換も
        s += json.dumps(rec, ensure_ascii=False, default=json_util.default)
        s += '<br/>'
    return s

# 1.TestData
#  mongoimport -d flask_sample -c sample -type json -file sample.json
# {"user_id":1,"votes":1.1,"reviews":11}
# {"user_id":2,"votes":1.0,"reviews":21}
# {"user_id":2,"votes":2.2,"reviews":22}
# {"user_id":3,"votes":1.0,"reviews":31}
# {"user_id":3,"votes":2.0,"reviews":32}
# {"user_id":3,"votes":3.3,"reviews":33}
#
# 2.by Console
# mongo localhost/flask_sample sample.js
# var res = db.sample.group({
#     key: {user_id: true},
#     initial: {votes_sum: 0.0, votes_count: 0},
#     reduce: function(doc, aggregator) {
#         aggregator.votes_sum += doc.votes;
#         aggregator.votes_count += 1;
#     },
#     finalize: function(doc){
#         doc.average_votes = doc.votes_sum / doc.votes_count;
#     }
# });
# shellPrint(res)

@app.route('/group', methods=['GET', 'POST'])
def group():
    ## group(self, key, condition, initial, reduce, finalize=None):
    recs = mongo.db.sample.group( \
        key={'user_id': 1},
        condition={},
        initial={'votes_sum': 0.0, 'votes_count': 0},
        reduce='''
            function(doc, aggregator) {
                aggregator.votes_sum += doc.votes;
                aggregator.votes_count += 1;
            }
        ''',
        finalize='''
        function(doc){
            doc.average_votes = doc.votes_sum / doc.votes_count;
        }'''
                                  )
    s = ""
    for rec in recs:
        s += json.dumps(rec, ensure_ascii=False)
        s += '<br/>'
    return s
