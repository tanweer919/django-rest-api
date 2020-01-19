# Django REST API Tutorial
Here REST API is implemented in the form of simple todo
## Different APIs
| url              | method | body                        | response                   |
|------------------|--------|-----------------------------|----------------------------|
| /todos           | GET    | none                        | list of all todos          |
| /todo/:id        | GET    | none                        | Detail of individual todos |
| /todo/new        | POST   | { todo: value, done: value} | Creation message           |
| /todo/:id/modify | POST   | {done: value}               | Updation message           |

## Model
```
    todo: CharField,
    done: Boolean
```