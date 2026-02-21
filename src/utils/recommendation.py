def recommend_system_size(monthly_usage, roof_area):
    """
    Recommend solar system size (kW)
    based on usage + available roof.
    """

    # Rule-based baseline from your design doc
    if monthly_usage < 200:
        size = 1
    elif monthly_usage < 500:
        size = 3
    else:
        size = 5

    # Roof constraint (1 kW needs ~100 sq ft)
    max_possible = roof_area / 100

    return round(min(size, max_possible), 2)