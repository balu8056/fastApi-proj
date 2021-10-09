import uuid
from app.helpers.constants import success, failure
from elasticsearch import AsyncElasticsearch

esConnection = AsyncElasticsearch("http://elastic:1timep@localhost:9200/")


async def getIndex(index):
    try:
        res = await esConnection.search(index=index, body={"query": {"match_all": {}}})
        return success, res["hits"]
    except Exception as ex:
        return failure, str(ex)


async def insertDoc(index, doc_type, doc):
    try:
        res = await esConnection.create(index=index, doc_type=doc_type, document=doc, id=str(uuid.uuid4()))
        return success, res
    except Exception as ex:
        return failure, str(ex)


async def updateDoc(index, Id, doc):
    try:
        res = await esConnection.update(index=index, id=Id, body={"doc": doc})
        return success, res
    except Exception as ex:
        return failure, str(ex)


async def deleteDoc(index, Id):
    try:
        res = await esConnection.delete(index=index, id=Id)
        return success, res
    except Exception as ex:
        return failure, str(ex)