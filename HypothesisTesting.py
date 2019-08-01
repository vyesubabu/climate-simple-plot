from scipy import stats


def significance_t_test(baseline, data, confidence_int=0.9):
    """
        baseline: np.array of baseline data
        data: np.array of interested data

        return True if data is significant increase/decrease/difference to baseline
    """
    t_res = stats.ttest_ind(baseline, data)
    if t_res.pvalue >= 1 - confidence_int:
        return False
    else:
        return True
