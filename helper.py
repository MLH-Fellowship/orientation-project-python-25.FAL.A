def validate_fields(json_data, required_fields):
    """
    Validates that all required fields are present in the json_data.
    Returns (True, None) if valid, (False, missing_field) if not.
    """
    for field in required_fields:
        if field not in json_data or json_data[field] is None:
            return False, field
    return True, None
