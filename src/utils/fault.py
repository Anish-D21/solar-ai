def detect_fault(predicted_generation, actual_generation, threshold_percent=15.0):
    """
    Detects system inefficiencies by comparing predicted vs actual generation.
    
    Args:
        predicted_generation (float): Monthly expected generation in kWh from ML model.
        actual_generation (float): Monthly actual generation in kWh.
        threshold_percent (float): Allowable deviation before triggering a fault (default 15%).
        
    Returns:
        dict: A dictionary containing fault status, deviation percentage, and alerts.
    """
    if actual_generation <= 0 or predicted_generation <= 0:
        return {
            "fault_detected": False,
            "deviation_percent": 0.0,
            "efficiency_score": 0.0,
            "message": "Valid production data required for fault detection."
        }

    deviation = predicted_generation - actual_generation
    deviation_percent = (deviation / predicted_generation) * 100
    
    # Efficiency score (caps at 100%)
    efficiency_score = min(100.0, (actual_generation / predicted_generation) * 100)

    # Note: deviations < 0 mean actual is higher than predicted (which is good)
    if deviation_percent > threshold_percent:
        message = (
            f"⚠️ Underperformance Alert: System generated {deviation_percent:.1f}% "
            f"less energy than expected. Check for dust, shading, or hardware faults."
        )
        fault_detected = True
    elif actual_generation > predicted_generation * 1.2:
         message = (
             f"✅ Excellent Production: System exceeded expectations by "
             f"{abs(deviation_percent):.1f}%. High efficiency!"
         )
         fault_detected = False
    else:
        message = "✅ System performing nominally within expected range."
        fault_detected = False

    return {
        "fault_detected": fault_detected,
        "deviation_percent": round(deviation_percent, 2),
        "efficiency_score": round(efficiency_score, 2),
        "message": message
    }
