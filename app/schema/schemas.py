def individual_serial(model_instance: object, model_id: str) -> dict:
    model_dict = model_instance.model_dump()
    return {"id": model_id, **model_dict}


def list_serial(models: list, model_class: object) -> list:
    return [
        individual_serial(model_class(**model), str(model["_id"]))
        for model in models
    ]
