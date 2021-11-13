[Interview questions](full.md)
# Apache Airflow
+ [What is Airflow?](#What-is-Airflow)
+ [What issues does Airflow resolve?](#What-issues-does-Airflow-resolve)
+ [Explain how workflow is designed in Airflow?](#Explain-how-workflow-is-designed-in-Airflow)
+ [Explain Airflow Architecture and its components?](#Explain-Airflow-Architecture-and-its-components)
+ [What are the types of Executors in Airflow?](#What-are-the-types-of-Executors-in-Airflow)
+ [What are the pros and cons of SequentialExecutor?](#What-are-the-pros-and-cons-of-SequentialExecutor)
+ [What are the pros and cons of LocalExecutor?](#What-are-the-pros-and-cons-of-LocalExecutor)
+ [What are the pros and cons of CeleryExecutor?](#What-are-the-pros-and-cons-of-CeleryExecutor)
+ [What are the pros and cons of KubernetesExecutor?](#What-are-the-pros-and-cons-of-KubernetesExecutor)
+ [How to define a workflow in Airflow?](#How-to-define-a-workflow-in-Airflow)
+ [How do you make the module available to airflow if you're using Docker Compose?](#How-do-you-make-the-module-available-to-airflow-if-you're-using-Docker-Compose)
+ [How to schedule DAG in Airflow?](#How-to-schedule-DAG-in-Airflow)
+ [What is XComs In Airflow?](#What-is-XComs-In-Airflow)
+ [What is xcom_pull in XCom Airflow?](#What-is-xcom_pull-in-XCom-Airflow)
+ [What is Jinja templates?](#What-is-Jinja-templates)
+ [How to use Airflow XComs in Jinja templates?](#How-to-use-Airflow-XComs-in-Jinja-templates)

## What is Airflow?
Apache Airflow is an open-source workflow management platform. It began in October 2014 at Airbnb as a solution for managing the company's increasingly complex workflows. Airbnb's creation of Airflow enabled them to programmatically author, schedule, and monitor their workflows via the built-in Airflow user interface. Airflow is a data transformation pipeline ETL (Extract, Transform, Load) workflow orchestration tool.

[Table of Contents](#Apache-Airflow)

## What issues does Airflow resolve?
Crons are an old technique of task scheduling.
Scalable
Cron requires external assistance to log, track, and manage tasks. The Airflow UI is used to track and monitor the workflow's execution.
Creating and maintaining a relationship between tasks in cron is a challenge, whereas it is as simple as writing Python code in Airflow.
Cron jobs are not reproducible until they are configured externally. Airflow maintains an audit trail of all tasks completed.

[Table of Contents](#Apache-Airflow)

## Explain how workflow is designed in Airflow?
A directed acyclic graph (DAG) is used to design an Airflow workflow. That is to say, when creating a workflow, consider how it can be divided into tasks that can be completed independently. The tasks can then be combined into a graph to form a logical whole.
The overall logic of your workflow is based on the shape of the graph. An Airflow DAG can have multiple branches, and you can choose which ones to follow and which to skip during workflow execution.
Airflow Pipeline DAG
Airflow could be completely stopped, and able to run workflows would then resume through restarting the last unfinished task.
It is important to remember that airflow operators can be run more than once when designing airflow operators. Each task should be idempotent, or capable of being performed multiple times without causing unintended consequences.

[Table of Contents](#Apache-Airflow)

## Explain Airflow Architecture and its components?
There are four major components to airflow.
+ Webserver
    + This is the Airflow UI built on the Flask, which provides an overview of the overall health of various DAGs and helps visualise various components and states of every DAG. For the Airflow setup, the Web Server also allows you to manage users, roles, and different configurations.
+ Scheduler
    + Every n seconds, the scheduler walks over the DAGs and schedules the task to be executed.Executor
+ Executor is another internal component of the scheduler.
    + The executors are the components that actually execute the tasks, while the Scheduler orchestrates them. Airflow has different types of executors, including SequentialExecutor, LocalExecutor, CeleryExecutor and KubernetesExecutor. People generally choose the executor which is best for their use case.
+ Worker
    + Workers are responsible to run the task that the executor has given them.
+ Metadata Database
Airflow supports a wide range of metadata storage databases. This database contains information about DAGs, their runs, and other Airflow configurations such as users, roles, and connections.
The DAGs' states and runs are shown by the Web Server from the database. This information is also updated in the metadata database by the Scheduler.

[Table of Contents](#Apache-Airflow)

## What are the types of Executors in Airflow?
The executors are the components that actually execute the tasks, while the Scheduler orchestrates them. Airflow has different types of executors, including SequentialExecutor, LocalExecutor, CeleryExecutor and KubernetesExecutor. People generally choose the executor which is best for their use case.
Types of Executor
+ SequentialExecutor
    + Only one task is executed at a time by SequentialExecutor. The scheduler and the workers both use the same machine.
+ LocalExecutor
    + LocalExecutor is the same as the Sequential Executor, except it can run multiple tasks at a time.
+ CeleryExecutor
    + Celery is a Python framework for running distributed asynchronous tasks.
As a result, CeleryExecutor has long been a part of Airflow, even before Kubernetes.
CeleryExecutors has a fixed number of workers on standby to take on tasks when they become available.
+ KubernetesExecutor
    + Each task is run by KubernetesExecutor in its own Kubernetes pod. It, unlike Celery, spins up worker pods on demand, allowing for the most efficient use of resources.

[Table of Contents](#Apache-Airflow)

## What are the pros and cons of SequentialExecutor?
Pros:
+ It's simple and straightforward to set up.
+ It's a good way to test DAGs while they're being developed.
Pros:
It isn't scalable.
It is not possible to perform many tasks at the same time.
Unsuitable for use in production

[Table of Contents](#Apache-Airflow)

## What are the pros and cons of LocalExecutor?
Pros:
+ Able to perform multiple tasks.
+ Can be used to run DAGs during development.
Cons:
+ The product isn't scalable.
+ There is only one point of failure.
+ Unsuitable for use in production.

[Table of Contents](#Apache-Airflow)

## What are the pros and cons of CeleryExecutor?
Pros:
+ It allows for scalability.
+ Celery is responsible for managing the workers. Celery creates a new one in the case of a failure.
Cons:
+ Celery requires RabbitMQ/Redis for task queuing, which is redundant with what Airflow already supports.
+ The setup is also complicated due to the above-mentioned dependencies.

[Table of Contents](#Apache-Airflow)

## What are the pros and cons of KubernetesExecutor?
Pros:
It combines the benefits of CeleryExecutor and LocalExecutor in terms of scalability and simplicity.
Fine-grained control over task-allocation resources. At the task level, the amount of CPU/memory needed can be configured.
Cons:
Airflow is newer to Kubernetes, and the documentation is complicated.

[Table of Contents](#Apache-Airflow)

## How to define a workflow in Airflow?
Python files are used to define workflows.
DAG (Directed Acyclic Graph)
The DAG Python class in Airflow allows you to generate a Directed Acyclic Graph, which is a representation of the workflow.
from Airflow.models import DAG
from airflow.utils.dates import days_ago
​
args = {
'start_date': days_ago(0),
}
​
dag = DAG(
dag_id='bash_operator_example',
default_args=args,
schedule_interval='* * * * *',
)
You can use the start date to launch a task on a specific date.
The schedule interval specifies how often each workflow is scheduled to run. '* * * * *' indicates that the tasks must run every minute.

[Table of Contents](#Apache-Airflow)


## How do you make the module available to airflow if you're using Docker Compose?
If we are using Docker Compose, then we will need to use a custom image with our own additional dependencies in order to make the module available to Airflow. Refer to the following Airflow Documentation for reasons why we need it and how to do it.

[Table of Contents](#Apache-Airflow)

## How to schedule DAG in Airflow?
DAGs could be scheduled by passing a timedelta or a cron expression (or one of the @ presets), which works well enough for DAGs that need to run on a regular basis, but there are many more use cases that are presently difficult to express "natively" in Airflow, or that require some complicated workarounds. You can refer Airflow Improvements Proposals (AIP).
Simply use the following command to start a scheduler:
+ airflow scheduler

[Table of Contents](#Apache-Airflow)

## What is XComs In Airflow?
XCom (short for cross-communication) are messages that allow data to be sent between tasks. The key, value, timestamp, and task/DAG id are all defined.

[Table of Contents](#Apache-Airflow)

## What is xcom_pull in XCom Airflow?
The xcom push and xcom pull methods on Task Instances are used to explicitly "push" and "pull" XComs to and from their storage. Whereas if do xcom push parameter is set to True (as it is by default), many operators and @task functions will auto-push their results into an XCom key named return value.
If no key is supplied to xcom pull, it will use this key by default, allowing you to write code like this:
 Pulls the return_value XCOM from "pushing_task"
value = task_instance.xcom_pull(task_ids='pushing_task')

[Table of Contents](#Apache-Airflow)

## What is Jinja templates?
Jinja is a templating engine that is quick, expressive, and extendable. The template has special placeholders that allow you to write code that looks like Python syntax. After that, data is passed to the template in order to render the final document.

[Table of Contents](#Apache-Airflow)

## How to use Airflow XComs in Jinja templates?
We can use XComs in Jinja templates as given below:
+ SELECT * FROM {{ task_instance.xcom_pull(task_ids='foo', key='table_name') }}

[Table of Contents](#Apache-Airflow)