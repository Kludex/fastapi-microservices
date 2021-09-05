from arq.worker import run_worker

from worker.main import WorkerSettings

if __name__ == "__main__":
    run_worker(WorkerSettings)
