import numpy as np 

def sample_with_temperature(prob_dist, temperature=1.0):
    """
    Model's last layer is softmax, so prob_dist already sums to 1.
    To apply temperature we have to undo the softmax (log), rescale, redo it.
    temperature -> 0   : greedy, picks the max every time
    temperature == 1   : sample exactly as the model predicts
    temperature > 1    : flatter distribution, more chaotic/creative
    """
    prob_dist = np.asarray(prob_dist).astype("float64")
    prob_dist = np.clip(prob_dist, 1e-10, 1.0)  # avoid log(0)

    if temperature <= 1e-3:
        return int(np.argmax(prob_dist))  # greedy, temperature basically off

    logits = np.log(prob_dist) / temperature
    exp_preds = np.exp(logits - np.max(logits))  # subtract max for numerical stability
    rescaled = exp_preds / np.sum(exp_preds)

    return int(np.random.choice(len(rescaled), p=rescaled))