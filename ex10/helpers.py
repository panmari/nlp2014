def latexify_matrix(m):
    s = " \\\\\n \\hline \n".join(["T{} & ".format(idx) + " & ".join(map(str, line)) for idx, line in enumerate(m)])
    s += " \\\\\n \\hline \n"
    return s