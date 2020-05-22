import datetime
from airflow import models
from airflow.contrib.operators import kubernetes_pod_operator

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)
dag=models.DAG(
            dag_id='a_pod-ex-minimum',
            schedule_interval=datetime.timedelta(days=1),
            start_date=YESTERDAY) 
        
kubernetes_min_pod = kubernetes_pod_operator.KubernetesPodOperator(
        task_id='pod-ex-minimum',
        name='pod-ex-minimum',
        dag=dag,
        cmds=['echo'],
        namespace='airflow',
        image='ubuntu:16.04',
        config_file="/usr/local/airflow/kube.config",)

