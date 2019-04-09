def docker_run(args):
        import subprocess
        cmd = ["docker", "run", "--rm"]
        cmd.extend(args)
        cp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out = cp.stdout; err = cp.stderr
        return (out, err)
