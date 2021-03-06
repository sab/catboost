import json

import process
import runtime


def execute_benchmark(path, budget=None, threads=None):
    """
    Run benchmark and return values
    :param path: path to benchmark binary
    :param budget: time budget, sec
    :param threads: number of threads to run benchmark
    :return: map of benchmark values
    """
    benchmark_path = runtime.binary_path(path)
    cmd = [benchmark_path, "-f", "json"]
    if budget is not None:
        cmd += ["-b", str(budget)]
    if threads is not None:
        cmd += ["-t", str(threads)]
    res = process.execute(cmd)
    return json.loads(res.std_out)
