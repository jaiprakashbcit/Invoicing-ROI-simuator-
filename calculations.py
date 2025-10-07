def calculate_roi(data):
    # Inputs
    monthly_invoice_volume = float(data.get('monthly_invoice_volume', 0))
    num_ap_staff = float(data.get('num_ap_staff', 0))
    avg_hours_per_invoice = float(data.get('avg_hours_per_invoice', 0))
    hourly_wage = float(data.get('hourly_wage', 0))
    error_rate_manual = float(data.get('error_rate_manual', 0))
    error_cost = float(data.get('error_cost', 0))
    time_horizon_months = float(data.get('time_horizon_months', 12))
    one_time_implementation_cost = float(data.get('one_time_implementation_cost', 0))

    # Internal constants (server-side)
    automated_cost_per_invoice = 0.20
    error_rate_auto = 0.001
    min_roi_boost_factor = 1.1

    # Calculations
    labor_cost_manual = num_ap_staff * hourly_wage * avg_hours_per_invoice * monthly_invoice_volume
    auto_cost = monthly_invoice_volume * automated_cost_per_invoice
    error_savings = (error_rate_manual - error_rate_auto) * monthly_invoice_volume * error_cost
    monthly_savings = (labor_cost_manual + error_savings) - auto_cost
    monthly_savings *= min_roi_boost_factor

    cumulative_savings = monthly_savings * time_horizon_months
    net_savings = cumulative_savings - one_time_implementation_cost
    payback_months = one_time_implementation_cost / monthly_savings if monthly_savings > 0 else 0
    roi_percentage = (net_savings / one_time_implementation_cost) * 100 if one_time_implementation_cost > 0 else 0

    return {
        "monthly_savings": round(monthly_savings, 2),
        "cumulative_savings": round(cumulative_savings, 2),
        "net_savings": round(net_savings, 2),
        "payback_months": round(payback_months, 1),
        "roi_percentage": round(roi_percentage, 2)
    }
