#!/usr/bin/env python3
import numpy as np


def create_confusion_matrix(labels, logits):
    return np.matmul(labels.transpose(), logits)
