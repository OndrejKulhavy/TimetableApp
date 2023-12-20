import random
from multiprocessing import Process, Manager
from multiprocessing.queues import JoinableQueue
Manager().Queue()

class UniqueQueue():
    def __init__(self, maxsize=0, *, ctx):
        JoinableQueue.__init__(self, maxsize=maxsize, ctx=ctx)
        self._set = set()

    def put(self, item, block=True, timeout=None):
        if item not in self._set:
            super().put(item, block, timeout)
            self._set.add(item)

    def get(self, block=True, timeout=None):
        item = super().get(block, timeout)
        self._set.remove(item)
        return item


def consumer(q: JoinableQueue):
    while True:
        res = q.get()
        print(f'Consume {res}')
        q.task_done()


def producer(q: JoinableQueue, food):
    for i in range(2):
        res = f'{food} {i}'
        print(f'Produce {res}')
        q.put(res)
    q.join()


if __name__ == "__main__":
    foods = ['apple', 'banana', 'melon', 'salad']
    jobs = 2
    q = JoinableQueue()

    producers = [
        Process(target=producer, args=(q, random.choice(foods)))
        for _ in range(jobs)
    ]

    # daemon=True is important here
    consumers = [
        Process(target=consumer, args=(q,), daemon=True)
        for _ in range(jobs * 2)
    ]

    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    for p in producers:
        p.join()

    print('Done')
