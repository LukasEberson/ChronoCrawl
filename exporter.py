import pandas as pd

def export_results(results, format='csv'):
    df = pd.DataFrame(results)
    filename = f"chrono_results.{format}"
    if format == 'csv':
        df.to_csv(filename, index=False)
    elif format == 'xlsx':
        df.to_excel(filename, index=False)
    print(f"Results saved to {filename}")
