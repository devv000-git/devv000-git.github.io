"""Sanitised educational reference of the Azure Table Storage backend.

The original VS Code code used AuthLevel.ANONYMOUS for all CRUD routes.
It was not sufficiently protected for internet-facing placement records.
This reference changes the Function auth level to FUNCTION as a minimal
access barrier, but production browser access still requires proper identity
authentication and per-user authorisation. Do not expose function keys in JS.
No actual Azure credentials or live tenant identifiers are included.
"""
import json
import os
import uuid
from datetime import datetime, timezone

import azure.functions as func
from azure.data.tables import TableServiceClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
TABLE_NAME = os.getenv("TABLE_NAME", "placementtasks")


def get_table():
    connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    return TableServiceClient.from_connection_string(connection_string).get_table_client(TABLE_NAME)


def respond(data, status=200):
    return func.HttpResponse(json.dumps(data), status_code=status, mimetype="application/json")


def entity_to_task(item):
    return {
        "id": item["RowKey"], "date": item.get("date", ""),
        "hours": item.get("hours", 0), "title": item.get("title", ""),
        "category": item.get("category", ""), "what": item.get("what", ""),
        "soWhat": item.get("soWhat", ""), "nowWhat": item.get("nowWhat", ""),
        "status": item.get("status", ""), "skills": json.loads(item.get("skills", "[]")),
        "createdAt": item.get("createdAt", ""), "updatedAt": item.get("updatedAt", "")
    }


@app.route(route="tasks", methods=["GET", "POST"])
def tasks(req: func.HttpRequest) -> func.HttpResponse:
    table = get_table()
    if req.method == "GET":
        items = [entity_to_task(item) for item in table.list_entities()]
        items.sort(key=lambda t: (t["date"], t["createdAt"]), reverse=True)
        return respond(items)
    try:
        body = req.get_json()
        hours = float(body.get("hours", 0))
        if hours < 0 or hours > 24:
            return respond({"message":"Invalid hours"}, 400)
    except (ValueError, TypeError):
        return respond({"message":"Invalid JSON or hours"}, 400)
    now = datetime.now(timezone.utc).isoformat()
    task_id = str(uuid.uuid4())
    entity = {
        "PartitionKey": "placement", "RowKey": task_id,
        "date": body.get("date", ""), "hours": hours,
        "title": body.get("title", ""), "category": body.get("category", "Other"),
        "what": body.get("what", ""), "soWhat": body.get("soWhat", ""),
        "nowWhat": body.get("nowWhat", ""), "status": body.get("status", "Planned"),
        "skills": json.dumps(body.get("skills", [])),
        "createdAt": now, "updatedAt": now
    }
    table.create_entity(entity)
    return respond(entity_to_task(entity), 201)


@app.route(route="tasks/{id}", methods=["PUT", "DELETE"])
def task_by_id(req: func.HttpRequest) -> func.HttpResponse:
    table = get_table()
    task_id = req.route_params.get("id")
    try:
        entity = table.get_entity(partition_key="placement", row_key=task_id)
    except Exception:
        return respond({"message":"Task not found"}, 404)

    if req.method == "DELETE":
        table.delete_entity(partition_key="placement", row_key=task_id)
        return respond({"deleted": task_id})
    try:
        body = req.get_json()
        hours = float(body.get("hours", entity.get("hours", 0)))
        if hours < 0 or hours > 24:
            return respond({"message":"Invalid hours"}, 400)
    except (ValueError, TypeError):
        return respond({"message":"Invalid JSON or hours"}, 400)
    for field in ("date", "title", "category", "what", "soWhat", "nowWhat", "status"):
        if field in body:
            entity[field] = body[field]
    if "skills" in body:
        entity["skills"] = json.dumps(body["skills"])
    entity["hours"] = hours
    entity["updatedAt"] = datetime.now(timezone.utc).isoformat()
    table.update_entity(entity)
    return respond({"id":task_id,"message":"Task updated"})
