from app_usage_utils import load_app_usage, app_usage_distance, annotate_app_usage
import matplotlib.pyplot as plt
import forcelayout as fl
import sys

algorithms = {
    'brute': fl.SpringForce,
    'chalmers96': fl.NeighbourSampling,
    'hybrid': fl.Hybrid,
    'pivot': fl.Pivot,
}

if len(sys.argv) < 2:
    print(f'\nusage: python3 animated_app_usage_layout.py <dataset size> <algorithm>')
    print('\tSizes: see datasets/app_usage')
    print('\tAvailable algorithms: brute, chalmers96, hybrid, pivot')
    exit(1)

if len(sys.argv) > 2 and sys.argv[2] not in algorithms:
    print('\tAvailable algorithms: brute, chalmers96, hybrid, pivot')
    exit(1)

data_set_size = int(sys.argv[1])
app_usage = load_app_usage(data_set_size)
algorithm = sys.argv[2].lower() if len(sys.argv) > 2 else 'pivot'
print(
    f"Creating Layout of {len(app_usage)} app usage using {algorithm} algorithm")

algorithm = algorithms[algorithm]

plt.figure(figsize=(8.0, 8.0))

animated_spring_layout = fl.draw_spring_layout_animated(dataset=app_usage,
                                                        distance=app_usage_distance,
                                                        algorithm=algorithm,
                                                        alpha=0.7,
                                                        color_by=lambda d: d[3],
                                                        annotate=annotate_app_usage,
                                                        algorithm_highlights=True)
plt.show()
