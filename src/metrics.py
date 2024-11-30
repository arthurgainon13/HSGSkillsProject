
def calculate_performance_metrics(data, initial_capital):
    final_value = data['Portfolio Value'].iloc[-1]
    total_return = (final_value / initial_capital) - 1
    return {'final_value': final_value, 'total_return': total_return}
