import pandas as pd
from core.data_processing.dataclasses.manager import TaskResourceManager
from core.data_processing.schedulers.scheduler import greedy_scheduler
from core.data_processing.parser.input_parser import process_problem_input
from core.data_processing.schedulers.scheduler import (
    task_most_blocks, task_least_blocks, task_max_interval, task_min_interval,
    task_most_resource_options, task_fewest_resource_options,
    resource_max_cycle, resource_min_cycle, resource_common_tags,
    resource_rare_tags, resource_most_assignments, resource_fewest_assignments
)

def solve_with_model(problem_input: dict, model_tuple, heuristics_tasks=None, heuristics_resources=None):
    """
    Dado un problema (tareas, recursos, bloques, intervalos) y un modelo entrenado,
    predice la mejor heurística y ejecuta el scheduler correspondiente.

    Parámetros:
    -----------
    problem_input : dict
        Diccionario con la definición del problema: tasks, resources, blocks, intervals.
    model : RandomForestClassifier
        Modelo entrenado para predecir la mejor heurística.
    heuristics_tasks : dict (opcional)
        Diccionario con las funciones de heurísticas de tareas.
    heuristics_resources : dict (opcional)
        Diccionario con las funciones de heurísticas de recursos.

    Retorna:
    --------
    manager : TaskResourceManager
        Manager con el scheduling ejecutado según la heurística predicha.
    predicted_heuristic : str
        Nombre de la heurística combinada elegida por el modelo.
    """
    model, feature_names = model_tuple
    
    if heuristics_tasks is None:
        heuristics_tasks = {
            "most_blocks": task_most_blocks,
            "least_blocks": task_least_blocks,
            "max_interval": task_max_interval,
            "min_interval": task_min_interval,
            "fewest_resource_options": task_fewest_resource_options,
            "most_resource_options": task_most_resource_options
        }

    if heuristics_resources is None:
        heuristics_resources = {
            "max_cycle": resource_max_cycle,
            "min_cycle": resource_min_cycle,
            "fewest_assignments": resource_fewest_assignments,
            "most_assignments": resource_most_assignments
        }

    # Procesar input a features
    features = process_problem_input(problem_input)
    df_features = pd.DataFrame([features])
    print("Columns in DataFrame:", df_features.columns)
    print("Feature names expected:", feature_names)

    
    # Crear diccionario combinado para acceder a funciones por el nombre completo
    combined_heuristics = {}
    for t_name, t_func in heuristics_tasks.items():
        for r_name, r_func in heuristics_resources.items():
            combined_heuristics[f"{t_name}_{r_name}"] = (t_func, r_func)

    # Predecir la heurística combinada
    predicted_heuristic = model.predict(df_features)[0]

    # Obtener las funciones directamente del diccionario combinado
    task_func, resource_func = combined_heuristics[predicted_heuristic]

    # --------------------------
    # Crear manager a partir de problem_input
    # --------------------------
    manager = TaskResourceManager(
        interval_blocks=problem_input["blocks"],
        cicle_intervals=problem_input["intervals"]
    )

    # Agregar tareas
    for t in problem_input["tasks"]:
        manager.add_task(
            name=t["name"],
            time_blocks=t["time_blocks"],
            chooseable_resources={tag: True for tag in t["compatible_tags"]},
            max_per_cicle=t.get("max_per_cicle"),
            min_per_cicle=t.get("min_per_cicle", 0),
            max_per_interval=t.get("max_per_interval"),
            min_per_interval=t.get("min_per_interval", 0)
        )

    # Agregar recursos
    for r in problem_input["resources"]:
        manager.add_resource(
            name=r["name"],
            tags=r["tags"],
            max_per_cicle=r.get("max_per_cicle"),
            min_per_cicle=r.get("min_per_cicle", 0),
            max_per_interval=r.get("max_per_interval"),
            min_per_interval=r.get("min_per_interval", 0)
        )

    # Ejecutar scheduler con las heurísticas elegidas
    greedy_scheduler(manager, task_heuristic=task_func, resource_heuristic=resource_func)

    return manager, predicted_heuristic