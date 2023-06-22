# TTM-challenge-CVPR-23

This is the code base we used for [Ego4d TTM challenge](https://eval.ai/web/challenges/challenge-page/1625/overview) held at CVPR'23. We secured the second place in the contest.

## Approach

You can locate a technical report within this repository. Our approach relies on Transformer-based models. To enhance the performance, we have employed an ensemble of two trained models. We may explore further improvements to our approach in the future. As a result, at this moment, we can only provide two JSON files, which contain predictions from the two trained models on the test set, along with the ensemble script.

## Reference

We suggest preprocessing the data following:

https://github.com/facebookresearch/Ego4d/blob/main/ego4d/cli/README.md

https://github.com/EGO4D/social-interactions/tree/ttm/scripts


