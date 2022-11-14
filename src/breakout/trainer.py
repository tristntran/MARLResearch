"""
_summary_


"""

def init_model(ALGO: callable, policy: str, env: str, n_steps: int, ):
    """
    _summary_

    :param ALGO: _description_
    :param policy: _description_
    :param env: _description_
    :param n_steps: _description_
    :return: _description_
    """
    model = ALGO(policy, env, verbose=1)
    return model

def load_model(ALGO:callable, file_path: str):
    """
    _summary_

    :param ALGO: _description_
    :param file_path: _description_
    """
    model = ALGO.load(file_path)
    return model