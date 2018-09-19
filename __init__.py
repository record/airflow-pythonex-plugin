from airflow.operators.python_operator import PythonOperator
from airflow.plugins_manager import AirflowPlugin


class PythonExOperator(PythonOperator):
    template_ext = ('.sql',)


class PythonExPlugin(AirflowPlugin):
    name = "pythonex_plugin"
    hooks = []
    operators = [PythonExOperator]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
