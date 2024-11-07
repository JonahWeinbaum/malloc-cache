import subprocess


def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)


def read(process):
    return process.stdout.readline().decode("utf-8").strip()


def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()


def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)

def monte_carlo(iters=1000):
    malloc1_avg = 0
    malloc2_avg = 0
    for i in range(iters):
        process = start("./malloc_cache")
        malloc1_avg += float(read(process)[-8:])
        malloc2_avg += float(read(process)[-8:])
    malloc1_avg /= iters
    malloc2_avg /= iters
    print(f"First malloc timing - {malloc1_avg}")
    print(f"Second malloc timing - {malloc2_avg}")
        
monte_carlo()
