from locust import HttpUser, task, tag, TaskSet
from locust import LoadTestShape

class authorTasks(TaskSet):
    # here are all the tests which we want to run, which contains endpoints along with their verbs which we want to test
    
    @tag('demo', 'getMultipleAuthors')
    @task(weight=1)
    def getAuthors(self):
        self.client.get('/api/v1/Authors')

    @tag('demo', 'createAuthor')
    @task(weight=1)
    def createAuthor(self):
        self.client.post('/api/v1/Authors', data='{"id": 0,"idBook": 0,"firstName": "deepak","lastName": "chourasia"}', headers={'Content-Type': 'application/json', 'Accept' : 'application/json'})

    @tag('demo', 'getBooks')
    @task(weight=1)
    def getBooks(self):
        self.client.get('/api/v1/Authors/authors/books/1')

    @tag('demo', 'getSingleAuthor')
    @task(weight=1)
    def getAuthor(self):
        self.client.get('/api/v1/Authors/1')

    @tag('demo', 'updateAuthor')
    @task(weight=1)
    def updateAuthor(self):
        self.client.put('/api/v1/Authors/1', data='{"id": 0,"idBook": 0,"firstName": "deepak","lastName": "chourasia"}', headers={'Content-Type': 'application/json', 'Accept' : 'application/json'})

    @tag('demo', 'deleteAuthor')
    @task(weight=1)
    def deleteAuthor(self):
        self.client.delete('/api/v1/Authors/1')


class authors(HttpUser):
    tasks = [authorTasks]


class StagesShape(LoadTestShape):
    # here is the load pattern
    stages = [
        {"duration": 10, "users": 1, "spawn_rate": 1},
        {"duration": 20, "users": 10, "spawn_rate": 2},
        {"duration": 30, "users": 25, "spawn_rate": 5},
        {"duration": 40, "users": 50, "spawn_rate": 10},
        {"duration": 50, "users": 100, "spawn_rate": 20}
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            # print('users', stage['users'])
            print('run_time', run_time)
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None



