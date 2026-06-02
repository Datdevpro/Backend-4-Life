# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "taoday"}

# @app.get("/about")
# def about():
#     return {"project": "Todo API",
#             "version": "1.0"}

# # Dynamic route with path parameter
# @app.get("/hello/{name}")
# def hello(name: str):
#     return {"message": f"Hello, {name}!"}

# # Static Route with query parameter
# @app.get("/search")
# def xinchao(keyword: str):
#     return {"message": f"Key word finding is {keyword}"}

# # dummy database using list
# todolist = [{"id": 1, "title": "Learn FastAPI"},
#     {"id": 2, "title": "Learn Docker"}]

# @app.get("/gettodos")
# def gettodos():
#     return {"todos": todolist}

# # use pydantic model to define the request body for creating a new todo item 
# #pydantic help to validate inputdata from user, define schema, parse JSON request body 
# class Todo(BaseModel):
#     id: int
#     title: str

# @app.post("/todos")
# def create_todo(todo: Todo):
#     todolist.append(todo)
#     return {"message": "Todo item created successfully", 
#             "todo": todo}


# @app.get("/todos/{todo_id}")
# def get_todo(todo_id: int):
#     for todo in todolist:
#         if todo["id"] == todo_id:
#             return todo
#     #return {"message": "404 Not Found"} 
#     raise HTTPException(status_code=404, detail="Todo item not found")


# @app.put("/todos/{todo_id}")
# def update_todo(todo_id: int, updated_todo: Todo):
#     for todo in todolist:
#         if todo["id"] == todo_id:
#             todo["title"] = updated_todo.title
#             return {
#                 "message": "Updated successfully",
#                 "Data": todo
#             }
#     raise HTTPException(status_code=404, detail="Todo item not found")
# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int):

#     for index, todo in enumerate(todolist):

#         if todo["id"] == todo_id:

#             deleted_todo = todolist.pop(index)

#             return {
#                 "message": "Todo deleted",
#                 "data": deleted_todo
#             }

#     raise HTTPException(status_code=404, detail="Todo not found")